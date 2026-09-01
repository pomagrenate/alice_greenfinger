# ALICE GREENFINGERS - OBJECT IDENTITY CORRELATION (STEP 5)

*Generated on 2026-09-01 17:57:09*

## 1. RECOVERED OBJECT FAMILIES & MEMORY LAYOUTS

### `EngineContext` (VTable `0x00497000`)

- **Constructor:** `FUN_00401500` | **Destructor:** `FUN_0040d590` | **Size:** 128 B
- **Evidence:** **[E1/E2/E3]**

| Member Offset | Type | Name | Purpose |
| :---: | :---: | :---: | --- |
| `+0x00` | `void**` | `vptr` | Object layout field |
| `+0x04` | `uint32_t` | `state_id` | Object layout field |
| `+0x08` | `void*` | `resource_mgr` | Object layout field |
| `+0x0C` | `void*` | `audio_sys` | Object layout field |

### `UIWidgetContainer` (VTable `0x00497100`)

- **Constructor:** `FUN_00405100` | **Destructor:** `FUN_00405480` | **Size:** 64 B
- **Evidence:** **[E1/E2]**

| Member Offset | Type | Name | Purpose |
| :---: | :---: | :---: | --- |
| `+0x00` | `void**` | `vptr` | Object layout field |
| `+0x04` | `int` | `control_id` | Object layout field |
| `+0x08` | `RECT` | `bounds` | Object layout field |

