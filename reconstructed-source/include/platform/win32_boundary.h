// ==========================================================================
// ALICE GREENFINGERS - WIN32 PLATFORM BOUNDARY
// Entry Point RVA: 0x004165C1
// ==========================================================================

#pragma once
#ifndef WIN32_BOUNDARY_H
#define WIN32_BOUNDARY_H

#include "platform/platform_types.h"

#ifdef __cplusplus
extern "C" {
#endif

int Platform_Initialize(void);
int Platform_ProcessMessages(void);
void Platform_Shutdown(void);

#ifdef __cplusplus
}
#endif

#endif // WIN32_BOUNDARY_H
