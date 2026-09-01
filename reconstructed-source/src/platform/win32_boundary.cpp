// ==========================================================================
// ALICE GREENFINGERS - WIN32 PLATFORM IMPLEMENTATION
// Reconstructed EntryPoint / WinMain Loop
// ==========================================================================

#include "platform/win32_boundary.h"
#include "objects/engine_context.h"
#include "generated/recovered_globals.h"

static struct Class_EngineContext g_EngineContext;

int Platform_Initialize(void) {
    EngineContext_Init(&g_EngineContext);
    return 0;
}

int Platform_ProcessMessages(void) {
    EngineContext_Update(&g_EngineContext);
    return 1;
}

void Platform_Shutdown(void) {
    EngineContext_Cleanup(&g_EngineContext);
}
