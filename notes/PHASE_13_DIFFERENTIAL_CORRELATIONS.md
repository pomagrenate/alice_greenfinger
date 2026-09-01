# ALICE GREENFINGERS - DIFFERENTIAL TRACE CORRELATION REPORT (STEP 16)

*Generated on 2026-09-01*

## 1. Trace Scenario Correlation Matrix (12 Scenarios)
| Scenario Identifier | Scenario Title | Total Events | Match Percentage | Forensic Correlation Verdict |
| :--- | :--- | ---: | ---: | :---: |
| `startup` | Process Startup & LBTC Preload | 3 | 100.0% | **[MATCH (E4)]** |
| `title_menu` | Main Menu & Title Sprites | 3 | 100.0% | **[MATCH (E4)]** |
| `farm_init` | Profile Dialog & Farm Grid Init | 3 | 100.0% | **[MATCH (E4)]** |
| `seed_purchase` | Seed Buy Opcode 1005 Dispatch | 2 | 100.0% | **[MATCH (E4)]** |
| `sowing` | Soil Tile Sowing Event | 2 | 100.0% | **[MATCH (E4)]** |
| `crop_growth` | 5-Stage Crop Growth Timers | 3 | 100.0% | **[MATCH (E4)]** |
| `harvest` | Mature Harvest & Basket Inventory | 3 | 100.0% | **[MATCH (E4)]** |
| `market_entry` | Market Opcode 1004 Dispatch | 3 | 100.0% | **[MATCH (E4)]** |
| `crop_sale` | Crop Sale Opcode 1006 Dispatch | 3 | 100.0% | **[MATCH (E4)]** |
| `day_transition` | Day End Summary & Day Counter ++ | 3 | 100.0% | **[MATCH (E4)]** |
| `save` | AGSV Stream Serialization | 1 | 100.0% | **[MATCH (E4)]** |
| `load` | AGSV Stream Deserialization | 2 | 100.0% | **[MATCH (E4)]** |

**Summary Finding:** 100.0% of observable semantic trace events matched across all 12 tested scenarios (31/31 events identical).
