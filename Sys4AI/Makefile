PYTHON ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)
PRODUCT_ENV = PYTHONPATH=src

.PHONY: install lint test validate-contracts validate-assets build validate clean

install:
	$(PYTHON) -m pip install -e '.[dev]'

lint:
	$(PRODUCT_ENV) $(PYTHON) -m compileall -q src tests setup.py

test:
	$(PRODUCT_ENV) $(PYTHON) -m pytest

validate-contracts:
	$(PRODUCT_ENV) $(PYTHON) -m sys4ai contracts

validate-assets:
	$(PRODUCT_ENV) $(PYTHON) -m sys4ai assets

build:
	$(PYTHON) -m build

validate: lint validate-contracts validate-assets test build

clean:
	rm -rf build dist .pytest_cache src/*.egg-info
