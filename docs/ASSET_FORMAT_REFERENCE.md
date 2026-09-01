# Alice Greenfingers - PopCap LBTC Asset Format Reference

## 1. Binary Container Header Structure
```c
#pragma pack(push, 1)
struct PopCap_LBTC_Header {
    char     magic[4];       // "LBTC" (0x4354424C)
    uint32_t version;        // Format version integer (1)
    uint32_t entry_count;    // Total sub-sprite entries in container
    uint32_t data_offset;    // Byte offset to image payload
};

struct PopCap_Sprite_Entry {
    uint16_t src_x;          // Source X coordinate in atlas bitmap
    uint16_t src_y;          // Source Y coordinate in atlas bitmap
    uint16_t width;          // Pixel width of sub-sprite
    uint16_t height;         // Pixel height of sub-sprite
    int16_t  dest_x_offset;  // Rendering alignment X offset
    int16_t  dest_y_offset;  // Rendering alignment Y offset
    uint32_t flags;          // Transparency and format flags
};
#pragma pack(pop)
```
