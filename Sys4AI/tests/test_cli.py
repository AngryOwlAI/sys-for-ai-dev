from __future__ import annotations

from pathlib import Path

from sys4ai.cli import main


def test_doctor_reports_product_identity(capsys) -> None:
    assert main(["doctor", "--json"]) == 0
    output = capsys.readouterr().out
    assert '"package": "sys4ai"' in output


def test_cli_generates_and_validates_target(tmp_path: Path) -> None:
    target = tmp_path / "sample"
    assert (
        main(
            [
                "generate",
                str(target),
                "--system-id",
                "sample",
                "--name",
                "Sample",
                "--intent",
                "Exercise the product CLI",
            ]
        )
        == 0
    )
    assert main(["validate", str(target)]) == 0
