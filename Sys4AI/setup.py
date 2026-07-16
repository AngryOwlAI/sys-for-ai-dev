"""Package portable contracts and assets beside the installed runtime."""

from pathlib import Path
from shutil import copytree

from setuptools import setup
from setuptools.command.build_py import build_py


class BuildPyWithResources(build_py):
    """Copy canonical non-code product sources into the wheel."""

    def run(self) -> None:
        super().run()
        root = Path(__file__).parent
        destination = Path(self.build_lib) / "sys4ai" / "resources"
        for name in ("assets", "contracts", "examples"):
            copytree(root / name, destination / name, dirs_exist_ok=True)


setup(cmdclass={"build_py": BuildPyWithResources})
