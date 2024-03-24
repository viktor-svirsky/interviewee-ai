.PHONY: clean-pyc clean-build docs clean env dev_env

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "run - run the project"
	@echo "env - create a new virtual environment"

clean: clean-build clean-pyc clean-test

dev_env: env
	if [ ! -f env/bin/py.test ]; then env/bin/python -m pip install -q -I -r requirements.txt -r requirements-dev.txt; fi

lint: dev_env
	env/bin/python -m black . && env/bin/python -m flake8 app.py

test: dev_env
	env/bin/python -m pytest

env:
	python3.12 -m venv env
	env/bin/python -m pip install -q -U pip setuptools wheel
	env/bin/python -m pip install -q -I -r requirements.txt

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-test:
	rm -rf .tox/
	rm -f .coverage
	rm -rf htmlcov/

run:
	env/bin/python -m app