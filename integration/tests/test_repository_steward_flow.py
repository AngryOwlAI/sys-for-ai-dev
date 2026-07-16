from __future__ import annotations

from pathlib import Path
from shutil import copytree

import yaml

from sys4ai.adapters.read_only_filesystem import ReadOnlyFilesystemHostAdapter
from sys4ai.application.services import ExecutionService, TargetFactory, VerificationService
from sys4ai.domain.models import SystemDefinition
from sys4ai.runtime.workspace import initialize_workspace


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
FIXTURE = REPOSITORY_ROOT / "integration/fixtures/target-systems/repo-steward"


def _definition() -> SystemDefinition:
    return SystemDefinition(
        "repo-steward",
        "Repository Steward",
        "Propose bounded evidence-backed repository maintenance without autonomous publication",
        "agentic-system",
    )


def test_committed_fixture_is_derivative_and_structurally_valid() -> None:
    result = VerificationService().verify(FIXTURE)
    manifest = yaml.safe_load((FIXTURE / "target-system.yaml").read_text(encoding="utf-8"))
    assert result.ok, result.to_dict()
    assert manifest["authority"] == "derivative"
    assert manifest["production_ready"] is False
    assert not (FIXTURE / ".sys4ai").exists()


def test_fixture_executes_only_its_bounded_read_in_ephemeral_state(
    tmp_path: Path,
) -> None:
    target = copytree(FIXTURE, tmp_path / "repo-steward")
    initialize_workspace(target, _definition(), allow_existing=True)
    transaction = yaml.safe_load(
        (target / "contracts/read-only-inspection.example.yaml").read_text(
            encoding="utf-8"
        )
    )
    result = ExecutionService().process(
        target,
        transaction,
        ReadOnlyFilesystemHostAdapter(target),
    )
    run = target / ".sys4ai/runs/fixture-read-001"
    assert result.ok, result.to_dict()
    assert "executed: true" in (run / "result.yaml").read_text(encoding="utf-8")
    assert "content_retained: false" in (
        run / "evidence/action-001.yaml"
    ).read_text(encoding="utf-8")
    assert VerificationService().verify(target).ok


def test_product_generates_a_fresh_equivalent_target(tmp_path: Path) -> None:
    target = TargetFactory().generate(_definition(), tmp_path / "generated")
    result = VerificationService().verify(target)
    assert result.ok, result.to_dict()
    assert (target / "operations/retirement.md").is_file()
    assert (target / ".sys4ai/workspace.yaml").is_file()
