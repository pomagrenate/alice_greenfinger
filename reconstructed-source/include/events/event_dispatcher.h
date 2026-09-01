// ==========================================================================
// ALICE GREENFINGERS - EVENT DISPATCH SYSTEM
// Target: FUN_00404170 (Opcode & UI Event Callback Dispatcher)
// Evidence: notes/FUN_00404170_DEEP_AUDIT.md & EVENT_CALLBACK_DISPATCH.md
// ABI: __thiscall / __cdecl
// Confidence: [VERIFIED]
// ==========================================================================

#pragma once
#ifndef EVENT_DISPATCHER_H
#define EVENT_DISPATCHER_H

#include "generated/recovered_types.h"

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Original RVA: 0x00404170
 * Subsystem:    SUBSYS_EVENT_DISPATCH
 * Role:         Opcode & UI Callback Dispatcher
 */
int FUN_00404170(int opcode_or_msg, void* ctx_param);

// Helper registration wrappers
int Event_DispatchOpcode(const char* opcode_name, void* param_vector);

#ifdef __cplusplus
}
#endif

#endif // EVENT_DISPATCHER_H
