# ALICE GREENFINGERS - REAL-TIME LOOP SPECIFICATION (STEP 7)

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
