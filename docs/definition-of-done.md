# Definition of Done — Grupo 8

Una historia del backlog solo se considera **terminada** cuando cumple todos estos criterios:

1. Cumple el criterio de aceptación descrito en el issue.
2. **Seguridad (obligatorio):** el código pasa el escaneo de Bandit sin alertas (el job *SAST* del pipeline termina en verde).
3. **Seguridad (obligatorio):** el código es revisado por otro integrante mediante Pull Request antes de integrarse a `main`.
4. pip-audit no reporta vulnerabilidades conocidas en las dependencias (job *SCA* en verde).
5. detect-secrets no encuentra credenciales nuevas; los secretos se leen desde variables de entorno.
6. Las pruebas automatizadas pasan.
