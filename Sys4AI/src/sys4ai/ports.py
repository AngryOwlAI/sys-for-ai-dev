"""Ports through which hosts provide capabilities to the core."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from .domain.models import Action, HostCapability


class ModelProvider(Protocol):
    def complete(self, prompt: str) -> str: ...


class HumanApprovalPort(Protocol):
    def request(self, decision: Mapping[str, Any]) -> bool: ...


class WorkspacePort(Protocol):
    @property
    def root(self) -> Path: ...

    def read_text(self, relative: str) -> str: ...

    def write_text(self, relative: str, content: str) -> Path: ...


class FileStorePort(Protocol):
    def read_bytes(self, key: str) -> bytes: ...

    def write_bytes(self, key: str, content: bytes) -> None: ...


class SourceControlPort(Protocol):
    def status(self) -> Mapping[str, Any]: ...

    def diff(self) -> str: ...


class ToolExecutionPort(Protocol):
    def execute(self, action: Action) -> Mapping[str, Any]: ...


class StateStorePort(Protocol):
    def load(self, key: str) -> Mapping[str, Any] | None: ...

    def save(self, key: str, value: Mapping[str, Any]) -> None: ...


class ArtifactCatalogPort(Protocol):
    def lookup(self, query: str) -> Mapping[str, Any] | None: ...

    def search(self, query: str, limit: int = 10) -> Sequence[Mapping[str, Any]]: ...


class EventSinkPort(Protocol):
    def emit(self, event: Mapping[str, Any]) -> None: ...


class ClockPort(Protocol):
    def now_iso(self) -> str: ...


class SecretsPort(Protocol):
    def get(self, name: str) -> str | None: ...


class HostCapabilityPort(Protocol):
    def capabilities(self) -> Sequence[HostCapability]: ...
