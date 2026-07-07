"""Small Phase 1 checks for secret-like structured examples."""

from __future__ import annotations

from typing import Any


SECRET_KEYS = {
    "access_key",
    "api_key",
    "auth_token",
    "client_secret",
    "connection_string",
    "password",
    "passwd",
    "private_key",
    "refresh_token",
    "secret",
    "token",
}

POLICY_KEYS = {
    "redact_generated_derivatives",
    "secrets_allowed",
}


def find_secret_like_values(data: Any, path: str = "") -> list[str]:
    """Find obvious secret-like keys or private key blocks without echoing values."""

    findings: list[str] = []
    if isinstance(data, dict):
        for key, value in data.items():
            key_text = str(key)
            key_path = f"{path}.{key_text}" if path else key_text
            normalized = key_text.casefold().replace("-", "_")
            if normalized in SECRET_KEYS and normalized not in POLICY_KEYS:
                findings.append(f"{key_path}: secret-like key is not allowed in Phase 1 examples")
            findings.extend(find_secret_like_values(value, key_path))
    elif isinstance(data, list):
        for index, value in enumerate(data):
            findings.extend(find_secret_like_values(value, f"{path}[{index}]"))
    elif isinstance(data, str) and "-----BEGIN" in data and "PRIVATE KEY-----" in data:
        findings.append(f"{path}: private key block is not allowed in Phase 1 examples")
    return findings
