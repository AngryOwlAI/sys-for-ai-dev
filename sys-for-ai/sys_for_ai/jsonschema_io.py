"""JSON Schema loading and validation helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, exceptions


class JsonSchemaLoadError(RuntimeError):
    """Raised when a JSON Schema file cannot be loaded as a JSON object."""


def load_json(path: str | Path) -> dict[str, Any]:
    """Load a JSON object from *path*."""

    target = Path(path)
    try:
        with target.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (json.JSONDecodeError, OSError) as exc:
        raise JsonSchemaLoadError(f"Cannot load JSON Schema {target}: {exc}") from exc

    if not isinstance(data, dict):
        raise JsonSchemaLoadError(f"{target}: expected JSON object at schema root")
    return data


def check_schema(schema: dict[str, Any]) -> list[str]:
    """Return deterministic schema errors for a Draft 2020-12 schema."""

    try:
        Draft202012Validator.check_schema(schema)
    except exceptions.SchemaError as exc:
        return [exc.message]
    return []


def validate_instance(instance: Any, schema: dict[str, Any]) -> list[str]:
    """Return deterministic validation errors for *instance* against *schema*."""

    validator = Draft202012Validator(schema)
    errors = sorted(
        validator.iter_errors(instance),
        key=lambda error: (list(error.path), list(error.schema_path), error.message),
    )
    return [_format_error(error) for error in errors]


def _format_error(error: exceptions.ValidationError) -> str:
    path = ".".join(str(part) for part in error.path)
    prefix = f"{path}: " if path else ""
    return f"{prefix}{error.message}"
