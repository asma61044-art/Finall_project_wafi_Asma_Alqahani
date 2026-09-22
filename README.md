# Wafi — IT Helpdesk Ticket Triage

Capstone for SDA-AIE-113. A lightweight rule-based service that routes IT tickets to a team and assigns `low`, `medium`, or `urgent` urgency.

## Run
```bash
make install
make test
make lint
docker compose up --build
```

API:
`POST /v1/predict` with `{"ticket_id":"T-1","text":"All users cannot access the service"}`.

`/health` is liveness and `/ready` is real readiness. Unknown request fields are rejected. The model is warmed only during startup.

Architecture: `domain` → `service` → `adapters` → `api`; the model is hidden behind a Protocol.

The project includes unit, integration and behavioural tests, an immutable golden file, Docker/Compose, non-root container execution, JSON logs with trace IDs, typed settings, CI/CD, benchmark/decision documents and a 5+ commit Git history.

Before final submission, enable GitHub branch protection on `main` as required by the course specification.
