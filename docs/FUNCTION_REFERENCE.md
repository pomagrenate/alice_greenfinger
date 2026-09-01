# Alice Greenfingers - Key Recovered Function Reference

| Function Symbol | RVA Address | Subsystem Domain | Verified Role | Evidence Level |
| :--- | :---: | :--- | :--- | :---: |
| `FUN_00401500` | `0x00401500` | Engine Initialization | Engine Context constructor & VTable assignment | **[E1/E3]** |
| `FUN_004033c0` | `0x004033c0` | Resource Loader | PopCap LBTC header parser and atlas builder | **[E1/E4]** |
| `FUN_00404170` | `0x00404170` | Event Dispatcher | Opcode matcher (`1001`..`1007`) & state transitioner | **[E1/E3]** |
| `FUN_004096a0` | `0x004096a0` | Engine Loop | 60 Hz frame render tick & `DAT_004a7f54` increment | **[E1/E3]** |
| `FUN_00411000` | `0x00411000` | Audio Host | FMOD subsystem host wrapper and status flag setter | **[E1/E3]** |
| `FUN_0040d590` | `0x0040d590` | Engine Shutdown | Context destruction and resource cleanup | **[E1/E3]** |
