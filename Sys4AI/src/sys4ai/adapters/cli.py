"""Reference capability declaration for a local CLI host."""

from __future__ import annotations

from ..domain.models import HostCapability


class CLIHostAdapter:
    """Expose observed capabilities without treating them as authorization."""

    def __init__(self, capabilities: tuple[HostCapability, ...] = ()) -> None:
        self._capabilities = capabilities

    def capabilities(self) -> tuple[HostCapability, ...]:
        return self._capabilities

    def capability(self, capability_id: str) -> HostCapability | None:
        return next(
            (item for item in self._capabilities if item.capability_id == capability_id),
            None,
        )
