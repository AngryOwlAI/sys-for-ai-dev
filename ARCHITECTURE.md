# Architecture orientation

The current architecture is divided across focused controlled documents:

- [`SYSTEM_MAP.md`](SYSTEM_MAP.md) — end-to-end levels, planes, and dependency direction
- [`architecture/system-context.md`](architecture/system-context.md) — actors and external context
- [`architecture/product-architecture.md`](architecture/product-architecture.md) — portable product structure
- [`architecture/development-system-architecture.md`](architecture/development-system-architecture.md) — bootstrap development system
- [`architecture/authority-and-state-model.md`](architecture/authority-and-state-model.md) — authority, state, and evidence dimensions
- [`architecture/self-hosting-model.md`](architecture/self-hosting-model.md) — trusted-release and candidate protocol
- [`architecture/target-system-model.md`](architecture/target-system-model.md) — generated targets
- [`architecture/host-adapter-model.md`](architecture/host-adapter-model.md) — host-neutral ports and adapters

The governing edge is `development -> product -> generated target`. Reverse
authority promotion is prohibited. This page is a navigation surface and does
not supersede the listed controlled sources.
