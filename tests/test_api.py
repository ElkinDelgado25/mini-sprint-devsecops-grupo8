import importlib
import secrets

import pytest


def test_health(client):
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_profile_requiere_api_key(client):
    assert client.get("/api/profile").status_code == 401


def test_profile_rechaza_la_clave_hardcodeada_original(client):
    resp = client.get("/api/profile", headers={"X-API-Key": "API_KEY_DEMO_NO_USAR_EN_PRODUCCION"})
    assert resp.status_code == 401


def test_profile_acepta_la_clave_del_entorno(client, creds):
    resp = client.get("/api/profile", headers={"X-API-Key": creds["API_KEY"]})
    assert resp.status_code == 200


def test_login_valido(client, creds):
    resp = client.post("/api/login", json={"username": "admin", "password": creds["DEMO_ADMIN_PASSWORD"]})
    assert resp.status_code == 200
    assert resp.get_json()["user"]["username"] == "admin"


def test_login_password_incorrecto(client):
    wrong = secrets.token_urlsafe(12)
    resp = client.post("/api/login", json={"username": "admin", "password": wrong})
    assert resp.status_code == 401


@pytest.mark.parametrize(
    "username,password",
    [
        ("admin' --", "cualquiera"),
        ("' OR '1'='1", "' OR '1'='1"),
        ("admin' OR 1=1 --", "x"),
    ],
)
def test_login_resiste_inyeccion_sql(client, username, password):
    resp = client.post("/api/login", json={"username": username, "password": password})
    assert resp.status_code == 401


def test_login_sin_datos_devuelve_400(client):
    assert client.post("/api/login", json={}).status_code == 400


def test_la_api_no_arranca_sin_api_key(creds, monkeypatch):
    import app as app_module

    monkeypatch.delenv("API_KEY")
    monkeypatch.setattr("dotenv.load_dotenv", lambda *a, **k: False)
    with pytest.raises(RuntimeError):
        importlib.reload(app_module)
