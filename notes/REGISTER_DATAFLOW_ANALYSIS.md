# ALICE GREENFINGERS - REGISTER-LEVEL DATAFLOW ANALYSIS (STEP 3)

*Generated on 2026-09-01 13:41:00*

## REGISTER USAGE & PROPAGATION PATTERNS

| Register | Primary Usage Pattern | Subsystem Propagation Role | Dataflow Evidence |
| --- | --- | --- | --- |
| `ECX` | `this` Pointer Base Address | Object Instance Base Pointer | Repeated access to `[ECX + 0x00 .. + 0x1a8]` |
| `EAX` | Return Value / Dynamic Call Target | Function Return & Indirect Dispatch | `CALL EAX` instructions after vtable load |
| `ESI` | Array Source Index / Sprite Vector | Loop Iteration Pointer | Blitting loops in `FUN_004096a0` |
| `EDI` | Screen Surface Buffer Pointer | Render Target Surface Pointer | Direct Memory Write loops in Graphics Subsystem |
