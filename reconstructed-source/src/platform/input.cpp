// ==========================================================================
// ALICE GREENFINGERS - INPUT EVENT QUEUE IMPLEMENTATION
// ==========================================================================

#include <string.h>
#include "platform/input.h"

#define MAX_INPUT_QUEUE 64

static InputEvent s_event_queue[MAX_INPUT_QUEUE];
static int s_queue_head = 0;
static int s_queue_tail = 0;
static MouseState s_mouse_state = {0, 0, false, false};
static KeyboardState s_keyboard_state = {{false}};

void Input_Initialize(void) {
    s_queue_head = 0;
    s_queue_tail = 0;
    memset(&s_mouse_state, 0, sizeof(MouseState));
    memset(&s_keyboard_state, 0, sizeof(KeyboardState));
}

void Input_PushEvent(const InputEvent* event) {
    if (!event) return;

    if (event->type == INPUT_MOUSE_MOVE) {
        s_mouse_state.x = event->mouse_x;
        s_mouse_state.y = event->mouse_y;
    } else if (event->type == INPUT_MOUSE_DOWN) {
        s_mouse_state.x = event->mouse_x;
        s_mouse_state.y = event->mouse_y;
        if (event->mouse_button == 1) s_mouse_state.left_down = true;
        if (event->mouse_button == 2) s_mouse_state.right_down = true;
    } else if (event->type == INPUT_MOUSE_UP) {
        s_mouse_state.x = event->mouse_x;
        s_mouse_state.y = event->mouse_y;
        if (event->mouse_button == 1) s_mouse_state.left_down = false;
        if (event->mouse_button == 2) s_mouse_state.right_down = false;
    } else if (event->type == INPUT_KEY_DOWN) {
        if (event->key_code >= 0 && event->key_code < 256) {
            s_keyboard_state.keys[event->key_code] = true;
        }
    } else if (event->type == INPUT_KEY_UP) {
        if (event->key_code >= 0 && event->key_code < 256) {
            s_keyboard_state.keys[event->key_code] = false;
        }
    }

    int next_tail = (s_queue_tail + 1) % MAX_INPUT_QUEUE;
    if (next_tail != s_queue_head) {
        s_event_queue[s_queue_tail] = *event;
        s_queue_tail = next_tail;
    }
}

bool Input_PollEvent(InputEvent* out_event) {
    if (!out_event || s_queue_head == s_queue_tail) return false;
    *out_event = s_event_queue[s_queue_head];
    s_queue_head = (s_queue_head + 1) % MAX_INPUT_QUEUE;
    return true;
}

const MouseState* Input_GetMouseState(void) {
    return &s_mouse_state;
}

const KeyboardState* Input_GetKeyboardState(void) {
    return &s_keyboard_state;
}
