// ==========================================================================
// ALICE GREENFINGERS - FMOD AUDIO SYSTEM IMPLEMENTATION
// Reconstructed FUN_00411000
// ==========================================================================

#include "audio/fmod_system.h"
#include "generated/recovered_globals.h"

int FUN_00411000(int audio_cmd, void* audio_data) {
    (void)audio_data;
    if (audio_cmd == 1) {
        DAT_004b1200 = 1;
        return 1;
    } else if (audio_cmd == 0) {
        DAT_004b1200 = 0;
        return 1;
    }
    return 0;
}

int Audio_InitFMOD(void) {
    return FUN_00411000(1, nullptr);
}

int Audio_PlaySoundSample(int sample_id, float volume) {
    (void)sample_id;
    (void)volume;
    return 1;
}

int Audio_PlayMusicTrack(int track_id) {
    (void)track_id;
    return 1;
}

void Audio_ShutdownFMOD(void) {
    FUN_00411000(0, nullptr);
}
