# ALICE GREENFINGERS - EXECUTION TRACE SCHEMA SPECIFICATION (PHASE 13)

*Generated on 2026-09-01*

## 1. Schema Field Definitions
| Field Name | Type | Description | Mandatory |
| :--- | :--- | :--- | :---: |
| `event_id` | `integer` | Sequence index within the captured execution trace | **YES** |
| `sim_tick` | `integer` | Value of 60 Hz frame counter (`DAT_004a7f54`) | **YES** |
| `event_type` | `string` | Classification (`STATE_TRANSITION`, `OPCODE_DISPATCH`, etc.) | **YES** |
| `state_id` | `integer` | Verified active game state (`0` to `5`) | **YES** |
| `rva` | `string` | Original PE relative virtual address (e.g., `0x00404170`) | *Optional* |
| `function_symbol`| `string` | Recovered symbolic name (e.g., `FUN_00404170`) | *Optional* |
| `opcode_id` | `integer` | Script/event opcode (`1001` Start, `1004` Market, etc.) | *Optional* |
| `global_address` | `string` | Global variable symbol (e.g., `DAT_004a86a4`) | *Optional* |
| `previous_value` | `any` | Value prior to state or memory mutation | *Optional* |
| `new_value` | `any` | Value following state or memory mutation | *Optional* |
| `resource_id` | `string` | Asset container or sprite identifier | *Optional* |
| `evidence_level` | `string` | `E1` (Static), `E2` (Reconstruction), `E3` (Runtime), `E4` (Differential), `E5` (Reproducible Experiment) | **YES** |
