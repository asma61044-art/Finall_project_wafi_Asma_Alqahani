# Engineering Decisions
1. Rule-based policy: explicitly permitted by the capstone and deterministic for behavioural tests.
2. Protocol model boundary: keeps the model swappable through dependency injection.
3. FastAPI: provides strict validation and the required `/v1/predict` endpoint.
4. Separate health/readiness: liveness does not imply model readiness.
5. Commit-SHA image tags: avoids mutable `latest` production tags and makes releases traceable.
