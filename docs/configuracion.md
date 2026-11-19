# Configuración segura de la API

La API ya no contiene secretos en el código: los lee de variables de entorno.

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt pre-commit
pre-commit install            # bloqueo de secretos en cada commit
cp .env.example .env          # genera valores propios para cada variable
python app.py                 # http://127.0.0.1:5000
```

| Variable | Uso |
|---|---|
| `API_KEY` | Valor esperado en el encabezado `X-API-Key` de `GET /api/profile` |
| `DEMO_ADMIN_PASSWORD` | Contraseña del usuario `admin` |
| `DEMO_STUDENT_PASSWORD` | Contraseña del usuario `estudiante` |

Las credenciales que aparecen en el `README.md` original del docente ya no son válidas.
