"""Reference host and storage adapters."""

from .cli import CLIHostAdapter
from .filesystem import FilesystemWorkspaceAdapter
from .git import GitWorkspaceAdapter
from .jsonschema import JSONSchemaValidatorAdapter
from .local_state import LocalStateAdapter
from .read_only_filesystem import ReadOnlyFilesystemHostAdapter
from .yaml_artifact import YAMLArtifactAdapter

__all__ = [
    "CLIHostAdapter",
    "FilesystemWorkspaceAdapter",
    "GitWorkspaceAdapter",
    "JSONSchemaValidatorAdapter",
    "LocalStateAdapter",
    "ReadOnlyFilesystemHostAdapter",
    "YAMLArtifactAdapter",
]
