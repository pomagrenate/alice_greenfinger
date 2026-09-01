// ==========================================================================
// ALICE GREENFINGERS FORENSIC RECONSTRUCTION - RECOVERED TYPE SYSTEM
// Generated based on notes/RECOVERED_TYPE_SYSTEM.md & OBJECT_MODEL_BLUEPRINT.md
// ==========================================================================

#pragma once
#ifndef RECOVERED_TYPES_H
#define RECOVERED_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

// Level 1 Primitive Types
typedef uint32_t   uint;
typedef uint8_t    byte;
typedef uint8_t    undefined;
typedef uint16_t   undefined2;
typedef uint32_t   undefined4;
typedef uint64_t   undefined8;
typedef uint32_t   ulong;
typedef uint16_t   ushort;

// Forward Declarations
struct Class_EngineContext;
struct RecoveredVTable_00497000;

// Function Pointer Types
typedef void (*EventCallbackFunc)(int cmd_id, void* ctx);
typedef void (*FrameUpdateFunc)(void* engine_ctx);
typedef void (*InitFunc)(void* engine_ctx);
typedef void (*CleanupFunc)(void* engine_ctx);

#ifdef __cplusplus
}
#endif

#endif // RECOVERED_TYPES_H
