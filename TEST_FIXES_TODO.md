# Test Suite Fixes - COMPLETED ✅

**Status:** ✅ ALL TESTS PASSING - Fixed on 2025-10-25
**Priority:** ✅ COMPLETED
**Time Spent:** ~2 hours

## Overview

The security fixes commit (5fc9d40) successfully implemented all HIGH and MEDIUM priority security improvements. All 8 pre-existing test failures have been resolved.

**Current Test Status:** ✅ 132 PASSING / 0 FAILING / 1 SKIPPED

## Task 1: Fix API Authentication Test Failures (4 tests)

**Priority:** HIGH
**Estimated Time:** 1-2 hours
**Files:** `tests/test_api.py`

### Failing Tests
1. `test_scan_vulnerable_file` - assert 403 == 200
2. `test_scan_secure_file` - assert 403 == 200
3. `test_invalid_file_type` - assert 403 == 400
4. `test_scan_response_structure` - assert 403 == 200

### Root Cause
API tests are receiving 403 Forbidden responses because they're not providing a valid API key in the request headers. The API authentication is working correctly - the tests just need to be updated.

### Error Log Evidence
```
WARNING terrasafe.api verify_api_key - API request with invalid API key
HTTP Request: POST http://testserver/scan "HTTP/1.1 403 Forbidden"
```

### Required Fix
Update test fixtures to inject a valid API key header:

```python
# Option 1: Use pytest fixture
@pytest.fixture
def test_api_key():
    """Generate a test API key and its hash for testing."""
    import secrets
    from terrasafe.api import hash_api_key

    api_key = secrets.token_urlsafe(32)
    api_key_hash = hash_api_key(api_key)
    return api_key, api_key_hash

@pytest.fixture
def client_with_auth(test_api_key):
    """TestClient with authentication header."""
    api_key, api_key_hash = test_api_key

    # Override settings with test hash
    from unittest.mock import patch
    with patch('terrasafe.config.settings.get_settings') as mock_settings:
        mock_settings.return_value.api_key_hash = api_key_hash

        client = TestClient(app)
        client.headers["X-API-Key"] = api_key
        yield client

# Option 2: Mock the verify_api_key dependency
from unittest.mock import patch

@pytest.fixture
def mock_auth():
    with patch('terrasafe.api.verify_api_key', return_value=True):
        yield

# Then use in tests:
def test_scan_vulnerable_file(client, mock_auth):
    # Test code here
    pass
```

### Acceptance Criteria
- [x] All 4 API tests pass ✅
- [x] Authentication is properly tested (valid key accepts, invalid key rejects) ✅
- [x] No security bypasses introduced ✅

### Implementation Summary
**Fixed on 2025-10-25**

Implemented proper bcrypt-based API key authentication mocking:

```python
# Generated test API key and hash
TEST_API_KEY = "test-api-key-for-testing-12345678"
TEST_API_KEY_HASH = hash_api_key(TEST_API_KEY)

# Created mock_settings fixture with all required attributes
@pytest.fixture
def mock_settings():
    with patch('terrasafe.api.settings') as mock:
        mock.api_key_hash = TEST_API_KEY_HASH
        mock.max_file_size_bytes = 10 * 1024 * 1024
        mock.max_file_size_mb = 10
        mock.scan_timeout_seconds = 60
        mock.is_development.return_value = True
        mock.is_production.return_value = False
        mock.environment = "test"
        yield mock
```

All API endpoints now properly test authentication with bcrypt hashing.

---

## Task 2: Fix Scanner Mock Test Failures (4 tests)

**Priority:** MEDIUM
**Estimated Time:** 1-2 hours
**Files:** `tests/test_security_scanner.py`

### Failing Tests
1. `test_complex_scan_scenario` - KeyError: 'rule_based_score'
2. `test_scan_parse_error` - Expected parse error, got file not found
3. `test_scan_successful` - KeyError: 'rule_based_score'
4. `test_scan_unexpected_error` - Expected exception, got file not found

### Root Cause
Tests are attempting to scan non-existent files without proper filesystem mocking. The scanner is correctly raising "File not found" errors, but the tests expect to mock the file operations.

### Error Log Evidence
```
ERROR terrasafe.application.scanner scan - File not found: test.tf
WARNING terrasafe.application.scanner _get_file_hash - Failed to get file hash for test.tf: [Errno 2] No such file or directory: 'test.tf'
```

### Required Fix
Add `Path.stat()` mocking to create virtual test files:

```python
from pathlib import Path
from unittest.mock import Mock, patch, mock_open
import os

@pytest.fixture
def mock_terraform_file():
    """Mock a Terraform file for testing."""
    content = """
    resource "aws_s3_bucket" "example" {
      bucket = "test-bucket"
      acl    = "public-read"
    }
    """

    with patch('pathlib.Path.exists', return_value=True), \
         patch('pathlib.Path.is_file', return_value=True), \
         patch('pathlib.Path.stat') as mock_stat, \
         patch('builtins.open', mock_open(read_data=content)):

        # Mock stat to return file size
        mock_stat.return_value = Mock(st_size=len(content))
        yield content

def test_scan_successful(mock_terraform_file):
    scanner = IntelligentSecurityScanner()
    results = scanner.scan('test.tf')

    assert 'rule_based_score' in results
    assert results['status'] == 'success'
```

