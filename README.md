# Visites

Petite API FastAPI qui compte les visites dans Redis.

## Routes

| Route          | Rôle                                         |
|----------------|----------------------------------------------|
| `GET /`        | Incrémente le compteur, renvoie `{"visites": N}` |
| `GET /health`  | `200` si Redis répond, `503` sinon           |
| `GET /metrics` | Métriques au format Prometheus               |

## Démarrage

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
docker run -d --name redis -p 6379:6379 redis:8-alpine
pytest -q
uvicorn app.main:app --reload
```

L'adresse de Redis se règle avec la variable `REDIS_URL`
(par défaut `redis://localhost:6379/0`).

Les tests utilisent un faux Redis en mémoire. Pour tester contre le vrai :
`pytest -m integration`.
