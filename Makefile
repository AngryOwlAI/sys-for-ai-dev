PY ?= python3

.PHONY: validate-rename validate-dev-skills validate-product-scaffold validate

validate-rename:
	$(PY) scripts/validate_rename.py

validate-dev-skills:
	$(PY) scripts/skills/validate_skill_manifest.py --root .

validate-product-scaffold:
	cd Sys4AI && $(MAKE) validate

validate: validate-rename validate-dev-skills validate-product-scaffold
