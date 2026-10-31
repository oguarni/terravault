"""Unit tests for ``IntelligentSecurityScanner`` error paths.

Happy-path scan behaviour is exercised end-to-end via the FastAPI client in
``test_api.py``; this module covers the failure branches that must short-circuit
the pipeline before rule analysis and ML prediction run.
"""
from unittest.mock import Mock
import json
import logging

import pytest

from pydantic import ValidationError

from terravault.application.scanner import IntelligentSecurityScanner
from terravault.config.settings import Settings, get_settings
from terravault.domain.models import Severity, Vulnerability
from terravault.domain.security_rules import SecurityRuleEngine
from terravault.infrastructure.ml_model import MLPredictor
from terravault.infrastructure.parser import HCLParser
from terravault.sarif_formatter import results_to_sarif


pytestmark = pytest.mark.unit


@pytest.fixture
def mock_rule_analyzer():
    return Mock(spec=SecurityRuleEngine)


@pytest.fixture
def mock_ml_predictor():
    return Mock(spec=MLPredictor)


@pytest.fixture
def scanner(mock_rule_analyzer, mock_ml_predictor):
    return IntelligentSecurityScanner(
        parser=HCLParser(),
        rule_analyzer=mock_rule_analyzer,
        ml_predictor=mock_ml_predictor,
    )


@pytest.mark.parametrize(
    "scenario, file_content, expected_error_fragment",
    [
        pytest.param(
            "parse_error",
            "this is { definitely not valid HCL",
            "Invalid HCL/JSON syntax",
            id="invalid_hcl_short_circuits_pipeline",
        ),
        pytest.param(
            "missing_file",
            None,
            "not found",
            id="missing_file_short_circuits_pipeline",
        ),
    ],
)
def test_scanner_returns_error_result_without_invoking_downstream_stages(
    tmp_path,
    scanner,
    mock_rule_analyzer,
    mock_ml_predictor,
    scenario,
    file_content,
    expected_error_fragment,
):
    if file_content is None:
        target = str(tmp_path / "nonexistent.tf")
    else:
        tf_file = tmp_path / "invalid.tf"
        tf_file.write_text(file_content)
        target = str(tf_file)

    results = scanner.scan(target)

    assert results["score"] == -1
    assert expected_error_fragment.lower() in results["error"].lower()
    mock_rule_analyzer.analyze.assert_not_called()
    mock_ml_predictor.predict_risk.assert_not_called()


def test_default_weights_come_from_settings(scanner):
    """A scanner with no explicit weights inherits the configured defaults."""
    settings = get_settings()
    assert scanner.rule_weight == settings.rule_weight
    assert scanner.ml_weight == settings.ml_weight


def test_custom_weights_change_final_score(tmp_path, mock_rule_analyzer, mock_ml_predictor):
    """The hybrid score must honour per-scanner weight overrides."""
    tf_file = tmp_path / "main.tf"
    tf_file.write_text('resource "aws_s3_bucket" "b" {\n  bucket = "demo"\n}\n')
    mock_rule_analyzer.analyze.return_value = [
        Vulnerability(
            severity=Severity.CRITICAL, points=30,
            message="m", resource="r", remediation="fix",
        )
    ]
    mock_ml_predictor.predict_risk.return_value = (80.0, "LOW")

    rules_only = IntelligentSecurityScanner(
        HCLParser(), mock_rule_analyzer, mock_ml_predictor,
        rule_weight=1.0, ml_weight=0.0,
    )
    hybrid = IntelligentSecurityScanner(
        HCLParser(), mock_rule_analyzer, mock_ml_predictor,
        rule_weight=0.6, ml_weight=0.4,
    )

    # rule_score = 30 (single critical), ml_score = 80 (mocked)
    assert rules_only.scan(str(tf_file))["score"] == 30
    assert hybrid.scan(str(tf_file))["score"] == int(0.6 * 30 + 0.4 * 80)


