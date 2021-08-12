.PHONY: clean clean-test clean-pyc clean-build clean-mypy help
.SILENT: format format-black format-import
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test clean-mypy ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean-mypy: ## remove mypy artifacts
	rm -fr .mypy_cache

lint: ## check style with flake8
	flake8 pragmail/ tests/ example/
	pylint pragmail/ tests/ example/

test: ## run tests and check code coverage
	pytest -v --cov=pragmail tests/
	coverage html

dist: clean ## build source and wheel package
	poetry build

install: clean ## install the package to the active Python's site-packages
	poetry install

format: format-black format-import ## format codebase using standard formatters

format-black: ## format code using black
	black pragmail/ tests/ example/

format-import: ## sort imports in codebase
	isort --profile black pragmail/ tests/ example/

setup-dev: ## setup development environment
	poetry shell
	poetry install
	pre-commit install --hook-type commit-msg
