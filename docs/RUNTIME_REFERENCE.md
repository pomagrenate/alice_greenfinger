# Alice Greenfingers - Runtime Execution Model Reference

## 1. Real-Time Decoupled Loop
- **Fixed Timestep Simulation:** 60.0 Hz ($\Delta t = 16.67	ext{ ms}$) updates `DAT_004a7f54` monotonically.
- **Variable Presentation Loop:** Backbuffer is rendered and swapped independently of tick count.
- **Dual Execution Modes:**
  - **Interactive Desktop Window:** Native Win32 window blitting via `SetDIBitsToDevice`.
  - **Headless Automated Test Context:** Direct memory rendering with zero GUI display overhead.
