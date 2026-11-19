import importlib
import secrets
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


@pytest.fixture()
def creds(tmp_path, monkeypatch):
    """Secretos aleatorios por prueba: nunca se escriben valores reales en el repositorio."""
    values = {
        "API_KEY": secrets.token_urlsafe(32),
        "DEMO_ADMIN_PASSWORD": secrets.token_urlsafe(16),
        "DEMO_STUDENT_PASSWORD": secrets.token_urlsafe(16),
    }
    for name, value in values.items():
        monkeypatch.setenv(name, value)
    monkeypatch.setenv("DB_PATH", str(tmp_path / "test.db"))
    return values


@pytest.fixture()
def client(creds):
    import app as app_module

    app_module = importlib.reload(app_module)
    app_module.init_db()
    return app_module.app.test_client()
