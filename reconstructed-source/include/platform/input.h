// ==========================================================================
// ALICE GREENFINGERS - INPUT EVENT ABSTRACTION
// ==========================================================================

#pragma once
#ifndef PLATFORM_INPUT_H
#define PLATFORM_INPUT_H

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef enum InputEventType {
    INPUT_NONE          = 0,
    INPUT_MOUSE_MOVE    = 1,
    INPUT_MOUSE_DOWN    = 2,
    INPUT_MOUSE_UP      = 3,
    INPUT_KEY_DOWN      = 4,
    INPUT_KEY_UP        = 5,
    INPUT_QUIT          = 6
} InputEventType;

typedef struct InputEvent {
    InputEventType type;
    int mouse_x;
    int mouse_y;
    int mouse_button;   // 1 = Left, 2 = Right, 3 = Middle
    int key_code;       // Virtual key code / ASCII
} InputEvent;

typedef struct MouseState {
    int x;
    int y;
    bool left_down;
    bool right_down;
} MouseState;

typedef struct KeyboardState {
    bool keys[256];
} KeyboardState;

void Input_Initialize(void);
void Input_PushEvent(const InputEvent* event);
bool Input_PollEvent(InputEvent* out_event);
const MouseState* Input_GetMouseState(void);
const KeyboardState* Input_GetKeyboardState(void);

#ifdef __cplusplus
}
#endif

#endif // PLATFORM_INPUT_H
