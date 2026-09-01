# ALICE GREENFINGERS - WIN32 IMPORT POINTER RESOLUTION (STEP 10)

*Generated on 2026-09-01 17:57:25*

## 1. DETERMINISTIC PE IAT IMPORT RESOLUTION (Cluster E — 46 Call Sites)

| Library DLL | Imported API Symbol | Call Site Count | Resolution Status |
| --- | --- | ---: | :---: |
| `USER32.DLL` | `PeekMessageW / DispatchMessageW` | 8 | **[VERIFIED (E1/E2)]** |
| `USER32.DLL` | `CreateWindowExW / ShowWindow` | 6 | **[VERIFIED (E1/E2)]** |
| `USER32.DLL` | `GetDC / ReleaseDC` | 4 | **[VERIFIED (E1/E2)]** |
| `GDI32.DLL` | `BitBlt / SetDIBitsToDevice` | 10 | **[VERIFIED (E1/E2)]** |
| `GDI32.DLL` | `CreateCompatibleDC / DeleteDC` | 6 | **[VERIFIED (E1/E2)]** |
| `KERNEL32.DLL` | `GetTickCount / QueryPerformanceCounter` | 8 | **[VERIFIED (E1/E2)]** |
| `WINMM.DLL` | `timeGetTime / timeBeginPeriod` | 4 | **[VERIFIED (E1/E2)]** |
