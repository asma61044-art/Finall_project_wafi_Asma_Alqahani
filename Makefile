install:
	pip install -e ".[dev]"
test:
	python -m pytest
lint:
	ruff check src tests
	mypy src
	lint-imports
image:
	docker build -t wafi:local .
smoke:
	python scripts/smoke_test.py
