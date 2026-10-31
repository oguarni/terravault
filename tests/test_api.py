"""API integration tests — exercise the real FastAPI pipeline via TestClient."""
import logging
import tempfile

import pytest

from terravault.api import UPLOAD_CHUNK_SIZE_BYTES


def assert_private_scan_logs(caplog, canary):
    """Check messages and exception rendering, including DEBUG records."""
    records = [record for record in caplog.records if record.name.startswith('terravault')]
    assert records
    for record in records:
        assert canary not in record.getMessage()
        assert canary not in (record.exc_text or '')
        if record.exc_info:
            assert canary not in logging.Formatter().formatException(record.exc_info)
        if record.name == 'terravault.api' and record.levelno >= logging.INFO:
            assert tempfile.gettempdir() not in record.getMessage()
            assert '/tmp' not in record.getMessage()


# ---------------------------------------------------------------------------
# Health / metrics
# ---------------------------------------------------------------------------

def test_health_endpoint_returns_healthy_status(api_client):
    response = api_client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_metrics_endpoint_exposes_scan_counter_when_available(api_client):
    response = api_client.get("/metrics")

    assert response.status_code in (200, 503)
    if response.status_code == 200:
        assert "terravault_scans_total" in response.text


# ---------------------------------------------------------------------------
# Authentication — parametrized across the two failure modes
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "headers, expected_detail_fragment",
    [
        pytest.param({}, "Missing API Key", id="missing_key"),
        pytest.param({"X-API-Key": "invalid-api-key-12345"}, "Invalid API Key", id="invalid_key"),
    ],
)
def test_scan_rejects_requests_without_valid_api_key(
    api_client, vulnerable_tf, headers, expected_detail_fragment
):
    response = api_client.post(
        "/scan",
        files={"file": ("test.tf", vulnerable_tf, "text/plain")},
        headers=headers,
    )

    assert response.status_code == 403
    assert expected_detail_fragment in response.json()["detail"]


# ---------------------------------------------------------------------------
# Scan behaviour — high/low risk on real Terraform content
# ---------------------------------------------------------------------------

def test_scan_vulnerable_file_returns_high_risk_score(api_client, api_headers, vulnerable_tf):
    response = api_client.post(
        "/scan",
        files={"file": ("vulnerable.tf", vulnerable_tf, "text/plain")},
        headers=api_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["score"] >= 70
    assert len(data["vulnerabilities"]) > 0


def test_scan_secure_file_returns_low_risk_score(api_client, api_headers, secure_tf):
    response = api_client.post(
        "/scan",
        files={"file": ("secure.tf", secure_tf, "text/plain")},
        headers=api_headers,
    )

    assert response.status_code == 200
    # Bound tracks the anomaly model, not the rules: the corpus-trained Isolation
    # Forest scores hardened files near 45 on the ML axis, which carries 0.4 of
    # the hybrid weight, so a secure file lands in the low 30s with zero findings.
    assert response.json()["score"] <= 35


# ---------------------------------------------------------------------------
# Upload validation — parametrized across invalid-file scenarios
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "filename, content, expected_status, expected_detail_fragment",
    [
        pytest.param("test.txt", b"not terraform", 400, "Terraform file", id="wrong_extension"),
        pytest.param("empty.tf", b"", 400, "empty", id="empty_body"),
    ],
)
def test_scan_rejects_invalid_uploads(
    api_client, api_headers, filename, content, expected_status, expected_detail_fragment
):
    response = api_client.post(
        "/scan",
        files={"file": (filename, content, "text/plain")},
        headers=api_headers,
    )

    assert response.status_code == expected_status
    assert expected_detail_fragment.lower() in response.json()["detail"].lower()


def test_scan_stops_reading_an_oversized_upload_instead_of_buffering_it_all(
    api_client, api_headers, mock_api_settings, monkeypatch
):
    """Regression: `await file.read()` pulled the entire body into memory and
    only then compared its length to the cap, so the limit reported damage that
    had already been done. The handler must read in bounded chunks and stop one
    chunk past the cap."""
    from starlette.datastructures import UploadFile

    mock_api_settings.max_file_size_bytes = 1024
    mock_api_settings.max_file_size_mb = 0.001

    bytes_read = []
    original_read = UploadFile.read

    async def counting_read(self, size=-1):
        chunk = await original_read(self, size)
        bytes_read.append(len(chunk))
        return chunk

    monkeypatch.setattr(UploadFile, "read", counting_read)

    oversized = b"x" * (5 * 1024 * 1024)
    response = api_client.post(
        "/scan",
        files={"file": ("huge.tf", oversized, "text/plain")},
        headers=api_headers,
    )

    assert response.status_code == 413
    assert "File too large" in response.json()["detail"]

    # Bounded: the cap plus at most one read granularity, never the whole body.
    assert sum(bytes_read) <= mock_api_settings.max_file_size_bytes + UPLOAD_CHUNK_SIZE_BYTES
    assert sum(bytes_read) < len(oversized)


