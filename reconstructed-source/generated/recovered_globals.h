// ==========================================================================
// ALICE GREENFINGERS FORENSIC RECONSTRUCTION - RECOVERED GLOBAL STATE
// Evidence: notes/RECOVERED_GLOBALS.md & GLOBAL_STATE_ARCHITECTURE.md
// Total Static Globals Cataloged: 175
// ==========================================================================

#pragma once
#ifndef RECOVERED_GLOBALS_H
#define RECOVERED_GLOBALS_H

#include "generated/recovered_types.h"

#ifdef __cplusplus
extern "C" {
#endif

// Address: DAT_004974f4 | Subsystem: SUBSYS_EVENT_DISPATCH | Frequency: 120 reads/writes | Role: Active Game State Enum (0..4) [VERIFIED]
extern uint32_t DAT_004974f4;

// Address: DAT_004a7f54 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 115 reads/writes | Role: Frame Tick Counter [VERIFIED]
extern uint32_t DAT_004a7f54;

// Address: DAT_00497528 | Subsystem: SUBSYS_POP_PARSER | Frequency: 18 reads/writes | Role: Sprite Atlas Handle Pointer [VERIFIED]
extern uint32_t DAT_00497528;

// Address: DAT_004b1200 | Subsystem: SUBSYS_AUDIO_FMOD | Frequency: 12 reads/writes | Role: FMOD Channel Status Word [VERIFIED]
extern uint32_t DAT_004b1200;

// Address: DAT_004a86a4 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 120 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a86a4;

// Address: DAT_004a95f0 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 103 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a95f0;

// Address: DAT_004a8690 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 76 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8690;

// Address: DAT_004a9620 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 65 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a9620;

// Address: DAT_004a869c | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 49 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a869c;

// Address: DAT_00490d40 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 47 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490d40;

// Address: DAT_004a7f38 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 40 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f38;

// Address: DAT_004a7f34 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 35 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f34;

// Address: DAT_0048cd18 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 30 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0048cd18;

// Address: DAT_004a90f8 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 28 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a90f8;

// Address: DAT_00487ad0 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 28 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00487ad0;

// Address: DAT_004a95e4 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 27 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a95e4;

// Address: DAT_004a95c4 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 27 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a95c4;

// Address: DAT_00497518 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 26 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00497518;

// Address: DAT_004a7f1c | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 25 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f1c;

// Address: DAT_004861d0 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 24 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004861d0;

// Address: DAT_004a8638 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 23 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8638;

// Address: DAT_004a95dc | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 22 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a95dc;

// Address: DAT_004a7f3d | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 22 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f3d;

// Address: DAT_004a9610 | Subsystem: SUBSYS_FRAME_RENDER | Frequency: 21 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a9610;

// Address: DAT_004a7f24 | Subsystem: SUBSYS_CORE_STATE | Frequency: 20 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f24;

// Address: DAT_004a86b4 | Subsystem: SUBSYS_CORE_STATE | Frequency: 20 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a86b4;

// Address: DAT_004974ec | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 19 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004974ec;

// Address: DAT_004a95e0 | Subsystem: SUBSYS_CORE_STATE | Frequency: 19 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a95e0;

// Address: DAT_004a95f8 | Subsystem: SUBSYS_CORE_STATE | Frequency: 19 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a95f8;

// Address: DAT_00497520 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 18 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00497520;

// Address: DAT_004a9730 | Subsystem: SUBSYS_CORE_STATE | Frequency: 17 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a9730;

// Address: DAT_00496660 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 17 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496660;

// Address: DAT_004a912c | Subsystem: SUBSYS_CORE_STATE | Frequency: 16 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a912c;

// Address: DAT_004a8694 | Subsystem: SUBSYS_CORE_STATE | Frequency: 16 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8694;

// Address: DAT_004a7f04 | Subsystem: SUBSYS_CORE_STATE | Frequency: 14 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f04;

// Address: DAT_004a8178 | Subsystem: SUBSYS_CORE_STATE | Frequency: 14 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8178;

// Address: DAT_004a95fc | Subsystem: SUBSYS_CORE_STATE | Frequency: 13 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a95fc;

// Address: DAT_00490a58 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 13 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490a58;

// Address: DAT_004974ea | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 12 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004974ea;

// Address: DAT_004974e6 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 12 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004974e6;

// Address: DAT_004a8630 | Subsystem: SUBSYS_CORE_STATE | Frequency: 12 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8630;

// Address: DAT_004a95f4 | Subsystem: SUBSYS_CORE_STATE | Frequency: 12 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a95f4;

// Address: DAT_004a8644 | Subsystem: SUBSYS_CORE_STATE | Frequency: 12 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8644;

// Address: DAT_00490a54 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 12 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490a54;

// Address: DAT_004a9538 | Subsystem: SUBSYS_CORE_STATE | Frequency: 11 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a9538;

// Address: DAT_004a7f0c | Subsystem: SUBSYS_CORE_STATE | Frequency: 11 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f0c;

// Address: DAT_004a8668 | Subsystem: SUBSYS_CORE_STATE | Frequency: 11 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8668;

// Address: DAT_004a8270 | Subsystem: SUBSYS_CORE_STATE | Frequency: 11 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8270;

// Address: DAT_004974fc | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 11 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004974fc;

// Address: DAT_00496668 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 11 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496668;

// Address: DAT_004974e3 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 10 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004974e3;

// Address: DAT_004a8650 | Subsystem: SUBSYS_CORE_STATE | Frequency: 10 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8650;

// Address: DAT_00484ea8 | Subsystem: SUBSYS_CORE_STATE | Frequency: 10 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00484ea8;

// Address: DAT_00497510 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 10 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00497510;

// Address: DAT_00490d50 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 10 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490d50;

// Address: DAT_00496f30 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 10 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496f30;

// Address: DAT_00490fe0 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 10 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490fe0;

// Address: DAT_00490fe4 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 10 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490fe4;

// Address: DAT_004a86ec | Subsystem: SUBSYS_CORE_STATE | Frequency: 10 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a86ec;

// Address: DAT_004a7538 | Subsystem: SUBSYS_CORE_STATE | Frequency: 10 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7538;

// Address: DAT_0048ae3c | Subsystem: SUBSYS_CORE_STATE | Frequency: 10 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0048ae3c;

// Address: DAT_004a8710 | Subsystem: SUBSYS_CORE_STATE | Frequency: 9 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8710;

// Address: DAT_004a8624 | Subsystem: SUBSYS_CORE_STATE | Frequency: 9 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8624;

// Address: DAT_004a954c | Subsystem: SUBSYS_CORE_STATE | Frequency: 9 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a954c;

// Address: DAT_004a8728 | Subsystem: SUBSYS_CORE_STATE | Frequency: 9 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8728;

// Address: DAT_004a9604 | Subsystem: SUBSYS_CORE_STATE | Frequency: 9 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a9604;

// Address: DAT_004a9124 | Subsystem: SUBSYS_CORE_STATE | Frequency: 9 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a9124;

// Address: DAT_00490708 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 9 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490708;

// Address: DAT_00496e6c | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 9 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496e6c;

// Address: DAT_004966c0 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 9 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004966c0;

// Address: DAT_00490bf0 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 9 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490bf0;

// Address: DAT_00491108 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 9 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00491108;

// Address: DAT_00491120 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 9 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00491120;

// Address: DAT_004a95c0 | Subsystem: SUBSYS_CORE_STATE | Frequency: 9 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a95c0;

// Address: DAT_004a7f00 | Subsystem: SUBSYS_CORE_STATE | Frequency: 9 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f00;

// Address: DAT_004a7f6c | Subsystem: SUBSYS_CORE_STATE | Frequency: 8 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f6c;

// Address: DAT_004974e2 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 8 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004974e2;

// Address: DAT_004a8628 | Subsystem: SUBSYS_CORE_STATE | Frequency: 8 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8628;

// Address: DAT_00496698 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 8 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496698;

// Address: DAT_004902e0 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 8 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004902e0;

// Address: DAT_00490d90 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 8 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490d90;

// Address: DAT_004862c0 | Subsystem: SUBSYS_CORE_STATE | Frequency: 8 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004862c0;

// Address: DAT_004a86e4 | Subsystem: SUBSYS_CORE_STATE | Frequency: 8 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a86e4;

// Address: DAT_0049205c | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 8 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0049205c;

// Address: DAT_004a95bc | Subsystem: SUBSYS_CORE_STATE | Frequency: 8 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a95bc;

// Address: DAT_004829a8 | Subsystem: SUBSYS_CORE_STATE | Frequency: 8 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004829a8;

// Address: DAT_004a826c | Subsystem: SUBSYS_CORE_STATE | Frequency: 7 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a826c;

// Address: DAT_004a90fc | Subsystem: SUBSYS_CORE_STATE | Frequency: 7 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a90fc;

// Address: DAT_004a863c | Subsystem: SUBSYS_CORE_STATE | Frequency: 7 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a863c;

// Address: DAT_004a87b0 | Subsystem: SUBSYS_CORE_STATE | Frequency: 7 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a87b0;

// Address: DAT_0049751c | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 7 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0049751c;

// Address: DAT_004a8658 | Subsystem: SUBSYS_CORE_STATE | Frequency: 7 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8658;

// Address: DAT_004a8684 | Subsystem: SUBSYS_CORE_STATE | Frequency: 7 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8684;

// Address: DAT_004a86e0 | Subsystem: SUBSYS_CORE_STATE | Frequency: 7 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a86e0;

// Address: DAT_004a88c4 | Subsystem: SUBSYS_CORE_STATE | Frequency: 7 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a88c4;

// Address: DAT_00497500 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 7 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00497500;

// Address: DAT_004966cc | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 7 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004966cc;

// Address: DAT_004966bc | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 7 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004966bc;

// Address: DAT_00490fd4 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 7 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490fd4;

// Address: DAT_0049110c | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 7 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0049110c;

// Address: DAT_00491124 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 7 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00491124;

// Address: DAT_00491480 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 7 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00491480;

// Address: DAT_004a753c | Subsystem: SUBSYS_CORE_STATE | Frequency: 7 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a753c;

// Address: DAT_004974f0 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 6 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004974f0;

// Address: DAT_004974e8 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 6 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004974e8;

// Address: DAT_004a90f0 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a90f0;

// Address: DAT_004a9544 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a9544;

// Address: DAT_004a7f08 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f08;

// Address: DAT_004a9138 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a9138;

// Address: DAT_004a871c | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a871c;

// Address: DAT_004a8634 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8634;

// Address: DAT_004a86b8 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a86b8;

// Address: DAT_004a7f44 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f44;

// Address: DAT_004a7f19 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f19;

// Address: DAT_004a7f1a | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f1a;

// Address: DAT_0049750c | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 6 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0049750c;

// Address: DAT_004a9724 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a9724;

// Address: DAT_00490800 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 6 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490800;

// Address: DAT_00496690 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 6 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496690;

// Address: DAT_0049669c | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 6 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0049669c;

// Address: DAT_004966c4 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 6 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004966c4;

// Address: DAT_004966b8 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 6 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004966b8;

// Address: DAT_00496688 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 6 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496688;

// Address: DAT_004a7540 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7540;

// Address: DAT_80004005 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_80004005;

// Address: DAT_00482a18 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00482a18;

// Address: DAT_0048cd98 | Subsystem: SUBSYS_CORE_STATE | Frequency: 6 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0048cd98;

// Address: DAT_004a7f58 | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f58;

// Address: DAT_0048cd50 | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0048cd50;

// Address: DAT_004a7f3c | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f3c;

// Address: DAT_004902d0 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 5 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004902d0;

// Address: DAT_0048cd70 | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0048cd70;

// Address: DAT_004a8714 | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8714;

// Address: DAT_004a879c | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a879c;

// Address: DAT_004a9608 | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a9608;

// Address: DAT_004a8654 | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8654;

// Address: DAT_004a865c | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a865c;

// Address: DAT_004a86fc | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a86fc;

// Address: DAT_004a9120 | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a9120;

// Address: DAT_004974f8 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 5 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004974f8;

// Address: DAT_00490a48 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 5 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00490a48;

// Address: DAT_00496e68 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 5 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496e68;

// Address: DAT_0048cd28 | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0048cd28;

// Address: DAT_00497150 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 5 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00497150;

// Address: DAT_004a86e8 | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a86e8;

// Address: DAT_00482998 | Subsystem: SUBSYS_CORE_STATE | Frequency: 5 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00482998;

// Address: DAT_00496630 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 5 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496630;

// Address: DAT_00497514 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00497514;

// Address: DAT_004974e9 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004974e9;

// Address: DAT_0048cd60 | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0048cd60;

// Address: DAT_0048cd58 | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0048cd58;

// Address: DAT_004a7f18 | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f18;

// Address: DAT_004921e8 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004921e8;

// Address: DAT_004a7f2c | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f2c;

// Address: DAT_004a88ac | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a88ac;

// Address: DAT_004a88b8 | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a88b8;

// Address: DAT_004a86a8 | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a86a8;

// Address: DAT_004a86b0 | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a86b0;

// Address: DAT_004a8708 | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a8708;

// Address: DAT_004a7f48 | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f48;

// Address: DAT_0048cd40 | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0048cd40;

// Address: DAT_004a7f40 | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a7f40;

// Address: DAT_004a86dc | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004a86dc;

// Address: DAT_00497508 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00497508;

// Address: DAT_00497504 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00497504;

// Address: DAT_004aa74c | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004aa74c;

// Address: DAT_004aa748 | Subsystem: SUBSYS_CORE_STATE | Frequency: 4 reads/writes | Role: State Variable / System Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004aa748;

// Address: DAT_00496684 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496684;

// Address: DAT_00496694 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496694;

// Address: DAT_0049682c | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_0049682c;

// Address: DAT_004902d8 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004902d8;

// Address: DAT_00496840 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496840;

// Address: DAT_00496872 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496872;

// Address: DAT_004910d0 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_004910d0;

// Address: DAT_00496f34 | Subsystem: SUBSYS_SCRIPT_HOST | Frequency: 4 reads/writes | Role: Script Host Context / Buffer Flag [HIGH-CONFIDENCE]
extern uint32_t DAT_00496f34;

#ifdef __cplusplus
}
#endif

#endif // RECOVERED_GLOBALS_H
