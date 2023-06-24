.PHONY: install virtualenv ipython clean test watch testcicd lint fmt


install:
	@echo "Installing  for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@echo "Creating virtualenv"
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@echo "Starting ipython"
	@.venv/bin/ipython



clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build


test:             ## Run tests.
	@.venv/bin/pytest -vv -s


testcicd:		   ## Run tests for CI.
	@pytest -v --junitxml=test-result.xml


watch:            ## Run tests on file changes.
	@ls **/*.py | entr pytest

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/isort dundie tests integration
	@.venv/bin/black dundie tests integration