# ALICE GREENFINGERS - VTABLE DEEP RECOVERY (STEP 4)

*Generated on 2026-09-01 17:56:55*

## 1. RECOVERED VTABLE SLOTS & OBJECT MAPPINGS

### `VTABLE_00497000` — Object Family: EngineContext / GameApplication

| Slot Offset | Target Function RVA | Subsystem Role | Evidence Status |
| :---: | :---: | --- | :---: |
| `+0x00` | `0x00401500` | `EngineContext_Initialize` | **[VERIFIED (E1/E3)]** |
| `+0x04` | `0x004096a0` | `EngineContext_TickAndRender` | **[VERIFIED (E1/E3)]** |
| `+0x08` | `0x00404170` | `EngineContext_DispatchEvent` | **[VERIFIED (E1/E3)]** |
| `+0x0C` | `0x0040d590` | `EngineContext_Shutdown` | **[VERIFIED (E1/E3)]** |

### `VTABLE_00497100` — Object Family: UIWidgetBase

| Slot Offset | Target Function RVA | Subsystem Role | Evidence Status |
| :---: | :---: | --- | :---: |
| `+0x00` | `0x00405210` | `UIWidget_Draw` | **[PROBABLE (E2)]** |
| `+0x04` | `0x00405340` | `UIWidget_HandleClick` | **[PROBABLE (E2)]** |
| `+0x08` | `0x00405480` | `UIWidget_Destroy` | **[PROBABLE (E2)]** |

