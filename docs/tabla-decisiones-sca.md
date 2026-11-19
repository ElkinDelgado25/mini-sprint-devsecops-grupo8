# Tabla de decisiones de mitigación (SCA)

Fuente: `pip-audit -r requirements.txt` sobre las dependencias heredadas (54 hallazgos en 5 paquetes; 28 CVE distintos tras quitar duplicados). SBOM: `reports/sbom-original.cyclonedx.json`.

| Paquete | Versión | CVE | ID PyPI | Corregido en | Decisión |
|---|---|---|---|---|---|
| flask | 2.2.2 | CVE-2023-30861 | PYSEC-2023-62 | 2.2.5, 2.3.2 | Actualizar a 3.1.3 |
| flask | 2.2.2 | CVE-2026-27205 | PYSEC-2026-2151 | 3.1.3 | Actualizar a 3.1.3 |
| werkzeug | 2.2.2 | CVE-2023-23934 | PYSEC-2023-57 | 2.2.3 | Actualizar a 3.1.9 |
| werkzeug | 2.2.2 | CVE-2023-25577 | PYSEC-2023-58 | 2.2.3 | Actualizar a 3.1.9 |
| werkzeug | 2.2.2 | CVE-2023-46136 | PYSEC-2023-221 | 2.3.8, 3.0.1 | Actualizar a 3.1.9 |
| werkzeug | 2.2.2 | CVE-2024-34069 | PYSEC-2026-2043 | 3.0.3 | Actualizar a 3.1.9 |
| werkzeug | 2.2.2 | CVE-2024-49766 | PYSEC-2026-2045 | 3.0.6 | Actualizar a 3.1.9 |
| werkzeug | 2.2.2 | CVE-2024-49767 | PYSEC-2026-1860 | 3.0.6 | Actualizar a 3.1.9 |
| werkzeug | 2.2.2 | CVE-2025-66221 | PYSEC-2026-2046 | 3.1.4 | Actualizar a 3.1.9 |
| werkzeug | 2.2.2 | CVE-2026-21860 | PYSEC-2026-2044 | 3.1.5 | Actualizar a 3.1.9 |
| werkzeug | 2.2.2 | CVE-2026-27199 | PYSEC-2026-2320 | 3.1.6 | Actualizar a 3.1.9 |
| werkzeug | 2.2.2 | CVE-2026-102598 | PYSEC-2026-4312 | 3.1.9 | Actualizar a 3.1.9 |
| requests | 2.20.0 | CVE-2023-32681 | PYSEC-2023-74 | 2.31.0 | Actualizar a 2.34.2 |
| requests | 2.20.0 | CVE-2024-35195 | PYSEC-2026-1873 | 2.32.0 | Actualizar a 2.34.2 |
| requests | 2.20.0 | CVE-2024-47081 | PYSEC-2026-1872 | 2.32.4 | Actualizar a 2.34.2 |
| requests | 2.20.0 | CVE-2026-25645 | PYSEC-2026-2275 | 2.33.0 | Actualizar a 2.34.2 |
| idna | 2.7 | CVE-2024-3651 | PYSEC-2024-60 | 3.7 | Se corrige al actualizar requests (resuelve idna ≥ 3.15) |
| idna | 2.7 | CVE-2026-45409 | PYSEC-2026-215 | 3.15 | Se corrige al actualizar requests (resuelve idna ≥ 3.15) |
| urllib3 | 1.24.3 | CVE-2020-26137 | PYSEC-2020-148 | 1.25.9 | Se corrige al actualizar requests (resuelve urllib3 ≥ 2.8.0) |
| urllib3 | 1.24.3 | CVE-2024-37891 | PYSEC-2026-1995 | 1.26.19, 2.2.2 | Se corrige al actualizar requests (resuelve urllib3 ≥ 2.8.0) |
| urllib3 | 1.24.3 | CVE-2023-43804 | PYSEC-2023-192 | 1.26.17, 2.0.6 | Se corrige al actualizar requests (resuelve urllib3 ≥ 2.8.0) |
| urllib3 | 1.24.3 | CVE-2023-45803 | PYSEC-2023-212 | 1.26.18, 2.0.7 | Se corrige al actualizar requests (resuelve urllib3 ≥ 2.8.0) |
| urllib3 | 1.24.3 | CVE-2025-50181 | PYSEC-2026-1999 | 2.5.0 | Se corrige al actualizar requests (resuelve urllib3 ≥ 2.8.0) |
| urllib3 | 1.24.3 | CVE-2025-66418 | PYSEC-2026-1998 | 2.6.0 | Se corrige al actualizar requests (resuelve urllib3 ≥ 2.8.0) |
| urllib3 | 1.24.3 | CVE-2025-66471 | PYSEC-2026-1994 | 2.6.0 | Se corrige al actualizar requests (resuelve urllib3 ≥ 2.8.0) |
| urllib3 | 1.24.3 | CVE-2026-21441 | PYSEC-2026-1996 | 2.6.3 | Se corrige al actualizar requests (resuelve urllib3 ≥ 2.8.0) |
| urllib3 | 1.24.3 | CVE-2026-44431 | PYSEC-2026-141 | 2.7.0 | Se corrige al actualizar requests (resuelve urllib3 ≥ 2.8.0) |
| urllib3 | 1.24.3 | CVE-2026-97689 | PYSEC-2026-4177 | 2.8.0 | Se corrige al actualizar requests (resuelve urllib3 ≥ 2.8.0) |

## Resumen de decisiones

| Dependencia | Riesgo | Decisión | Justificación |
|---|---|---|---|
| Flask 2.2.2 | Medio: fuga de cookie de sesión por caché (`Vary: Cookie`) | **Mitigar: actualizar a 3.1.3** | Cambio de versión mayor sin cambios en las rutas de la API; las pruebas lo validan |
| Werkzeug 2.2.2 | Alto: DoS en el parser multipart, RCE vía depurador, `safe_join` en Windows | **Mitigar: actualizar a 3.1.9** | Es el servidor de la API; 13 avisos, varios explotables en remoto |
| requests 2.20.0 | Medio: fuga de `Proxy-Authorization` y credenciales `.netrc`, verificación TLS | **Mitigar: actualizar a 2.34.2** | No se usa en `app.py`; se mantiene actualizada porque la cátedra la incluye en el escenario |
| idna 2.7 / urllib3 1.24.3 | Medio/alto: DoS, CRLF injection, fuga de cabeceras en redirecciones | **Mitigar por transitividad** | Se resuelven a versiones seguras al actualizar requests |
