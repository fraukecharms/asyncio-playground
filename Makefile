install:
	poetry install && \
	pre-commit install


test:
	python -m pytest -vv tests

# needs to be made consistent with pre-commit formatter
format:
	black .

check:
	pre-commit run --all-files

lint:
	flake8 --ignore=E501,W503,E266,E203

all: install lint
