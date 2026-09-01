// ==========================================================================
// ALICE GREENFINGERS - RESOURCE ARCHIVE LOADER (PHASE 4 DECOMPILED)
// Target: FUN_004033c0 (PopCap GFX Archive Extractor)
// ==========================================================================

#pragma once
#ifndef RESOURCE_LOADER_H
#define RESOURCE_LOADER_H

#include "generated/recovered_types.h"

#ifdef __cplusplus
extern "C" {
#endif

#pragma pack(push, 1)
struct PopCap_LBTC_Header {
    char     magic[4];       // +0x00: "LBTC" (0x4354424C) [VERIFIED]
    uint32_t version;        // +0x04: Format version [VERIFIED]
    uint32_t entry_count;    // +0x08: Sub-sprite entry count [VERIFIED]
    uint32_t data_offset;    // +0x0C: Offset to compressed image payload [VERIFIED]
};

struct PopCap_Sprite_Entry {
    uint16_t src_x;          // +0x00: X coordinate in atlas [VERIFIED]
    uint16_t src_y;          // +0x02: Y coordinate in atlas [VERIFIED]
    uint16_t width;          // +0x04: Sub-image pixel width [VERIFIED]
    uint16_t height;         // +0x06: Sub-image pixel height [VERIFIED]
    int16_t  dest_x_offset;  // +0x08: Render alignment X offset [VERIFIED]
    int16_t  dest_y_offset;  // +0x0A: Render alignment Y offset [VERIFIED]
    uint32_t flags;          // +0x0C: Format & transparency flags [VERIFIED]
};
#pragma pack(pop)

int FUN_004033c0(const char* archive_path, void* dest_buffer, int buffer_size, int flags, void* out_handle, void* reserved);
int Resource_LoadGfxArchive(const char* filepath);
int Resource_ValidateLBTCHeader(const struct PopCap_LBTC_Header* header);

#ifdef __cplusplus
}
#endif

#endif // RESOURCE_LOADER_H
