# Portable Continue Example

## Scenario

A generated target system has a tracked state file and a handoff directory.

## Generic Steps

1. Inspect `<TARGET_STATE_PATH>`.
2. Inspect the latest `<TARGET_HANDOFF_PATH>`.
3. Run the target memory preflight command.
4. Select one authorized work packet.
5. Execute inside its write boundary.
6. Run declared validators.
7. Write `<NEXT_HANDOFF_PATH>`.

## Expected Result

The operator can resume the target system without relying on chat history.