def test_scan_rejects_file_exceeding_configured_size_limit(
    api_client, api_headers, mock_api_settings
):
    mock_api_settings.max_file_size_bytes = 100
    mock_api_settings.max_file_size_mb = 0.0001

    response = api_client.post(
        "/scan",
        files={"file": ("large.tf", b"x" * 200, "text/plain")},
        headers=api_headers,
    )

    assert response.status_code == 413
    detail = response.json()["detail"]
    assert "File too large" in detail
    assert "0.0001MB" in detail


@pytest.mark.unit
@pytest.mark.parametrize(
    'filename, expected_name',
    [('my-infra.tf', 'my-infra.tf'), ('../../my infra.tf', 'my_infra.tf')],
)
def test_scan_returns_safe_upload_name(api_client, api_headers, secure_tf, filename, expected_name):
    response = api_client.post(
        '/scan', files={'file': (filename, secure_tf, 'text/plain')}, headers=api_headers,
    )

    assert response.status_code == 200
    assert response.json()['file'] == expected_name
    assert tempfile.gettempdir() not in response.text
    assert '/tmp' not in response.text


@pytest.mark.unit
def test_malformed_upload_keeps_content_and_paths_private(api_client, api_headers, caplog):
    canary = 'CANARY_SECRET_9f3b2c'
    caplog.set_level(logging.DEBUG, logger='terravault')
    response = api_client.post(
        '/scan', files={'file': ('broken.tf', f'password = "{canary}"\n@invalid', 'text/plain')},
        headers=api_headers,
    )

    assert response.status_code == 422
    assert response.json()['detail'] == 'Terraform parse error: the file is not valid HCL or JSON'
    for forbidden in (canary, tempfile.gettempdir(), '/tmp', 'Token('):
        assert forbidden not in response.text
    assert_private_scan_logs(caplog, canary)


@pytest.mark.unit
@pytest.mark.parametrize(
    'error_type, expected_detail',
    [
        ('TerraformParseError', 'Terraform parse error: the file is not valid HCL or JSON'),
        ('FileNotFoundError', 'Scan failed: the uploaded file is unavailable'),
        ('PermissionError', 'Scan failed: the uploaded file could not be accessed'),
        ('ValueError', 'Terraform scan failed'),
        (None, 'Terraform scan failed'),
    ],
)
def test_scan_failure_uses_controlled_detail(
    api_client, api_headers, secure_tf, monkeypatch, caplog, error_type, expected_detail,
):
    from terravault import api

    canary = 'CANARY_SECRET_9f3b2c'
    caplog.set_level(logging.DEBUG, logger='terravault')

    def fail_scan(filepath, display_name):
        return {'score': -1, 'file': filepath, 'error': canary, 'error_type': error_type}

    monkeypatch.setattr(api.scanner, 'scan', fail_scan)
    response = api_client.post(
        '/scan', files={'file': ('failed.tf', secure_tf, 'text/plain')}, headers=api_headers,
    )

    assert response.status_code == 422
    assert response.json()['detail'] == expected_detail
    assert_private_scan_logs(caplog, canary)


@pytest.mark.unit
def test_unexpected_scan_exception_keeps_content_private(
    api_client, api_headers, secure_tf, monkeypatch, caplog,
):
    from terravault import api

    canary = 'CANARY_SECRET_9f3b2c'
    caplog.set_level(logging.DEBUG, logger='terravault')

    def fail_scan(filepath, display_name):
        raise RuntimeError(canary + filepath)

    monkeypatch.setattr(api.scanner, 'scan', fail_scan)
    response = api_client.post(
        '/scan', files={'file': ('../my infra.tf', secure_tf, 'text/plain')}, headers=api_headers,
    )

    assert response.status_code == 500
    assert response.json()['detail'] == 'Internal server error during scan'
    assert_private_scan_logs(caplog, canary)
    errors = [record for record in caplog.records if record.name == 'terravault.api'
              and record.levelno == logging.ERROR]
    assert any("'my_infra.tf': RuntimeError" in record.getMessage() for record in errors)
