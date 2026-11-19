"""API de laboratorio. Solo para uso local."""
import hmac
import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()

app = Flask(__name__)
DB_PATH = Path(os.environ.get("DB_PATH", Path(__file__).with_name("practica.db")))


def require_env(name):
    """Lee un secreto obligatorio desde el entorno; la API no arranca sin él."""
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Falta la variable de entorno {name}. Copia .env.example a .env y complétala.")
    return value


API_KEY = require_env("API_KEY")


def init_db():
    """Crea datos ficticios para probar el endpoint de autenticación."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users "
            "(id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
        )
        conn.executemany(
            "INSERT OR REPLACE INTO users (id, username, password) VALUES (?, ?, ?)",
            [
                (1, "admin", require_env("DEMO_ADMIN_PASSWORD")),
                (2, "estudiante", require_env("DEMO_STUDENT_PASSWORD")),
            ],
        )


@app.get("/api/health")
def health():
    return jsonify(status="ok", service="API de práctica")


@app.get("/api/profile")
def profile():
    provided = request.headers.get("X-API-Key", "")
    # Comparación en tiempo constante para no filtrar la clave por tiempos de respuesta.
    if not hmac.compare_digest(provided.encode(), API_KEY.encode()):
        return jsonify(error="No autorizado"), 401
    return jsonify(user="admin", message="Acceso de demostración")


@app.post("/api/login")
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "")
    password = data.get("password", "")

    # Vulnerabilidad intencional: SQL concatenado con datos del usuario.
    query = (
        "SELECT id, username FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(query).fetchone()

    if row:
        return jsonify(message="Login correcto", user={"id": row[0], "username": row[1]})
    return jsonify(error="Credenciales inválidas"), 401


if __name__ == "__main__":
    init_db()
    # Escucha solo en localhost. No publicar esta API vulnerable en Internet.
    app.run(host="127.0.0.1", port=5000, debug=False)
