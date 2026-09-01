// ==========================================================================
// ALICE GREENFINGERS FORENSIC RECONSTRUCTION - RECOVERED VTABLES
// Evidence: notes/VTABLE_OWNERSHIP_MAP.md & RECOVERED_VTABLES.md
// ==========================================================================

#pragma once
#ifndef RECOVERED_VTABLES_H
#define RECOVERED_VTABLES_H

#include "generated/recovered_types.h"

#ifdef __cplusplus
extern "C" {
#endif

/*
 * VTable: VTABLE_00497000
 * Owning Object: Class_EngineContext
 * Address: 0x00497000
 */
struct RecoveredVTable_00497000 {
    void* slot_00; // +0x00 -> FUN_0040d590 (Init / Constructor) [VERIFIED]
    void* slot_04; // +0x04 -> FUN_004096a0 (Frame Layer Update) [VERIFIED]
    void* slot_08; // +0x08 -> FUN_00404170 (UI Event Callback) [VERIFIED]
    void* slot_0C; // +0x0C -> FUN_00401c00 (Destructor / Cleanup) [HIGH-CONFIDENCE]
};

extern const struct RecoveredVTable_00497000 g_VTable_00497000;

#ifdef __cplusplus
}
#endif

#endif // RECOVERED_VTABLES_H
