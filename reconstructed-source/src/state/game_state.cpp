// ==========================================================================
// ALICE GREENFINGERS - GAME STATE MACHINE IMPLEMENTATION
// ==========================================================================

#include "state/game_state.h"
#include "generated/recovered_globals.h"

RecoveredGameState State_GetCurrentState(void) {
    return (RecoveredGameState)DAT_004974f4;
}

bool State_IsValidTransition(RecoveredGameState from, RecoveredGameState to) {
    switch (from) {
        case STATE_STARTUP:
            return (to == STATE_MAIN_MENU);
        case STATE_MAIN_MENU:
            return (to == STATE_NAME_DIALOG || to == STATE_GAMEPLAY || to == STATE_PAUSE_OPTIONS);
        case STATE_NAME_DIALOG:
            return (to == STATE_MAIN_MENU || to == STATE_GAMEPLAY);
        case STATE_GAMEPLAY:
            return (to == STATE_PAUSE_OPTIONS || to == STATE_MAIN_MENU || to == STATE_SHOP_MARKET);
        case STATE_PAUSE_OPTIONS:
            return (to == STATE_GAMEPLAY || to == STATE_MAIN_MENU);
        case STATE_SHOP_MARKET:
            return (to == STATE_GAMEPLAY || to == STATE_MAIN_MENU);
        default:
            return false;
    }
}

void State_SetState(RecoveredGameState newState, const char* transitionSource) {
    (void)transitionSource;
    DAT_004974f4 = (uint32_t)newState;
}
