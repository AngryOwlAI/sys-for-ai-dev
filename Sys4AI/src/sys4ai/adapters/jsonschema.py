"""JSON Schema adapter for product and target contracts."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import jsonschema


class JSONSchemaValidatorAdapter:
    def validate(
        self, instance: Any, schema: Mapping[str, Any]
    ) -> tuple[str, ...]:
        errors = jsonschema.Draft202012Validator(schema).iter_errors(instance)
        return tuple(error.message for error in sorted(errors, key=lambda item: list(item.path)))
