.PHONY: clean clean-test clean-pyc clean-build clean-mypy help format
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
	flake8 sample_package tests

test: ## quickly run tests
	python setup.py test

coverage: ## check code coverage
	coverage run --source sample_package setup.py test
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

dist: clean ## build source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

format: format-black sort-import ## format codebase using standard formatters

format-black: ## format code using black
	python -m black pragmail/ tests/

sort-import: ## sort imports in codebase
	python -m isort -rc pragmail/ tests/
