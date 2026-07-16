PYTHON ?= $(if $(wildcard Sys4AI/.venv/bin/python),Sys4AI/.venv/bin/python,python3)
PRODUCT_PYTHON ?= $(if $(wildcard Sys4AI/.venv/bin/python),$(CURDIR)/Sys4AI/.venv/bin/python,$(PYTHON))

.PHONY: install-development generate-host-bindings validate-development validate-product validate-integration validate

install-development:
	$(PYTHON) -m pip install -e 'development[dev]'

generate-host-bindings:
	$(PYTHON) development/tools/generate_host_bindings.py --root .

validate-development:
	PYTHONPATH=development $(PYTHON) -m sfadev.cli validate
	PYTHONPATH=development $(PYTHON) -m pytest -q development/tests

validate-product:
	$(MAKE) -C Sys4AI validate PYTHON="$(PRODUCT_PYTHON)"

validate-integration:
	PYTHONPATH=Sys4AI/src $(PRODUCT_PYTHON) -m pytest -q integration/tests

validate: validate-development validate-product validate-integration
