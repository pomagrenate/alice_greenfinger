# ALICE GREENFINGERS - INPUT MODEL SPECIFICATION (STEP 5)

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
