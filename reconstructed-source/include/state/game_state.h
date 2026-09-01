// ==========================================================================
// ALICE GREENFINGERS - GAME STATE MACHINE
// Evidence: notes/GAME_STATE_ARCHITECTURE.md & GAME_STATE_MACHINE.md
// ==========================================================================

#pragma once
#ifndef GAME_STATE_H
#define GAME_STATE_H

#include "generated/recovered_types.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef enum RecoveredGameState {
    STATE_STARTUP       = 0, // FUN_0040d590 -> DAT_004974f4 = 0 [VERIFIED]
    STATE_MAIN_MENU     = 1, // FUN_00404170 -> DAT_004974f4 = 1 [VERIFIED]
    STATE_NAME_DIALOG   = 2, // FUN_00404170 -> DAT_004974f4 = 2 [VERIFIED]
    STATE_GAMEPLAY      = 3, // FUN_004096a0 -> DAT_004a7f54 = 1 [VERIFIED]
    STATE_PAUSE_OPTIONS = 4, // FUN_00404170 -> DAT_004974f4 = 4 [VERIFIED]
    STATE_SHOP_MARKET   = 5  // FUN_00404170 -> DAT_004974f4 = 5 [RUNTIME-OBSERVED]
} RecoveredGameState;

RecoveredGameState State_GetCurrentState(void);
void State_SetState(RecoveredGameState newState, const char* transitionSource);
bool State_IsValidTransition(RecoveredGameState from, RecoveredGameState to);

#ifdef __cplusplus
}
#endif

#endif // GAME_STATE_H
