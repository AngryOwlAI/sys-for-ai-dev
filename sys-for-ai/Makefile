PY ?= python3
VENV ?= .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

.PHONY: venv install doctor validate validate-agentjob validate-skills bootstrap-memory clean-local

venv:
	$(PY) -m venv $(VENV)

install: venv
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt

doctor:
	$(PYTHON) -m sys_for_ai.cli doctor

validate-agentjob:
	$(PYTHON) -m sys_for_ai.cli validate-agentjob control_records/examples/phase1_smoke_agentjob.yaml

validate-skills:
	$(PYTHON) -m sys_for_ai.cli validate-skills skills/core_skill_manifest.yaml

bootstrap-memory:
	$(PYTHON) -m sys_for_ai.cli bootstrap-memory registries

validate: doctor validate-agentjob validate-skills bootstrap-memory

clean-local:
	rm -rf .pytest_cache __pycache__ sys_for_ai/__pycache__ .local/receipts
