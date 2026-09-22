# Benchmarks

Run these commands on the final submission machine and paste the measured output below.

```bash
/usr/bin/time -p python -m pytest
/usr/bin/time -p docker build -t wafi:local .
docker image inspect wafi:local --format '{{.Size}} bytes'
```

## Recorded results

- Test time: `TO BE RECORDED`
- Docker build time: `TO BE RECORDED`
- Docker image size: `TO BE RECORDED`
- Coverage: produced by `make test`

Acceptance targets from the course specification:
- image <= 500 MB
- fast test gate <= 60 seconds
- core-layer branch coverage >= 80%
