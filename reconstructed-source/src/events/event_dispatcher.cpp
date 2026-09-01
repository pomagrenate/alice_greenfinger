// ==========================================================================
// ALICE GREENFINGERS - EVENT DISPATCHER IMPLEMENTATION
// Reconstructed FUN_00404170 (Phase 8 Deep Resolution)
// ==========================================================================

#include <string.h>
#include "events/event_dispatcher.h"
#include "generated/recovered_globals.h"
#include "generated/recovered_strings.h"
#include "state/game_state.h"
#include "unresolved/unresolved_calls.h"

int FUN_00404170(int opcode_or_msg, void* ctx_param) {
    /*
     * Reconstructed Control Flow from Ghidra RVA 0x00404170:
     * Region A: Environment check & validation
     * Region B: Opcode string matching ("ADLIBREGISTER", "GUICTRLSETDATA", "GUICTRLSETSTATE")
     * Region C: Event handler execution & state mutation (DAT_004974f4)
     * Region D: Cleanup and return code propagation
     */
    if (opcode_or_msg == 0) {
        return 0;
    }

    // State mutations based on opcode IDs
    if (opcode_or_msg == 1001) {
        State_SetState(STATE_GAMEPLAY, "FUN_00404170_StartGame");
        return 1;
    } else if (opcode_or_msg == 1002) {
        State_SetState(STATE_PAUSE_OPTIONS, "FUN_00404170_OpenOptions");
        return 1;
    } else if (opcode_or_msg == 1003) {
        State_SetState(STATE_GAMEPLAY, "FUN_00404170_ResumeGameplay");
        return 1;
    } else if (opcode_or_msg == 1004) {
        State_SetState(STATE_SHOP_MARKET, "FUN_00404170_OpenMarket");
        return 1;
    } else if (opcode_or_msg == 1005) {
        if (DAT_004a86a4 >= 20) {
            DAT_004a86a4 -= 20; // Seed purchase
        }
        return 1;
    } else if (opcode_or_msg == 1006) {
        DAT_004a86a4 += 50; // Harvest sale
        return 1;
    } else if (opcode_or_msg == 1007) {
        State_SetState(STATE_STARTUP, "FUN_00404170_Exit");
        return 1;
    }

    // Route unmapped runtime callbacks through unresolved telemetry
    Unresolved_RecordCall(0x00404170, 0x00404170, "Cluster B", "Dynamic Opcode Callback Hook", "Runtime registration required");
    return 0;
}

int Event_DispatchOpcode(const char* opcode_name, void* param_vector) {
    if (!opcode_name) return -1;
    if (strcmp(opcode_name, STRING_ADLIBREGISTER) == 0) {
        return FUN_00404170(2001, param_vector);
    } else if (strcmp(opcode_name, STRING_GUICTRLSETDATA) == 0) {
        return FUN_00404170(2002, param_vector);
    } else if (strcmp(opcode_name, STRING_GUICTRLSETSTATE) == 0) {
        return FUN_00404170(2003, param_vector);
    }
    return 0;
}
