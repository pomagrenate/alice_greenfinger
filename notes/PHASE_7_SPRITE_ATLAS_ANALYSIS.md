# ALICE GREENFINGERS - SPRITE ATLAS STRUCTURE ANALYSIS (STEP 3)

*Generated on 2026-09-01*

## 1. PopCap LBTC Container Layout
```c
#pragma pack(push, 1)
struct PopCap_LBTC_Header {
    char     magic[4];       // +0x00: "LBTC" (0x4354424C) [E1/E4 Verified]
    uint32_t version;        // +0x04: Version integer (1) [E1/E4 Verified]
    uint32_t entry_count;    // +0x08: Sub-sprite count [E1/E4 Verified]
    uint32_t data_offset;    // +0x0C: Payload offset [E1/E4 Verified]
};

struct PopCap_Sprite_Entry {
    uint16_t src_x;          // +0x00: Atlas source X [E1/E4 Verified]
    uint16_t src_y;          // +0x02: Atlas source Y [E1/E4 Verified]
    uint16_t width;          // +0x04: Pixel width [E1/E4 Verified]
    uint16_t height;         // +0x06: Pixel height [E1/E4 Verified]
    int16_t  dest_x_offset;  // +0x08: Render alignment X offset [E1/E4 Verified]
    int16_t  dest_y_offset;  // +0x0A: Render alignment Y offset [E1/E4 Verified]
    uint32_t flags;          // +0x0C: Format / transparency flags [E1/E4 Verified]
};
#pragma pack(pop)
```
