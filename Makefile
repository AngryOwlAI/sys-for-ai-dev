PY ?= python3

.PHONY: validate-dev-skills validate-product-scaffold validate

validate-dev-skills:
	$(PY) scripts/skills/validate_skill_manifest.py --root .

validate-product-scaffold:
	cd sys-for-ai && $(MAKE) validate

validate: validate-dev-skills validate-product-scaffold
