# ALICE GREENFINGERS - RESOURCE DECODER DECOMPILATION (STEP 10)

*Generated on 2026-09-01*

## 1. Recovered PopCap LBTC Container Format
```c
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
```
