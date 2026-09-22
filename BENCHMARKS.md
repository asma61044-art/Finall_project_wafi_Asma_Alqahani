# Benchmarks
Run before submission:
- `time python -m pytest` — test time (must be <=60s).
- `time docker build -t wafi:local .` — build time.
- `docker image inspect wafi:local --format '{{.Size}}'` — image size (must be <=500 MB).
Do not invent measurements; record the actual final-machine results here.
