.PHONY: install virtualenv ipython clean test watch testcicd lint fmt build publish-test publish mypy


install:
	@echo "Installing  for dev environment"
	@.venv/bin/python -m pip install -e '.[test,dev]'

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
	@.venv/bin/pytest -s --forked

testcicd:		   ## Run tests for CI.
	@pytest -v --forked --junitxml=test-result.xml


watch:            ## Run tests on file changes.
	@ls **/*.py | entr pytest  --forked

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/isort dundie tests integration
	@.venv/bin/black dundie tests integration


build:            ## Build package.
	@.venv/bin/python setup.py sdist bdist_wheel

publish-test:          ## Publish package.
	@twine upload --repository testpypi dist/*

publish:          ## Publish package.
	@twine upload dist/*

mypy:
	@.venv/bin/mypy dundie tests integration