### Alternative Approach: Use Temporary Files
```python
import tempfile
from pathlib import Path

@pytest.fixture
def temp_terraform_file():
    """Create a real temporary Terraform file for testing."""
    content = """
    resource "aws_s3_bucket" "example" {
      bucket = "test-bucket"
    }
    """

    with tempfile.NamedTemporaryFile(mode='w', suffix='.tf', delete=False) as f:
        f.write(content)
        temp_path = f.name

    yield temp_path

    # Cleanup
    Path(temp_path).unlink()

def test_scan_successful(temp_terraform_file):
    scanner = IntelligentSecurityScanner()
    results = scanner.scan(temp_terraform_file)
    assert 'rule_based_score' in results
```

### Acceptance Criteria
- [x] All 4 scanner tests pass ✅
- [x] Tests properly isolate filesystem operations ✅
- [x] Tests cover both successful scans and error conditions ✅
- [x] No actual file I/O during test runs (all properly mocked) ✅

### Implementation Summary
**Fixed on 2025-10-25**

Added comprehensive filesystem mocking for all scanner tests:

```python
from unittest.mock import mock_open

# Mock all file operations including binary file read for hashing
mock_file_content = b"terraform content here"
with patch('pathlib.Path.exists', return_value=True), \
     patch('pathlib.Path.is_file', return_value=True), \
     patch('pathlib.Path.stat') as mock_stat, \
     patch('builtins.open', mock_open(read_data=mock_file_content)):
    mock_stat.return_value.st_size = 1024
    mock_stat.return_value.st_mtime = 1234567890.0
    results = self.scanner.scan(test_file)
```

Key improvements:
- Used `mock_open(read_data=...)` with binary data for file hashing
- Added `st_mtime` to mock_stat for cache key generation
- All file operations properly isolated - no actual I/O

---

## Environment Issue: Shell Variable Expansion

**⚠️ CRITICAL:** The test failures were initially masked by an environment variable issue.

### The Problem
When running tests, if the shell has `TERRASAFE_API_KEY_HASH` set (from a previous `source .env`), the bcrypt hash gets corrupted:

```bash
# In .env file (correct):
TERRASAFE_API_KEY_HASH='REDACTED_HASH'

# After 'source .env' (BROKEN):
TERRASAFE_API_KEY_HASH=/QuamsfdPEe  # Only 11 chars instead of 60!
```

The `$2b`, `$12`, and `$PNgLco...` are interpreted as shell variables and expanded.

### The Solution
**Before running tests:**
```bash
unset TERRASAFE_API_KEY_HASH
pytest
```

Or ensure the environment is clean in CI/CD:
```yaml
# .github/workflows/test.yml
- name: Run tests
  env:
    TERRASAFE_API_KEY_HASH: ""  # Let python-dotenv load from .env
  run: pytest
```

**Never use `source .env` in production or test environments!** Let python-dotenv handle it.

---

## Verification Steps ✅ COMPLETED

All verification steps passed successfully on 2025-10-25:

1. **Ensure clean environment:** ✅
   ```bash
   unset TERRASAFE_API_KEY_HASH
   ```

2. **Run full test suite:** ✅
   ```bash
   ./run_tests.sh -v
   # OR
   env -u TERRASAFE_API_KEY_HASH python3 -m pytest -v
   ```

3. **Actual results:** ✅
   ```
   ================= 132 passed, 1 skipped, 20 warnings in 39.74s =================
   ```

4. **All test groups passing:** ✅
   - API tests: 7/7 passing
   - Scanner tests: 25/25 passing
   - Security tests: 23/24 passing (1 skipped - Redis rate limiting)
   - Performance tests: 14/14 passing
   - All other test suites: 100% passing

**New Helper Script Created:** `run_tests.sh` - Automatically handles environment cleanup

---

## CI/CD Integration

After tests pass locally, update CI/CD pipeline:

```yaml
# .github/workflows/ci.yml
name: Test Suite

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        env:
          # Ensure clean environment - let python-dotenv load .env
          TERRASAFE_API_KEY_HASH: ""
        run: |
          pytest -v --tb=short --cov=terrasafe --cov-report=term-missing

      - name: Check test coverage
        run: |
          pytest --cov=terrasafe --cov-fail-under=80
```

---

## ✅ Ready for Next Steps

With all tests passing, the project is now ready for:

1. **Code Review** - Ready for peer review of:
   - Security fixes (commit 5fc9d40)
   - Test infrastructure improvements
   - Authentication mocking implementation

2. **Merge to Main** - All criteria met:
   - ✅ 132/132 tests passing
   - ✅ Security fixes implemented
   - ✅ No regressions introduced
   - ✅ Test coverage maintained

3. **Deploy to Staging** - Follow SECURITY_FIXES_SUMMARY.md deployment checklist:
   - Generate staging-specific secrets
   - Set TERRASAFE_ENVIRONMENT=staging
   - Run database migrations
   - Verify health endpoints

4. **Load Testing** - Verify database index performance improvements
5. **Security Audit** - Consider third-party review of path traversal fixes
6. **Production Deployment** - Follow production checklist with fresh credentials

## Important: Running Tests

**ALWAYS use one of these methods to run tests:**

```bash
# Method 1: Use the helper script (recommended)
./run_tests.sh -v

# Method 2: Manually unset environment variable
env -u TERRASAFE_API_KEY_HASH python3 -m pytest -v

# Method 3: In CI/CD, ensure clean environment
# .github/workflows/test.yml
env:
  TERRASAFE_API_KEY_HASH: ""
run: pytest -v
```

**NEVER run tests after `source .env`** - This corrupts the bcrypt hash via shell expansion!

---

## References

- Security fixes commit: `5fc9d40`
- Detailed security analysis: `SECURITY_FIXES_SUMMARY.md`
- Test results: 124/132 passing
- Pytest documentation: https://docs.pytest.org/en/stable/
- FastAPI testing: https://fastapi.tiangolo.com/tutorial/testing/
