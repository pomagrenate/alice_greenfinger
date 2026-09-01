// ==========================================================================
// ALICE GREENFINGERS - UNRESOLVED INDIRECT CALL DEPENDENCY REGISTRY
// Evidence: notes/INDIRECT_CALL_CLUSTER_ANALYSIS.md (Clusters A - G)
// Total Unresolved Call Sites: 425
// ==========================================================================

#pragma once
#ifndef UNRESOLVED_CALLS_H
#define UNRESOLVED_CALLS_H

#include "generated/recovered_types.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct UnresolvedCallRecord {
    uint32_t call_site_rva;
    uint32_t caller_rva;
    const char* cluster;
    const char* description;
    const char* resolution_strategy;
    uint32_t invocation_count;
} UnresolvedCallRecord;

void Unresolved_InitRegistry(void);
void Unresolved_RecordCall(uint32_t call_site, uint32_t caller, const char* cluster, const char* desc, const char* strat);
uint32_t Unresolved_GetTotalInvocations(void);
uint32_t Unresolved_GetUnresolvedCount(void);

#ifdef __cplusplus
}
#endif

#endif // UNRESOLVED_CALLS_H
