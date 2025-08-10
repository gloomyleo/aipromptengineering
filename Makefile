# Makefile helpers

.PHONY: setup lint docs-serve docs-build clean

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	. .venv/bin/activate && pip install mkdocs mkdocs-material

lint:
	flake8 labs --max-line-length=120 --extend-ignore=E203,W503 || true

docs-serve:
	. .venv/bin/activate && mkdocs serve -a 127.0.0.1:8001

docs-build:
	. .venv/bin/activate && mkdocs build

clean:
	rm -rf site dist build .pytest_cache **/__pycache__
