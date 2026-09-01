// ==========================================================================
// ALICE GREENFINGERS - Class_EngineContext Layout
// Evidence: notes/OBJECT_MODEL_BLUEPRINT.md & OBJECT_LAYOUT_RECOVERY.md
// Confidence: [VERIFIED / HIGH-CONFIDENCE]
// ==========================================================================

#pragma once
#ifndef ENGINE_CONTEXT_H
#define ENGINE_CONTEXT_H

#include "generated/recovered_types.h"
#include "generated/recovered_vtables.h"

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Object: Class_EngineContext
 * Base Address Register: ECX (__thiscall)
 * Associated VTable: VTABLE_00497000
 */
struct Class_EngineContext {
    const struct RecoveredVTable_00497000* vtable; // +0x00 [VERIFIED]
    uint32_t field_04;                             // +0x04 [HIGH-CONFIDENCE] Frame Update Counter
    void*    field_08;                             // +0x08 [HIGH-CONFIDENCE] Event Listener List Pointer
    uint32_t field_0C;                             // +0x0C [HIGH-CONFIDENCE] Script Host Flags
    void*    field_10;                             // +0x10 [HIGH-CONFIDENCE] Sprite Atlas Handle Pointer
};

void EngineContext_Init(struct Class_EngineContext* ctx);
void EngineContext_Update(struct Class_EngineContext* ctx);
void EngineContext_EventCallback(struct Class_EngineContext* ctx, int cmd_id, void* param);
void EngineContext_Cleanup(struct Class_EngineContext* ctx);

#ifdef __cplusplus
}
#endif

#endif // ENGINE_CONTEXT_H
