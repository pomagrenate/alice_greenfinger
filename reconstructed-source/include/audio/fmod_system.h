// ==========================================================================
// ALICE GREENFINGERS - FMOD AUDIO BOUNDARY
// Target: FUN_00411000
// Evidence: notes/AUDIO_ARCHITECTURE.md
// ==========================================================================

#pragma once
#ifndef FMOD_SYSTEM_H
#define FMOD_SYSTEM_H

#include "generated/recovered_types.h"

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Original RVA: 0x00411000
 * Subsystem:    SUBSYS_AUDIO_FMOD
 * Role:         FMOD Audio Wrapper Host
 */
int FUN_00411000(int audio_cmd, void* audio_data);

int Audio_InitFMOD(void);
int Audio_PlaySoundSample(int sample_id, float volume);
int Audio_PlayMusicTrack(int track_id);
void Audio_ShutdownFMOD(void);

#ifdef __cplusplus
}
#endif

#endif // FMOD_SYSTEM_H
