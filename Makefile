.PHONY: install virtualenv ipython

install:
	@echo "Installing  for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@echo "Creating virtualenv"
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@echo "Starting ipython"
	@.venv/bin/ipython



