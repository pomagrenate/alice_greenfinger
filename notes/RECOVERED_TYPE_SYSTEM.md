# ALICE GREENFINGERS - RECOVERED TYPE SYSTEM (STEP 14)

*Generated on 2026-09-01 13:47:59*

## CONSERVATIVE TYPE DICTIONARY

```cpp
typedef unsigned int uint32_t;
typedef unsigned short uint16_t;
typedef unsigned char uint8_t;

enum GameState {
    STATE_STARTUP = 0,
    STATE_MAIN_MENU = 1,
    STATE_NAME_DIALOG = 2,
    STATE_GAMEPLAY = 3,
    STATE_PAUSE_OPTIONS = 4
};

typedef void (__stdcall *EventCallbackFunc)(int cmd_id, void* ctx);
```
