// ==========================================================================
// ALICE GREENFINGERS - UNRESOLVED CALL REGISTRY IMPLEMENTATION
// ==========================================================================

#include "unresolved/unresolved_calls.h"

static uint32_t g_UnresolvedInvocations = 0;
static const uint32_t g_TotalUnresolvedCount = 425;

void Unresolved_InitRegistry(void) {
    g_UnresolvedInvocations = 0;
}

void Unresolved_RecordCall(uint32_t call_site, uint32_t caller, const char* cluster, const char* desc, const char* strat) {
    (void)call_site;
    (void)caller;
    (void)cluster;
    (void)desc;
    (void)strat;
    g_UnresolvedInvocations++;
}

uint32_t Unresolved_GetTotalInvocations(void) {
    return g_UnresolvedInvocations;
}

uint32_t Unresolved_GetUnresolvedCount(void) {
    return g_TotalUnresolvedCount;
}