def test_display_name_preserves_cache_and_default_sarif_paths(tmp_path, scanner, mock_rule_analyzer,
                                                            mock_ml_predictor, caplog):
    tf_file = tmp_path / 'main.tf'
    tf_file.write_text('resource "aws_s3_bucket" "b" { bucket = "demo" }')
    mock_rule_analyzer.analyze.return_value = [
        Vulnerability(Severity.HIGH, 20, 'Test finding', 'b', 'Fix finding'),
    ]
    mock_ml_predictor.predict_risk.return_value = (20.0, 'HIGH')
    caplog.set_level(logging.INFO, logger='terravault.application.scanner')

    first = scanner.scan(str(tf_file), display_name='upload.tf')
    cached = scanner.scan(str(tf_file), display_name='renamed.tf')
    assert first['file'] == 'upload.tf'
    assert cached['file'] == 'renamed.tf'
    assert cached['performance']['from_cache'] is True
    assert all(str(tf_file) not in record.getMessage() for record in caplog.records)

    default = scanner.scan(str(tf_file))
    assert default['file'] == str(tf_file)
    sarif_run = json.loads(results_to_sarif([default]))['runs'][0]
    assert sarif_run['artifacts'][0]['location']['uri'] == str(tf_file)
    assert sarif_run['results'][0]['locations'][0]['physicalLocation']['artifactLocation']['uri'] == str(tf_file)


@pytest.mark.parametrize('error_class', [PermissionError, RuntimeError])
def test_scanner_errors_do_not_log_exception_content(tmp_path, scanner, monkeypatch, caplog, error_class):
    tf_file = tmp_path / 'main.tf'
    tf_file.write_text('resource "aws_s3_bucket" "b" {}')
    canary = 'CANARY_SECRET_9f3b2c'

    def fail_parse(filepath):
        raise error_class(canary)

    monkeypatch.setattr(scanner.parser, 'parse', fail_parse)
    caplog.set_level(logging.DEBUG, logger='terravault')
    result = scanner.scan(str(tf_file), display_name='upload.tf')

    assert result['score'] == -1
    assert result['file'] == 'upload.tf'
    assert canary not in result['error']
    assert all(canary not in record.getMessage() for record in caplog.records)
    assert all(not record.exc_info and not record.exc_text for record in caplog.records)


def test_settings_accept_valid_custom_weights():
    """Weights that sum to 1.0 are accepted."""
    settings = Settings(rule_weight=0.8, ml_weight=0.2)
    assert settings.rule_weight == 0.8
    assert settings.ml_weight == 0.2


def test_settings_reject_weights_not_summing_to_one():
    """Weights that do not sum to 1.0 are rejected at construction."""
    with pytest.raises(ValidationError):
        Settings(rule_weight=0.7, ml_weight=0.4)


def test_track_metrics_fallback_is_a_passthrough_when_metrics_unavailable():
    """The ImportError fallback must return the function unchanged.

    ``terravault.metrics`` imports cleanly whenever ``prometheus_client`` is
    installed, so the fallback branch in ``scanner`` never runs in a normal
    suite. Reimport the module with that import forced to fail, and assert the
    decorator is a genuine passthrough — it must not wrap, rename, or otherwise
    alter the function it is handed.
    """
    import builtins
    import importlib
    import sys

    real_import = builtins.__import__

    def failing_import(name, *args, **kwargs):
        if name == "terravault.metrics":
            raise ImportError("simulated: prometheus_client not installed")
        return real_import(name, *args, **kwargs)

    saved = sys.modules.pop("terravault.application.scanner", None)
    builtins.__import__ = failing_import
    try:
        module = importlib.import_module("terravault.application.scanner")

        def sample(value: int) -> int:
            return value * 2

        decorated = module.track_metrics(sample)
        assert decorated is sample
        assert decorated(21) == 42
    finally:
        builtins.__import__ = real_import
        # Restore the normally-imported module so later tests see the real
        # decorator rather than this module's fallback copy.
        sys.modules.pop("terravault.application.scanner", None)
        if saved is not None:
            sys.modules["terravault.application.scanner"] = saved
        else:
            importlib.import_module("terravault.application.scanner")
