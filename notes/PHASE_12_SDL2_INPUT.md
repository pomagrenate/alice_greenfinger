# ALICE GREENFINGERS - SDL2 INPUT ADAPTER (STEP 6)

*Generated on 2026-09-01*

## 1. Event Normalization Matrix
| SDL2 Event Type | Platform-Neutral Event | Target Dispatch Action |
| :--- | :--- | :--- |
| `SDL_MOUSEMOTION` | `INPUT_EVENT_MOUSE_MOVE` | Updates hover coordinates `(x, y)` |
| `SDL_MOUSEBUTTONDOWN` | `INPUT_EVENT_MOUSE_DOWN` | Triggers UI click / tile click |
| `SDL_MOUSEBUTTONUP` | `INPUT_EVENT_MOUSE_UP` | Completes drag / drop interaction |
| `SDL_KEYDOWN` | `INPUT_EVENT_KEY_DOWN` | Maps ESC key to Pause Opcode 1002 |
| `SDL_QUIT` | `INPUT_EVENT_QUIT` | Requests clean application exit |
