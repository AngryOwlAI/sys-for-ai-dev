from __future__ import annotations

from pathlib import Path

from sys4ai.adapters.filesystem import FilesystemWorkspaceAdapter
from sys4ai.assurance.validation import validate_assets, validate_contracts
from sys4ai.memory.catalog import lookup_source, search_sources


def test_product_contracts_and_examples_validate() -> None:
    result = validate_contracts()
    assert result.ok, result.to_dict()
    assert "contracts/schemas/execution-transaction.schema.json" in result.evidence


def test_product_assets_and_catalogs_validate() -> None:
    result = validate_assets()
    assert result.ok, result.to_dict()
    assert "contracts/catalogs/role-types.yaml" in result.evidence


def test_filesystem_adapter_rejects_path_traversal(tmp_path: Path) -> None:
    workspace = FilesystemWorkspaceAdapter(tmp_path / "workspace")
    workspace.ensure_directory("")
    try:
        workspace.write_text("../outside.txt", "unsafe")
    except ValueError as exc:
        assert "escapes workspace" in str(exc)
    else:
        raise AssertionError("path traversal was accepted")


def test_source_first_search_reports_authority(tmp_path: Path) -> None:
    source = tmp_path / "requirements.md"
    source.write_text(
        "---\nartifact_id: REQ-001\nauthority: controlled\n---\n# Requirements\n",
        encoding="utf-8",
    )
    results = search_sources(tmp_path, "Requirements")
    assert results[0]["authority"] == "controlled"
    assert lookup_source(tmp_path, "REQ-001") == {
        "path": "requirements.md",
        "artifact_id": "REQ-001",
        "title": "Requirements",
        "authority": "controlled",
    }
