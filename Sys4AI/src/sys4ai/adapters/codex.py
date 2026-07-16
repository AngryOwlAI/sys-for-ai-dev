"""Reference capability description for a Codex host adapter."""

from __future__ import annotations

from ..domain.models import HostCapability


class CodexHostAdapter:
    """Describe declared host capabilities without granting permissions."""

    def __init__(self, capabilities: tuple[HostCapability, ...] = ()) -> None:
        self._capabilities = capabilities

    def capabilities(self) -> tuple[HostCapability, ...]:
        return self._capabilities

    def capability(self, capability_id: str) -> HostCapability | None:
        return next(
            (
                capability
                for capability in self._capabilities
                if capability.capability_id == capability_id
            ),
            None,
        )
