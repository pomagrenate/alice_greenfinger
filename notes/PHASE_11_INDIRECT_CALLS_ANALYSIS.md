# ALICE GREENFINGERS - PHASE 11 INDIRECT CALLS ANALYSIS (STEP 2)

*Generated on 2026-09-01 18:47:14*

## 1. REACHABILITY & CLUSTER AUDIT OF 124 ISOLATED SITES

| Cluster Category | Total Sites | Campaign Reachability | Forensic Status |
| :--- | ---: | :---: | :--- |
| **Cluster A (VTable Virtual Dispatch)** | 98 | Non-blocking / Secondary UI | **[UNRESOLVED_ISOLATED]** |
| **Cluster C (GUI Control Hooks)** | 18 | Non-blocking / Secondary Dialogs | **[UNRESOLVED_ISOLATED]** |
| **Cluster G (Stack Function Pointers)** | 8 | Non-blocking / Transient Helper | **[UNRESOLVED_ISOLATED]** |

**Finding:** 100% of the 124 remaining isolated indirect calls reside in secondary optional UI dialogs, error popups, and legacy wrappers. None block the core campaign progression pathway.
