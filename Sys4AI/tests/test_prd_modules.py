from __future__ import annotations

import os
import shutil
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from typing import Optional

from sys_for_ai.prd_modules import (
    TX19_COMMON_PROVENANCE_RELATIONSHIPS,
    TX19_SOURCE_PRDS,
    _validate_registered_provenance,
    _validate_tx19_module,
    validate_prd_modules,
)

PRODUCT_ROOT = Path(__file__).resolve().parents[1]

HEADER = (
    "prd_module_id,path,title,status,subject_layer,authority_scope,owns_requirement_prefixes,"
    "references_source_prds,supersedes,source_authority_status,owner_role,validation_status,"
    "source_hash,last_validated_at,notes\n"
)


class PrdModuleTests(unittest.TestCase):
    def test_current_prd_module_registry_passes(self) -> None:
        result = validate_prd_modules("registries/prd_module_registry.csv")

        self.assertTrue(result.ok, result.messages)

    def test_planned_modules_may_reference_future_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            registry = _write_fixture(Path(temp_dir), status="planned", validation_status="planned")

            with _working_directory(registry.parents[1]):
                result = validate_prd_modules("registries/prd_module_registry.csv")

            self.assertTrue(result.ok, result.messages)

    def test_duplicate_canonical_requirement_ownership_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            registry = _write_fixture(
                Path(temp_dir),
                status="canonical",
                validation_status="validated",
                source_authority_status="canonical",
                duplicate_canonical=True,
            )

            with _working_directory(registry.parents[1]):
                result = validate_prd_modules("registries/prd_module_registry.csv")

            self.assertFalse(result.ok)
            self.assertTrue(
                any("multiple canonical owners" in message for message in result.messages),
                result.messages,
            )

    def test_draft_cannot_claim_canonical_authority(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            registry = _write_fixture(
                Path(temp_dir),
                status="draft",
                validation_status="pending",
                source_authority_status="canonical",
                write_module=True,
            )

            with _working_directory(registry.parents[1]):
                result = validate_prd_modules("registries/prd_module_registry.csv")

            self.assertFalse(result.ok)
            self.assertTrue(
                any("draft module cannot claim canonical authority" in message for message in result.messages),
                result.messages,
            )

    def test_orphan_active_requirement_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            registry = _write_fixture(
                Path(temp_dir),
                status="draft",
                validation_status="pending",
                write_module=True,
                orphan_requirement=True,
            )

            with _working_directory(registry.parents[1]):
                result = validate_prd_modules("registries/prd_module_registry.csv")

            self.assertFalse(result.ok)
            self.assertTrue(
                any("orphan active requirement prefix: SFA-CORE-TWO" in message for message in result.messages),
                result.messages,
            )

    def test_duplicate_draft_intended_ownership_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            registry = _write_fixture(
                Path(temp_dir),
                status="draft",
                validation_status="pending",
                duplicate_intended=True,
            )

            with _working_directory(registry.parents[1]):
                result = validate_prd_modules("registries/prd_module_registry.csv")

            self.assertFalse(result.ok)
            self.assertTrue(
                any("multiple intended owners" in message for message in result.messages),
                result.messages,
            )

    def test_validated_module_requires_current_source_hash(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            registry = _write_fixture(
                Path(temp_dir),
                status="draft",
                validation_status="validated",
                write_module=True,
            )

            with _working_directory(registry.parents[1]):
                result = validate_prd_modules("registries/prd_module_registry.csv")

            self.assertFalse(result.ok)
            self.assertTrue(
                any("validated module cannot retain a pending source_hash" in message for message in result.messages),
                result.messages,
            )

    def test_retired_agentjob_phrase_fails_tx19_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            module = Path(temp_dir) / "legacy.md"
            module.write_text(
                "TX-19-MODULES DDR-SFADEV-STRATEGIC-BASELINE-G08-001 historical compatibility "
                "ExecutionTransaction resume operation retired\n\n"
                "Define bounded AgentJob execution.\n",
                encoding="utf-8",
            )
            row = {
                "prd_module_id": "PRD-MOD-AGENTJOB-CONTINUE",
                "status": "draft",
                "source_authority_status": "derivative_draft",
                "validation_status": "validated",
            }

            messages = _validate_tx19_module(
                module,
                row,
                "fixture",
                sorted(TX19_SOURCE_PRDS),
            )

            self.assertTrue(any("retired execution phrase remains active" in message for message in messages), messages)

    def test_missing_tx19_plan_provenance_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            registry_root, row = _write_provenance_fixture(
                Path(temp_dir),
                module_id="PRD-MOD-INIT-DISCOVERY",
                omitted_relationship=("traces_to", "SRC-STRATEGIC-BASELINE-MIGRATION-PLAN"),
            )

            messages = _validate_registered_provenance(registry_root, row, "fixture")

            self.assertTrue(
                any(
                    "traces_to -> SRC-STRATEGIC-BASELINE-MIGRATION-PLAN" in message
                    for message in messages
                ),
                messages,
            )

    def test_missing_module_specific_g02_provenance_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            registry_root, row = _write_provenance_fixture(
                Path(temp_dir),
                module_id="PRD-MOD-SYSTEM-LAYERS-SELF-HOSTING",
            )

            messages = _validate_registered_provenance(registry_root, row, "fixture")

            self.assertTrue(
                any("supported_by -> SRC-DDR-STRATEGIC-BASELINE-001" in message for message in messages),
                messages,
            )


def _write_fixture(
    temp_root: Path,
    *,
    status: str,
    validation_status: str,
    source_authority_status: str = "derivative_draft",
    duplicate_canonical: bool = False,
    duplicate_intended: bool = False,
    write_module: bool = False,
    orphan_requirement: bool = False,
) -> Path:
    product = temp_root / "Sys4AI"
    registries = product / "registries"
    registries.mkdir(parents=True)
    (product / "schemas/contracts").mkdir(parents=True)
    shutil.copyfile(
        PRODUCT_ROOT / "schemas/contracts/prd_module_registry_row.schema.json",
        product / "schemas/contracts/prd_module_registry_row.schema.json",
    )
    prds = temp_root / "PRDs"
    prds.mkdir()
    source_prd = prds / "source.md"
    source_prd.write_text("# Source\n", encoding="utf-8")

    (registries / "system_layer_registry.csv").write_text(
        "layer_id,layer_name,layer_type,canonical_roots,mutable_roots,derivative_roots,authority_notes,requires_director_decision_for_mutation,default_validators,owner,source_hash,last_validated_at,notes\n"
        "framework_product,Framework product,framework,PRDs,PRDs/modules,,fixture,false,,test,pending,pending,fixture\n",
        encoding="utf-8",
    )
    (registries / "role_registry.csv").write_text(
        "role_id,role_name,role_class,system_layer_scope,primary_mission,required_skills,optional_skills,forbidden_skills,primary_outputs,allowed_artifact_classes,may_create_execution_transactions,requires_director_decision,authority_status,owner,supersedes,source_hash,last_validated_at,notes\n"
        "requirements_manager,Requirements Manager,governance,framework_product,fixture,,,,,prd,true,false,controlled,test,,pending,pending,fixture\n",
        encoding="utf-8",
    )
    (registries / "requirement_trace_registry.csv").write_text(
        "trace_id,requirement_id,requirement_lifecycle,applicability_status,phase0_selector,phase0_source,coverage_status,trace_class,semantic_justification,semantic_review_verdict,phase1_selectors,evidence_paths,notes\n"
        "TRACE-PRD-MOD-ONE,SFA-CORE-ONE,active,required,SFA-CORE-ONE,PRD-MOD-ONE,covered,implemented,fixture,sufficient,PRD-MOD-ONE,PRD-MOD-ONE,fixture\n"
        + (
            "TRACE-PRD-MOD-TWO,SFA-CORE-TWO,active,required,SFA-CORE-TWO,PRD-MOD-TWO,covered,implemented,fixture,sufficient,PRD-MOD-TWO,PRD-MOD-TWO,fixture\n"
            if orphan_requirement
            else ""
        ),
        encoding="utf-8",
    )

    module_path = prds / "module.md"
    if write_module or status != "planned":
        _write_module(module_path, "PRD-MOD-ONE", source_authority_status)

    rows = [
        _row("PRD-MOD-ONE", module_path, source_prd, status, source_authority_status, validation_status),
    ]
    if duplicate_canonical or duplicate_intended:
        second_module = prds / "module_two.md"
        _write_module(second_module, "PRD-MOD-TWO", source_authority_status)
        rows.append(_row("PRD-MOD-TWO", second_module, source_prd, status, source_authority_status, validation_status))

    registry = registries / "prd_module_registry.csv"
    registry.write_text(HEADER + "".join(rows), encoding="utf-8")
    return registry


def _row(
    module_id: str,
    module_path: Path,
    source_prd: Path,
    status: str,
    source_authority_status: str,
    validation_status: str,
) -> str:
    module_registry_path = f"PRDs/{module_path.name}"
    source_registry_path = f"PRDs/{source_prd.name}"
    return (
        f"{module_id},{module_registry_path},Fixture Module,{status},framework_product,fixture_scope,"
        f"SFA-CORE-ONE,{source_registry_path},,{source_authority_status},requirements_manager,"
        f"{validation_status},pending,2026-07-08T22:26:00Z,fixture\n"
    )


def _write_module(path: Path, module_id: str, source_authority_status: str) -> None:
    path.write_text(
        "# Module\n\n"
        f"**PRD module ID:** {module_id}\n"
        "> Authority notice: fixture.\n\n"
        "**Source PRDs:** PRDs/source.md\n"
        "**Owns requirement prefixes:** SFA-CORE-ONE\n"
        "**Subject layer:** framework_product\n"
        f"**Source authority status:** {source_authority_status}\n",
        encoding="utf-8",
    )


def _write_provenance_fixture(
    temp_root: Path,
    *,
    module_id: str,
    omitted_relationship: Optional[tuple[str, str]] = None,
) -> tuple[Path, dict[str, str]]:
    registry_root = temp_root / "registries"
    registry_root.mkdir()
    module_path = "PRDs/modules/fixture.md"
    source_id = "SRC-PRD-MODULE-FIXTURE"
    (registry_root / "source_registry.csv").write_text(
        "source_id,path,authority_status\n"
        f"{source_id},{module_path},derivative_draft\n",
        encoding="utf-8",
    )
    relationships = sorted(TX19_COMMON_PROVENANCE_RELATIONSHIPS - {omitted_relationship})
    (registry_root / "object_relationship_registry.csv").write_text(
        "subject_id,predicate,object_id\n"
        + "".join(
            f"{source_id},{predicate},{object_id}\n" for predicate, object_id in relationships
        ),
        encoding="utf-8",
    )
    return registry_root, {"prd_module_id": module_id, "path": module_path}


@contextmanager
def _working_directory(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


if __name__ == "__main__":
    unittest.main()
