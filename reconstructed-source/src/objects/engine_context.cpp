// ==========================================================================
// ALICE GREENFINGERS - Class_EngineContext Implementation
// ==========================================================================

#include "objects/engine_context.h"
#include "events/event_dispatcher.h"
#include "engine/game_loop.h"
#include "generated/recovered_globals.h"

// Evidence-backed VTable instance for Class_EngineContext (0x00497000)
const struct RecoveredVTable_00497000 g_VTable_00497000 = {
    (void*)EngineContext_Init,           // +0x00: FUN_0040d590 [VERIFIED]
    (void*)EngineContext_Update,         // +0x04: FUN_004096a0 [VERIFIED]
    (void*)EngineContext_EventCallback,  // +0x08: FUN_00404170 [VERIFIED]
    (void*)EngineContext_Cleanup         // +0x0C: FUN_00401c00 [HIGH-CONFIDENCE]
};

void EngineContext_Init(struct Class_EngineContext* ctx) {
    if (!ctx) return;
    ctx->vtable = &g_VTable_00497000;
    ctx->field_04 = 0;
    ctx->field_08 = nullptr;
    ctx->field_0C = 0;
    ctx->field_10 = nullptr;
    DAT_004974f4 = 0; // Set STATE_STARTUP [VERIFIED]
}

void EngineContext_Update(struct Class_EngineContext* ctx) {
    if (!ctx) return;
    ctx->field_04++;
    DAT_004a7f54 = ctx->field_04; // Frame tick counter [VERIFIED]
}

void EngineContext_EventCallback(struct Class_EngineContext* ctx, int cmd_id, void* param) {
    if (!ctx) return;
    FUN_00404170(cmd_id, param);
}

void EngineContext_Cleanup(struct Class_EngineContext* ctx) {
    if (!ctx) return;
    ctx->field_08 = nullptr;
    ctx->field_10 = nullptr;
}
