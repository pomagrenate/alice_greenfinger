#!/usr/bin/env python3
"""
Phase 6 - Steps 5 to 8:
- Step 5: Input Abstraction (input.h / input.cpp & notes/PHASE_6_INPUT_MODEL.md)
- Step 6: Event Dispatch Integration (notes/PHASE_6_INPUT_EVENT_PIPELINE.md)
- Step 7: Real-Time Loop (notes/PHASE_6_REALTIME_LOOP.md)
- Step 8: Deterministic Clock Integration (notes/PHASE_6_CLOCK_INTEGRATION.md)
"""

import os
import sys
import json
import datetime

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
NOTES_DIR = os.path.join(PROJECT_ROOT, 'notes')
ANALYSIS_DIR = os.path.join(PROJECT_ROOT, 'analysis')
SOURCE_DIR = os.path.join(PROJECT_ROOT, 'reconstructed-source')

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}")

def run_steps_5_to_8():
    log("=== PHASE 6: RUNNING STEPS 5 TO 8 ===")

    # ---------------------------------------------------------
    # STEP 5: INPUT ABSTRACTION (input.h / input.cpp)
    # ---------------------------------------------------------
    input_h = os.path.join(SOURCE_DIR, 'include', 'platform', 'input.h')
    with open(input_h, 'w', encoding='utf-8') as f:
        f.write('''// ==========================================================================
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
''')

    input_cpp = os.path.join(SOURCE_DIR, 'src', 'platform', 'input.cpp')
    with open(input_cpp, 'w', encoding='utf-8') as f:
        f.write('''// ==========================================================================
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
''')

    with open(os.path.join(NOTES_DIR, 'PHASE_6_INPUT_MODEL.md'), 'w', encoding='utf-8') as f:
        f.write('''# ALICE GREENFINGERS - INPUT MODEL SPECIFICATION (STEP 5)

*Generated on 2026-09-01*

## 1. Normalized Input Abstraction
- **Header:** `include/platform/input.h`
- **Implementation:** `src/platform/input.cpp`
- **Supported Event Types:**
  - `INPUT_MOUSE_MOVE`: Updates cursor `(x, y)`.
  - `INPUT_MOUSE_DOWN` / `INPUT_MOUSE_UP`: Left (1), Right (2), Middle (3).
  - `INPUT_KEY_DOWN` / `INPUT_KEY_UP`: Standard key codes.
  - `INPUT_QUIT`: Requests application shutdown.
- **Queue Model:** Circular FIFO buffer (`MAX_INPUT_QUEUE = 64`) decoupled from OS event polling.
''')
    log("Step 5: Created input.h/cpp and generated notes/PHASE_6_INPUT_MODEL.md")

    # ---------------------------------------------------------
    # STEP 6: EVENT DISPATCH INTEGRATION
    # ---------------------------------------------------------
    with open(os.path.join(NOTES_DIR, 'PHASE_6_INPUT_EVENT_PIPELINE.md'), 'w', encoding='utf-8') as f:
        f.write('''# ALICE GREENFINGERS - INPUT EVENT PIPELINE INTEGRATION (STEP 6)

*Generated on 2026-09-01*

## 1. Input-to-Dispatcher Routing
```
+--------------------------+
| OS Window Message        | (WM_LBUTTONDOWN, WM_KEYDOWN)
+------------+-------------+
             |
             v
+--------------------------+
| Input_PushEvent()        | (Normalized InputEvent queued)
+------------+-------------+
             |
             v
+--------------------------+
| Event_ProcessInput()     | (Evaluates active game state)
+------------+-------------+
             |
             v
+--------------------------+
| FUN_00404170 Dispatcher  | (Opcode matching, VTable slot +0x08 callback)
+------------+-------------+
             |
             v
+--------------------------+
| State / Global Mutation  | (State_SetState, DAT_004974f4, DAT_004a86a4)
+--------------------------+
```

## 2. Interactive Click Handlers per State
- **State 1 (MAIN_MENU):** Left click on "Start" bounds triggers Opcode `1001` (`STATE_GAMEPLAY`).
- **State 2 (NAME_DIALOG):** Left click on "OK" bounds triggers transition to `STATE_GAMEPLAY`.
- **State 3 (GAMEPLAY):** Left click on farm grid advances tile interaction; click on "Pause" triggers `STATE_PAUSE_OPTIONS` (Opcode `1002`); click on "Market" triggers `STATE_SHOP_MARKET`.
- **State 4 (PAUSE_OPTIONS):** Left click on "Resume" returns to `STATE_GAMEPLAY`.
- **State 5 (SHOP_MARKET):** Left click on "Return" returns to `STATE_GAMEPLAY`.
''')
    log("Step 6: Generated notes/PHASE_6_INPUT_EVENT_PIPELINE.md")

    # ---------------------------------------------------------
    # STEP 7 & 8: REAL-TIME LOOP & DETERMINISTIC CLOCK
    # ---------------------------------------------------------
    with open(os.path.join(NOTES_DIR, 'PHASE_6_REALTIME_LOOP.md'), 'w', encoding='utf-8') as f:
        f.write('''# ALICE GREENFINGERS - REAL-TIME LOOP SPECIFICATION (STEP 7)

*Generated on 2026-09-01*

## 1. Fixed Timestep Loop Architecture
```cpp
const double FIXED_DELTA_MS = 16.666667; // 60 Hz simulation
double accumulator = 0.0;

while (Window_IsRunning(win)) {
    // 1. Poll OS Events
    Window_PollEvents(win);

    // 2. Process Input Queue
    InputEvent evt;
    while (Input_PollEvent(&evt)) {
        Event_ProcessInput(&evt);
    }

    // 3. Fixed Timestep Simulation Update
    accumulator += elapsed_frame_time_ms;
    while (accumulator >= FIXED_DELTA_MS) {
        GameLoop_Tick(nullptr, 16); // FUN_004096a0 -> DAT_004a7f54++
        accumulator -= FIXED_DELTA_MS;
    }

    // 4. Render & Present
    RenderState rs = Render_BuildState();
    Renderer_Draw(&rs);
    Window_PresentBuffer(win, Renderer_GetBackbuffer(), 800, 600);
}
```
''')

    with open(os.path.join(NOTES_DIR, 'PHASE_6_CLOCK_INTEGRATION.md'), 'w', encoding='utf-8') as f:
        f.write('''# ALICE GREENFINGERS - DETERMINISTIC CLOCK INTEGRATION (STEP 8)

*Generated on 2026-09-01*

## 1. Clock Variable Separation & Invariants
| Variable | Domain | Determinism Property | Update Trigger |
| :--- | :--- | :--- | :--- |
| `DAT_004a7f54` | Simulation Tick | **100% Deterministic** | Advances exactly once per 16.67ms simulation step |
| `g_render_frame_count` | Presentation | Variable / Hardware dependent | Advances once per display refresh / backbuffer swap |
| `g_elapsed_real_time_ms`| OS Wall Clock | Monotonic timestamp | Measured via `GetTickCount()` |
''')
    log("Step 7 & 8: Generated notes/PHASE_6_REALTIME_LOOP.md and notes/PHASE_6_CLOCK_INTEGRATION.md")

    log("=== PHASE 6: STEPS 5 TO 8 COMPLETED SUCCESSFULLY ===")

if __name__ == '__main__':
    run_steps_5_to_8()
