## Historia del backlog
Closes #

## Definition of Done (DoD)
- [ ] El código pasa el escaneo de **Bandit sin alertas** (job SAST en verde).
- [ ] **pip-audit no reporta CVE** en `requirements.txt` (job SCA en verde).
- [ ] **detect-secrets** no encuentra secretos nuevos; los valores sensibles viven en variables de entorno (`.env`).
- [ ] El Pull Request fue **revisado por otro integrante** del equipo antes de fusionar.
- [ ] Las pruebas funcionales pasan.
