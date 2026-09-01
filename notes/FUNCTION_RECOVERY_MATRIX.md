# ALICE GREENFINGERS - EXHAUSTIVE FUNCTION RECOVERY MATRIX (STEP 2)

*Generated on 2026-09-01 13:08:50*

## FUNCTION AUDIT METRICS
- **Total Functions Extracted from Unpacked EXE:** 1,847
- **Confirmed Core Logic & Subroutines:** 1,847
- **Thunks / Jump Wrappers:** 0
- **Decompiler Coverage Rate:** 100% of discovered control flows extracted

## FUNCTION INVENTORY TABLE

| Address (RVA) | Identifier | Params | Lines of C | Subsystem & Type | Strings Referenced | APIs Called | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0x00401000` | `FUN_00401000` | 1 | 21 | `Helper Subroutine` | `None` | `Shell_NotifyIconW` | **Medium (Decompiled C Flow)** |
| `0x00401070` | `FUN_00401070` | 0 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004010a0` | `FUN_004010a0` | 0 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004010e0` | `FUN_004010e0` | 4 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00401100` | `FUN_00401100` | 3 | 80 | `Core Subsystem Logic` | `"TaskbarCreated"` | `DefWindowProcW, KillTimer, SetTimer` | **High (Decompiled C Flow)** |
| `0x00401250` | `FUN_00401250` | 1 | 47 | `Helper Subroutine` | `None` | `KillTimer, SetTimer, Shell_NotifyIconW` | **Medium (Decompiled C Flow)** |
| `0x004012f0` | `FUN_004012f0` | 0 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00401350` | `FUN_00401350` | 0 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00401380` | `FUN_00401380` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004013a0` | `FUN_004013a0` | 0 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004013c0` | `FUN_004013c0` | 1 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00401400` | `FUN_00401400` | 0 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00401460` | `FUN_00401460` | 2 | 32 | `Helper Subroutine` | `None` | `GetFullPathNameW` | **Medium (Decompiled C Flow)** |
| `0x00401500` | `FUN_00401500` | 0 | 333 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00401960` | `FUN_00401960` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00401980` | `FUN_00401980` | 2 | 36 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x004019d0` | `FUN_004019d0` | 0 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00401a10` | `FUN_00401a10` | 1 | 25 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00401a50` | `FUN_00401a50` | 0 | 49 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00401b10` | `FUN_00401b10` | 0 | 39 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00401b80` | `FUN_00401b80` | 0 | 55 | `Core Subsystem Logic` | `None` | `LoadStringW, Shell_NotifyIconW` | **High (Decompiled C Flow)** |
| `0x00401c90` | `FUN_00401c90` | 0 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00401cb0` | `FUN_00401cb0` | 1 | 132 | `Core Subsystem Logic` | `"close all"` | `UnregisterHotKey, DestroyWindow, FreeLibrary` | **High (Decompiled C Flow)** |
| `0x00401f20` | `FUN_00401f20` | 0 | 124 | `Script / Win32 Host Logic` | `"/AutoIt3ExecuteLine", "/ErrorStdOut", "/AutoIt3OutputDebug"` | `GetModuleFileNameW` | **High (Verified Logic)** |
| `0x00402160` | `FUN_00402160` | 0 | 42 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00402250` | `FUN_00402250` | 1 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00402280` | `FUN_00402280` | 0 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004022d0` | `FUN_004022d0` | 2 | 88 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00402400` | `FUN_00402400` | 0 | 84 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00402560` | `FUN_00402560` | 1 | 120 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x004026f0` | `FUN_004026f0` | 0 | 27 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00402710` | `FUN_00402710` | 0 | 37 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00402780` | `FUN_00402780` | 0 | 73 | `Core Subsystem Logic` | `None` | `FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x00402880` | `FUN_00402880` | 3 | 353 | `Core Subsystem Logic` | `None` | `CharUpperBuffW, FID_conflict__memcpy, SUB42` | **High (Decompiled C Flow)** |
| `0x00402e0a` | `FUN_00402e0a` | 0 | 335 | `Core Subsystem Logic` | `None` | `CharUpperBuffW, FID_conflict__memcpy, WARNING` | **High (Decompiled C Flow)** |
| `0x00402f00` | `FUN_00402f00` | 0 | 67 | `Core Subsystem Logic` | `None` | `ROUND, FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x00402f80` | `FUN_00402f80` | 2 | 66 | `Core Subsystem Logic` | `None` | `FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x00403020` | `FUN_00403020` | 1 | 32 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00403060` | `FUN_00403060` | 3 | 58 | `Core Subsystem Logic` | `None` | `CharUpperBuffW` | **High (Decompiled C Flow)** |
| `0x004031b0` | `FUN_004031b0` | 3 | 147 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00403350` | `FUN_00403350` | 0 | 35 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004033c0` | `FUN_004033c0` | 6 | 209 | `Core Subsystem Logic` | `"#include depth exceeded.  Make sure there are no recursive includes", "Error opening the file", "Unterminated string"` | `CONCAT31, FID_conflict___iswspace_l, GetCurrentDirectoryW` | **High (Decompiled C Flow)** |
| `0x0040373c` | `FUN_0040373c` | 0 | 21 | `Helper Subroutine` | `None` | `CONCAT31, SetCurrentDirectoryW` | **Medium (Decompiled C Flow)** |
| `0x004037a0` | `FUN_004037a0` | 0 | 150 | `Core Subsystem Logic` | `None` | `CARRY4, CONCAT31, ROUND` | **High (Decompiled C Flow)** |
| `0x00403910` | `FUN_00403910` | 2 | 45 | `Helper Subroutine` | `None` | `CARRY4, ReadFile` | **Medium (Decompiled C Flow)** |
| `0x004039a0` | `FUN_004039a0` | 0 | 60 | `Core Subsystem Logic` | `"#include"` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00403a20` | `FUN_00403a20` | 5 | 112 | `Script / Win32 Host Logic` | `",param_1);
        return false;
      }
      iVar1 = __wcsnicmp(param_1,L", "#notrayicon", ",0xd);
    if (iVar1 == 0) {
      if (*(int *)((int)this + 0x20) != 0) {
        uVar4 = 0;
        do {
          iVar1 = __wcsicmp((wchar_t *)**(undefined4 **)(*(int *)((int)this + 0x1c) + uVar4 * 4),
                            param_2);
          if (iVar1 == 0) {
            return (bool)(((**(int **)(*(int *)((int)this + 0x2c) + uVar4 * 4) < 2) - 1U & 3) + 1);
          }
          uVar4 = uVar4 + 1;
        } while (uVar4 < *(uint *)((int)this + 0x20));
        return true;
      }
    }
    else {
      iVar1 = __wcsnicmp(param_1,L"` | `None` | **High (Verified Logic)** |
| `0x00403a50` | `FUN_00403a50` | 2 | 40 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00403af0` | `FUN_00403af0` | 2 | 27 | `Helper Subroutine` | `None` | `MultiByteToWideChar` | **Medium (Decompiled C Flow)** |
| `0x00403b70` | `FUN_00403b70` | 2 | 36 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00403bd0` | `FUN_00403bd0` | 0 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00403c30` | `FUN_00403c30` | 1 | 27 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00403c90` | `FUN_00403c90` | 2 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00403cc0` | `FUN_00403cc0` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00403cd0` | `FUN_00403cd0` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00403d10` | `FUN_00403d10` | 4 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00403d80` | `FUN_00403d80` | 0 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00403da0` | `FUN_00403da0` | 1 | 37 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00403e10` | `FUN_00403e10` | 2 | 45 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00403ea0` | `FUN_00403ea0` | 2 | 164 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00404100` | `FUN_00404100` | 2 | 37 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00404170` | `FUN_00404170` | 2 | 2,408 | `Script / Win32 Host Logic` | `"WINGETPROCESS", "GUICTRLSETGRAPHIC", "TCPCLOSESOCKET"` | `None` | **High (Verified Logic)** |
| `0x00408cc0` | `FUN_00408cc0` | 3 | 62 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00408d90` | `FUN_00408d90` | 3 | 61 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00408e80` | `FUN_00408e80` | 1 | 129 | `Core Subsystem Logic` | `None` | `VariantCopy, VariantClear, VariantInit` | **High (Decompiled C Flow)** |
| `0x00408f40` | `FUN_00408f40` | 0 | 53 | `Core Subsystem Logic` | `None` | `VariantClear` | **High (Decompiled C Flow)** |
| `0x00408fc0` | `FUN_00408fc0` | 1 | 185 | `Core Subsystem Logic` | `"Variable must be of type \'Object\'."` | `None` | **High (Decompiled C Flow)** |
| `0x004091b0` | `FUN_004091b0` | 1 | 200 | `Core Subsystem Logic` | `None` | `CONCAT31, InterlockedDecrement, InterlockedIncrement` | **High (Decompiled C Flow)** |
| `0x004091e0` | `FUN_004091e0` | 2 | 481 | `Core Subsystem Logic` | `None` | `CONCAT44, GetExitCodeProcess, PeekMessageW` | **High (Decompiled C Flow)** |
| `0x004096a0` | `FUN_004096a0` | 4 | 1,869 | `Core Subsystem Logic` | `None` | `SEXT24, VariantCopy, CharUpperBuffW` | **High (Decompiled C Flow)** |
| `0x0040a780` | `FUN_0040a780` | 4 | 1,050 | `Core Subsystem Logic` | `"䲋త䏇\f", "삄萏޻", "쒃蔄࿀\xf584Ȑ謀褓謐ы䢉謄ࡓ傉謈౛墉，謃⑌褌ు䒋␤߿뢀ý"` | `CONCAT31, VariantCopy, CONCAT44` | **High (Decompiled C Flow)** |
| `0x0040afa0` | `FUN_0040afa0` | 3 | 695 | `Core Subsystem Logic` | `None` | `VariantCopy, CONCAT44, FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x0040b400` | `FUN_0040b400` | 1 | 65 | `Core Subsystem Logic` | `None` | `VariantClear` | **High (Decompiled C Flow)** |
| `0x0040b510` | `FUN_0040b510` | 3 | 106 | `Core Subsystem Logic` | `None` | `CARRY4, FID_conflict__memcpy, SUB84` | **High (Decompiled C Flow)** |
| `0x0040b5f0` | `FUN_0040b5f0` | 1 | 374 | `Core Subsystem Logic` | `None` | `CONCAT44` | **High (Decompiled C Flow)** |
| `0x0040b910` | `FUN_0040b910` | 0 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040b960` | `FUN_0040b960` | 0 | 129 | `Core Subsystem Logic` | `None` | `VariantCopy, VariantClear, VariantInit` | **High (Decompiled C Flow)** |
| `0x0040ba10` | `FUN_0040ba10` | 0 | 37 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0040baa0` | `FUN_0040baa0` | 1 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040bb00` | `FUN_0040bb00` | 1 | 41 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040bb80` | `FUN_0040bb80` | 0 | 63 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x0040bc10` | `FUN_0040bc10` | 0 | 40 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040bc70` | `FUN_0040bc70` | 1 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040bcc0` | `FUN_0040bcc0` | 1 | 45 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040bd20` | `FUN_0040bd20` | 2 | 36 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040bd50` | `FUN_0040bd50` | 1 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040bd80` | `FUN_0040bd80` | 2 | 56 | `Core Subsystem Logic` | `None` | `FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x0040be70` | `FUN_0040be70` | 0 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040bec0` | `FUN_0040bec0` | 4 | 48 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040bf20` | `FUN_0040bf20` | 3 | 294 | `Core Subsystem Logic` | `"Variable is not of type \'Object\'."` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0040c1f0` | `FUN_0040c1f0` | 3 | 76 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040c2c0` | `FUN_0040c2c0` | 3 | 63 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040c360` | `FUN_0040c360` | 0 | 59 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040c4c0` | `FUN_0040c4c0` | 0 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040c4e0` | `FUN_0040c4e0` | 4 | 94 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040c600` | `FUN_0040c600` | 2 | 24 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0040c620` | `FUN_0040c620` | 0 | 17 | `Helper Subroutine` | `None` | `GetTime` | **Medium (Decompiled C Flow)** |
| `0x0040c650` | `FUN_0040c650` | 2 | 47 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040c670` | `FUN_0040c670` | 0 | 71 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x0040c6e0` | `FUN_0040c6e0` | 4 | 48 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040c790` | `FUN_0040c790` | 0 | 38 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040c7f0` | `FUN_0040c7f0` | 0 | 121 | `Core Subsystem Logic` | `None` | `GetStdHandle, CloseHandle` | **High (Decompiled C Flow)** |
| `0x0040cb00` | `FUN_0040cb00` | 1 | 130 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040cbd0` | `FUN_0040cbd0` | 2 | 29 | `Helper Subroutine` | `None` | `QueryPerformanceCounter` | **Medium (Decompiled C Flow)** |
| `0x0040cc30` | `FUN_0040cc30` | 0 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040cc70` | `FUN_0040cc70` | 4 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040ccd0` | `FUN_0040ccd0` | 3 | 167 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0040ce70` | `FUN_0040ce70` | 1 | 36 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040ce80` | `FUN_0040ce80` | 2 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040ceb0` | `FUN_0040ceb0` | 0 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040cf00` | `FUN_0040cf00` | 3 | 55 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040cfc0` | `FUN_0040cfc0` | 2 | 25 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0040cff0` | `FUN_0040cff0` | 0 | 37 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040d040` | `FUN_0040d040` | 0 | 34 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0040d090` | `FUN_0040d090` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040d0b0` | `FUN_0040d0b0` | 0 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040d0d0` | `FUN_0040d0d0` | 0 | 31 | `Helper Subroutine` | `"WM_GETCONTROLNAME"` | `RegisterWindowMessageW` | **Medium (Decompiled C Flow)** |
| `0x0040d150` | `FUN_0040d150` | 2 | 30 | `Helper Subroutine` | `None` | `TranslateAcceleratorW` | **Medium (Decompiled C Flow)** |
| `0x0040d170` | `FUN_0040d170` | 1 | 47 | `Helper Subroutine` | `None` | `IsDialogMessageW` | **Medium (Decompiled C Flow)** |
| `0x0040d1a0` | `FUN_0040d1a0` | 0 | 35 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0040d200` | `FUN_0040d200` | 0 | 30 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0040d220` | `FUN_0040d220` | 2 | 25 | `Helper Subroutine` | `None` | `QueryPerformanceCounter` | **Medium (Decompiled C Flow)** |
| `0x0040d260` | `FUN_0040d260` | 2 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040d290` | `FUN_0040d290` | 0 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040d2c0` | `FUN_0040d2c0` | 0 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040d330` | `FUN_0040d330` | 0 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040d370` | `FUN_0040d370` | 0 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040d3b0` | `FUN_0040d3b0` | 3 | 26 | `Helper Subroutine` | `None` | `Sleep, GetTime` | **Medium (Decompiled C Flow)** |
| `0x0040d410` | `FUN_0040d410` | 0 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040d440` | `FUN_0040d440` | 0 | 56 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040d530` | `FUN_0040d530` | 0 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040d590` | `FUN_0040d590` | 0 | 102 | `Script / Win32 Host Logic` | `";
        pHVar5 = GetForegroundWindow();
        ShellExecuteW(pHVar5,pwVar7,pWVar8,in_EAX,pWVar9,IVar10);
      }
      else {
        FUN_00401b10();
        FUN_0040d200();
        FUN_0040d200();
        IVar10 = 1;
        pWVar9 = local_22c;
        pWVar8 = local_43c;
        pwVar7 = L", "This is a compiled AutoIt script. AV researchers please email avsupport@autoitscript.com for support.", ",0x10);
    return;
  }
  if (DAT_004a7f54 == 0) {
    DAT_004974f4 = 0xffffffff;
  }
  else {
    local_5 = '\0';
    if (DAT_004a7f54 == 1) {
      local_6 = '\0';
      FUN_00403a50(1,0xffffffff);
      DAT_004a90eb = DAT_004974e8;
      cVar6 = local_6;
    }
    else {
      uVar3 = FUN_0040f520(&local_5,&DAT_004a7f54);
      cVar6 = DAT_004a90e9;
      if ((char)uVar3 == '\0') {
        DAT_004974f4 = 1;
        goto LAB_0040d699;
      }
      DAT_004a7f58 = DAT_004a90e8;
      GetFullPathNameW(&DAT_004a7f6c,0x104,local_43c,(LPWSTR *)&DAT_004a7f50);
    }
    iVar4 = FUN_00401460(&DAT_004a7f6c,DAT_004a7f54);
    if (iVar4 != 0) {
      FUN_0040ec50();
      SetCurrentDirectoryW(local_22c);
      DAT_004974f4 = 1;
      return;
    }
    if ((cVar6 != '\x01') || (bVar1 = FUN_00432fee(), bVar1)) {
      FUN_00410390();
      FUN_00410570();
      if (DAT_004a7f58 == '\0') {
        FUN_0040e0c0();
      }
      FUN_004091e0(&DAT_004a8178,1);
      if (DAT_004a7f58 == '\0') {
        FUN_00401000(0x4a8710);
      }
    }
    else {
      GetModuleFileNameW((HMODULE)0x0,local_43c,0x104);
      if (local_5 == '\0') {
        IVar10 = 1;
        pWVar9 = local_22c;
        pWVar8 = local_43c;
        pwVar7 = L"` | `GetCurrentDirectoryW, SetCurrentDirectoryW, GetFullPathNameW` | **High (Verified Logic)** |
| `0x0040d6b0` | `FUN_0040d6b0` | 1 | 38 | `Helper Subroutine` | `None` | `SystemParametersInfoW` | **Medium (Decompiled C Flow)** |
| `0x0040d7c0` | `FUN_0040d7c0` | 0 | 44 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0040d860` | `FUN_0040d860` | 3 | 163 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040da20` | `FUN_0040da20` | 0 | 27 | `Helper Subroutine` | `None` | `CloseHandle` | **Medium (Decompiled C Flow)** |
| `0x0040da60` | `FUN_0040da60` | 0 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040da90` | `FUN_0040da90` | 0 | 38 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040daf0` | `FUN_0040daf0` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040db10` | `FUN_0040db10` | 0 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040db70` | `FUN_0040db70` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040db90` | `FUN_0040db90` | 0 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040dbb0` | `FUN_0040dbb0` | 0 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040dbd0` | `FUN_0040dbd0` | 0 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040dc00` | `FUN_0040dc00` | 1 | 37 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0040dc90` | `FUN_0040dc90` | 0 | 64 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040ddd0` | `FUN_0040ddd0` | 0 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040de10` | `FUN_0040de10` | 0 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040de40` | `FUN_0040de40` | 1 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040dea0` | `FUN_0040dea0` | 0 | 98 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0040df90` | `FUN_0040df90` | 3 | 67 | `Core Subsystem Logic` | `None` | `CARRY4, CONCAT31, SetFilePointerEx` | **High (Decompiled C Flow)** |
| `0x0040e050` | `FUN_0040e050` | 1 | 15 | `Helper Subroutine` | `None` | `CONCAT44, SetFilePointerEx, ZEXT48` | **Medium (Decompiled C Flow)** |
| `0x0040e080` | `FUN_0040e080` | 0 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e0a0` | `FUN_0040e0a0` | 1 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e0c0` | `FUN_0040e0c0` | 0 | 56 | `Core Subsystem Logic` | `None` | `DestroyIcon, Shell_NotifyIconW` | **High (Decompiled C Flow)** |
| `0x0040e1c0` | `FUN_0040e1c0` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e1f0` | `FUN_0040e1f0` | 0 | 41 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e270` | `FUN_0040e270` | 0 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e2a0` | `FUN_0040e2a0` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e2d0` | `FUN_0040e2d0` | 0 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e310` | `FUN_0040e310` | 0 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e360` | `FUN_0040e360` | 0 | 80 | `Core Subsystem Logic` | `"Include"` | `GetModuleFileNameW` | **High (Decompiled C Flow)** |
| `0x0040e4c0` | `FUN_0040e4c0` | 0 | 40 | `Script / Win32 Host Logic` | `"Software\\AutoIt v3\\AutoIt", "Include"` | `RegOpenKeyExW, RegQueryValueExW, RegCloseKey` | **High (Verified Logic)** |
| `0x0040e500` | `FUN_0040e500` | 0 | 150 | `Core Subsystem Logic` | `None` | `FreeLibrary, GetSystemInfo, GetCurrentProcess` | **High (Decompiled C Flow)** |
| `0x0040e660` | `FUN_0040e660` | 0 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e680` | `FUN_0040e680` | 0 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e6a0` | `FUN_0040e6a0` | 0 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e6e0` | `FUN_0040e6e0` | 0 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e710` | `FUN_0040e710` | 0 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e750` | `FUN_0040e750` | 0 | 28 | `Helper Subroutine` | `None` | `OleUninitialize` | **Medium (Decompiled C Flow)** |
| `0x0040e790` | `FUN_0040e790` | 4 | 63 | `Core Subsystem Logic` | `None` | `CompareStringW` | **High (Decompiled C Flow)** |
| `0x0040e7d0` | `FUN_0040e7d0` | 3 | 77 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040e810` | `FUN_0040e810` | 0 | 57 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040e830` | `FUN_0040e830` | 1 | 86 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0040e950` | `FUN_0040e950` | 0 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040e9a0` | `FUN_0040e9a0` | 5 | 55 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040e9f0` | `FUN_0040e9f0` | 2 | 33 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0040ea70` | `FUN_0040ea70` | 2 | 31 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0040ead0` | `FUN_0040ead0` | 0 | 46 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040eb50` | `FUN_0040eb50` | 0 | 35 | `Helper Subroutine` | `None` | `CharUpperBuffW` | **Medium (Decompiled C Flow)** |
| `0x0040ebb0` | `FUN_0040ebb0` | 0 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040ebd0` | `FUN_0040ebd0` | 0 | 22 | `Helper Subroutine` | `"IsThemeActive", "uxtheme.dll"` | `LoadLibraryA, GetProcAddress` | **Medium (Decompiled C Flow)** |
| `0x0040ec00` | `FUN_0040ec00` | 0 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040ec20` | `FUN_0040ec20` | 0 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040ec50` | `FUN_0040ec50` | 0 | 46 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040ed70` | `FUN_0040ed70` | 2 | 36 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040edc0` | `FUN_0040edc0` | 1 | 36 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040ee60` | `FUN_0040ee60` | 2 | 42 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040eec0` | `FUN_0040eec0` | 1 | 37 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040ef20` | `FUN_0040ef20` | 0 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040ef40` | `FUN_0040ef40` | 0 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040ef60` | `FUN_0040ef60` | 0 | 22 | `Helper Subroutine` | `"IsWow64Process", "kernel32.dll"` | `LoadLibraryA, GetProcAddress` | **Medium (Decompiled C Flow)** |
| `0x0040ef90` | `FUN_0040ef90` | 0 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040efb0` | `FUN_0040efb0` | 0 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040efd0` | `FUN_0040efd0` | 0 | 22 | `Helper Subroutine` | `"kernel32.dll", "GetNativeSystemInfo"` | `LoadLibraryA, GetProcAddress` | **Medium (Decompiled C Flow)** |
| `0x0040f000` | `FUN_0040f000` | 0 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f030` | `FUN_0040f030` | 0 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f060` | `FUN_0040f060` | 0 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f090` | `FUN_0040f090` | 0 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f0a0` | `FUN_0040f0a0` | 0 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f0c0` | `FUN_0040f0c0` | 2 | 57 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040f0f0` | `FUN_0040f0f0` | 0 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f110` | `FUN_0040f110` | 2 | 44 | `Helper Subroutine` | `None` | `CreateFileW` | **Medium (Decompiled C Flow)** |
| `0x0040f160` | `FUN_0040f160` | 0 | 40 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f170` | `FUN_0040f170` | 0 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f190` | `FUN_0040f190` | 0 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f1b0` | `FUN_0040f1b0` | 0 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f1d0` | `FUN_0040f1d0` | 1 | 17 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0040f1f0` | `FUN_0040f1f0` | 0 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f210` | `FUN_0040f210` | 1 | 19 | `Helper Subroutine` | `"SwapMouseButtons", "Control Panel\\Mouse"` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0040f250` | `FUN_0040f250` | 5 | 39 | `Script / Win32 Host Logic` | `None` | `CONCAT31, RegOpenKeyExW, RegQueryValueExW` | **High (Verified Logic)** |
| `0x0040f2e0` | `FUN_0040f2e0` | 0 | 25 | `Helper Subroutine` | `None` | `QueryPerformanceFrequency` | **Medium (Decompiled C Flow)** |
| `0x0040f310` | `FUN_0040f310` | 0 | 59 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0040f380` | `FUN_0040f380` | 0 | 37 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f410` | `FUN_0040f410` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f430` | `FUN_0040f430` | 1 | 30 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0040f490` | `FUN_0040f490` | 2 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f4d0` | `FUN_0040f4d0` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f4e0` | `FUN_0040f4e0` | 1 | 15 | `Helper Subroutine` | `None` | `SystemParametersInfoW` | **Medium (Decompiled C Flow)** |
| `0x0040f520` | `FUN_0040f520` | 2 | 38 | `Script / Win32 Host Logic` | `"AutoIt script files (*.au3, *.a3x)", "au3", "Run Script:"` | `GetOpenFileNameW` | **High (Verified Logic)** |
| `0x0040f570` | `FUN_0040f570` | 3 | 144 | `Core Subsystem Logic` | `">>>AUTOIT SCRIPT<<<"` | `CONCAT31, CONCAT44` | **High (Decompiled C Flow)** |
| `0x0040f5c0` | `FUN_0040f5c0` | 1 | 76 | `Core Subsystem Logic` | `"EA06"` | `FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x0040f6f0` | `FUN_0040f6f0` | 1 | 33 | `Helper Subroutine` | `None` | `WideCharToMultiByte` | **Medium (Decompiled C Flow)** |
| `0x0040f760` | `FUN_0040f760` | 1 | 69 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0040f820` | `FUN_0040f820` | 0 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f850` | `FUN_0040f850` | 0 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f880` | `FUN_0040f880` | 1 | 37 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0040f910` | `FUN_0040f910` | 0 | 29 | `Helper Subroutine` | `"%02X"` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040f9d0` | `FUN_0040f9d0` | 2 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0040fa10` | `FUN_0040fa10` | 1 | 171 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x004100c0` | `FUN_004100c0` | 1 | 23 | `Helper Subroutine` | `None` | `CONCAT21, CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00410100` | `FUN_00410100` | 0 | 28 | `Helper Subroutine` | `">>>AUTOIT NO CMDEXECUTE<<<"` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00410120` | `FUN_00410120` | 0 | 18 | `Helper Subroutine` | `None` | `GetFullPathNameW` | **Medium (Decompiled C Flow)** |
| `0x00410160` | `FUN_00410160` | 0 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410190` | `FUN_00410190` | 2 | 36 | `Helper Subroutine` | `None` | `GetFullPathNameW` | **Medium (Decompiled C Flow)** |
| `0x00410200` | `FUN_00410200` | 1 | 37 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00410290` | `FUN_00410290` | 0 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004102b0` | `FUN_004102b0` | 0 | 50 | `Helper Subroutine` | `None` | `CONCAT31, SHGetDesktopFolder, SHGetPathFromIDListW` | **Medium (Decompiled C Flow)** |
| `0x00410390` | `FUN_00410390` | 0 | 39 | `Script / Win32 Host Logic` | `"AutoIt v3"` | `LoadCursorW, GetSysColorBrush, LoadImageW` | **High (Verified Logic)** |
| `0x00410490` | `FUN_00410490` | 2 | 38 | `Script / Win32 Host Logic` | `"AutoIt v3 GUI", "TaskbarCreated"` | `GetSysColorBrush, ImageList_ReplaceIcon, RegisterClassExW` | **High (Verified Logic)** |
| `0x00410570` | `FUN_00410570` | 0 | 16 | `Script / Win32 Host Logic` | `"AutoIt v3", "edit"` | `CreateWindowExW, ShowWindow` | **High (Verified Logic)** |
| `0x00410600` | `FUN_00410600` | 0 | 53 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00410620` | `FUN_00410620` | 0 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410640` | `FUN_00410640` | 0 | 23 | `Helper Subroutine` | `None` | `CloseHandle, VirtualFreeEx` | **Medium (Decompiled C Flow)** |
| `0x00410660` | `FUN_00410660` | 0 | 41 | `Helper Subroutine` | `None` | `DestroyIcon` | **Medium (Decompiled C Flow)** |
| `0x00410780` | `FUN_00410780` | 0 | 31 | `Helper Subroutine` | `None` | `DestroyWindow, DeleteObject` | **Medium (Decompiled C Flow)** |
| `0x004107b0` | `FUN_004107b0` | 0 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004107c0` | `FUN_004107c0` | 0 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004107d0` | `FUN_004107d0` | 0 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410800` | `FUN_00410800` | 0 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410820` | `FUN_00410820` | 0 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410860` | `FUN_00410860` | 0 | 33 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004108f0` | `FUN_00408f40` | 0 | 53 | `Core Subsystem Logic` | `None` | `VariantClear` | **High (Decompiled C Flow)** |
| `0x00410900` | `FUN_00410900` | 0 | 45 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410940` | `FUN_00410940` | 0 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410960` | `FUN_00410960` | 0 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004109a0` | `FUN_004109a0` | 0 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004109c0` | `FUN_004109c0` | 0 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004109e0` | `FUN_004109e0` | 0 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410a00` | `FUN_00410a00` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410a30` | `FUN_00410a30` | 0 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410a40` | `FUN_00410a40` | 0 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410a70` | `FUN_00410a70` | 0 | 30 | `Helper Subroutine` | `None` | `FreeLibrary` | **Medium (Decompiled C Flow)** |
| `0x00410aa0` | `FUN_00410aa0` | 0 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410ab0` | `FUN_00410ab0` | 0 | 34 | `Helper Subroutine` | `None` | `MapVirtualKeyW` | **Medium (Decompiled C Flow)** |
| `0x00410b20` | `FUN_00410b20` | 0 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410b50` | `FUN_00410b50` | 0 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410b70` | `FUN_00410b70` | 0 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410ba0` | `FUN_00410ba0` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410bc0` | `FUN_00410bc0` | 0 | 14 | `Helper Subroutine` | `None` | `CharUpperBuffW` | **Medium (Decompiled C Flow)** |
| `0x00410be0` | `FUN_00410be0` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410bf0` | `FUN_00410bf0` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410c20` | `FUN_00410c20` | 4 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410c60` | `FUN_00410c60` | 1 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410ca0` | `FUN_00410ca0` | 0 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410cd0` | `FUN_00410cd0` | 0 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410cfc` | `FUN_00410cfc` | 3 | 45 | `Helper Subroutine` | `None` | `CONCAT44` | **Medium (Decompiled C Flow)** |
| `0x00410de2` | `FUN_00410de2` | 0 | 38 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410e44` | `FUN_00410e44` | 1 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410e4b` | `FUN_00410e4b` | 0 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00410e53` | `FUN_00410e53` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004111dc` | `FUN_004111dc` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00411304` | `FUN_00411304` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00411593` | `FUN_00411593` | 2 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004115ba` | `FUN_004115ba` | 2 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041169a` | `FUN_0041169a` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004116a3` | `FUN_004116a3` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004118c5` | `FUN_004118c5` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00411942` | `FUN_00411942` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00413190` | `FUN_00413190` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041319b` | `FUN_0041319b` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041324e` | `FUN_0041324e` | 1 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041351d` | `FUN_0041351d` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00413650` | `FUN_00413650` | 2 | 50 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00413660` | `FUN_00413660` | 2 | 80 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00413b52` | `FUN_00413b52` | 0 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00414021` | `FUN_00414021` | 1 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00414131` | `FUN_00414131` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00414326` | `FUN_00414326` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00414432` | `FUN_00414432` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041458e` | `FUN_0041458e` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004145bd` | `FUN_004145bd` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041460f` | `FUN_0041460f` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004149b8` | `FUN_004149b8` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00414ab2` | `FUN_00414ab2` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00414cfa` | `FUN_00414cfa` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00414e3c` | `FUN_00414e3c` | 2 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041503d` | `FUN_0041503d` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00415143` | `FUN_00415143` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004152bb` | `FUN_004152bb` | 1 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041539a` | `FUN_0041539a` | 0 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00415658` | `FUN_00415658` | 2 | 143 | `Core Subsystem Logic` | `None` | `FID_conflict___get_dstbias` | **High (Decompiled C Flow)** |
| `0x004169f1` | `FUN_004169f1` | 1 | 137 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0041711d` | `FUN_0041711d` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041738b` | `FUN_0041738b` | 0 | 84 | `Core Subsystem Logic` | `None` | `SystemCP, InterlockedDecrement, InterlockedIncrement` | **High (Decompiled C Flow)** |
| `0x004174ec` | `FUN_004174ec` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00417870` | `FUN_00417870` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041787c` | `FUN_0041787c` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004178a8` | `FUN_004178a8` | 0 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004179de` | `FUN_004179de` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004179e7` | `FUN_004179e7` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00417b9d` | `FUN_00417b9d` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00417ba9` | `FUN_00417ba9` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00417d9b` | `FUN_00417d9b` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00417ef8` | `FUN_00417ef8` | 5 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00417f25` | `FUN_00417f25` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00417fdd` | `FUN_00417fdd` | 1 | 16 | `Helper Subroutine` | `"Unknown exception"` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041807d` | `FUN_0041807d` | 1 | 12 | `Helper Subroutine` | `None` | `Tidy` | **Medium (Decompiled C Flow)** |
| `0x00418088` | `FUN_00418088` | 2 | 15 | `Helper Subroutine` | `None` | `Tidy` | **Medium (Decompiled C Flow)** |
| `0x004181f2` | `FUN_004181f2` | 1 | 11 | `Helper Subroutine` | `None` | `LeaveCriticalSection` | **Medium (Decompiled C Flow)** |
| `0x004182c2` | `FUN_004182c2` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00418337` | `FUN_00418337` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041839d` | `FUN_0041839d` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00418511` | `FUN_00418511` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041854d` | `FUN_0041854d` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041855c` | `FUN_0041855c` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041912b` | `FUN_0041912b` | 2 | 37 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00419192` | `FUN_00419192` | 4 | 555 | `Core Subsystem Logic` | `None` | `CONCAT44, CONCAT31, LocaleUpdate` | **High (Decompiled C Flow)** |
| `0x0041aeec` | `FUN_0041aeec` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041afee` | `FUN_0041afee` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041b0ac` | `FUN_0041b0ac` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041b87e` | `FUN_0041b87e` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041b8b9` | `FUN_0041b8b9` | 2 | 36 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041b91b` | `FUN_0041b91b` | 4 | 574 | `Core Subsystem Logic` | `None` | `CONCAT44, CONCAT31, LocaleUpdate` | **High (Decompiled C Flow)** |
| `0x0041c5f4` | `FUN_0041c5f4` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041c8eb` | `FUN_0041c8eb` | 3 | 51 | `Core Subsystem Logic` | `None` | `CONCAT16, CONCAT17, CONCAT24` | **High (Decompiled C Flow)** |
| `0x0041d0da` | `FUN_0041d0da` | 0 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041d5fb` | `FUN_0041d5fb` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041d6e6` | `FUN_0041d6e6` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041d8ba` | `FUN_0041d8ba` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041e0ba` | `FUN_0041e0ba` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041e2c0` | `FUN_0041e2c0` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041e35b` | `FUN_0041e35b` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041e364` | `FUN_0041e364` | 0 | 170 | `Core Subsystem Logic` | `None` | `GetTimeZoneInformation, FID_conflict___get_dstbias, WideCharToMultiByte` | **High (Decompiled C Flow)** |
| `0x0041e5e7` | `FUN_0041e5e7` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041e677` | `FUN_0041e677` | 10 | 99 | `Core Subsystem Logic` | `None` | `FID_conflict___get_dstbias` | **High (Decompiled C Flow)** |
| `0x0041e86e` | `FUN_0041e86e` | 0 | 99 | `Core Subsystem Logic` | `None` | `FID_conflict___get_dstbias` | **High (Decompiled C Flow)** |
| `0x0041ea8b` | `FUN_0041ea8b` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041eacc` | `FUN_0041eacc` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041ed95` | `FUN_0041ed95` | 0 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041ed9b` | `FUN_0041ed9b` | 0 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041eda1` | `FUN_0041eda1` | 0 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041eda7` | `FUN_0041eda7` | 0 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0041f2a4` | `FUN_0041f2a4` | 0 | 63 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0041fe19` | `FUN_0041fe19` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00420057` | `FUN_00420057` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004205f9` | `FUN_004205f9` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00420829` | `FUN_00420829` | 0 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004215c4` | `FUN_004215c4` | 6 | 100 | `Core Subsystem Logic` | `"e+000"` | `LocaleUpdate, FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x0042200c` | `FUN_0042200c` | 3 | 125 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x004223fd` | `FUN_004223fd` | 0 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00422400` | `FUN_00422400` | 5 | 361 | `Core Subsystem Logic` | `None` | `CONCAT44, GetLastError, GetFileType` | **High (Decompiled C Flow)** |
| `0x00422bcb` | `FUN_00422bcb` | 0 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00422d54` | `FUN_00422d54` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00423473` | `FUN_00423473` | 5 | 40 | `Helper Subroutine` | `None` | `I10_OUTPUT` | **Medium (Decompiled C Flow)** |
| `0x004238c3` | `FUN_004238c3` | 0 | 13 | `Helper Subroutine` | `None` | `CloseHandle` | **Medium (Decompiled C Flow)** |
| `0x00425914` | `FUN_00425914` | 1 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042592f` | `FUN_0042592f` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042593c` | `FUN_0042593c` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00425947` | `FUN_00425947` | 1 | 23 | `Helper Subroutine` | `None` | `SQRT` | **Medium (Decompiled C Flow)** |
| `0x00425976` | `FUN_00425976` | 1 | 25 | `Helper Subroutine` | `None` | `SQRT` | **Medium (Decompiled C Flow)** |
| `0x004259ab` | `FUN_004259ab` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004259b6` | `FUN_004259b6` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004259bf` | `FUN_004259bf` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004259c8` | `FUN_004259c8` | 1 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004259d1` | `FUN_004259d1` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004259e2` | `FUN_004259e2` | 1 | 10 | `Helper Subroutine` | `None` | `SQRT` | **Medium (Decompiled C Flow)** |
| `0x004259eb` | `FUN_004259eb` | 2 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00425a0e` | `FUN_00425a0e` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00425a36` | `FUN_00425a36` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00425a80` | `FUN_00425a80` | 2 | 33 | `Helper Subroutine` | `None` | `CONCAT44, ROUND` | **Medium (Decompiled C Flow)** |
| `0x00425ab6` | `FUN_00425ab6` | 0 | 30 | `Helper Subroutine` | `None` | `CONCAT44, ROUND` | **Medium (Decompiled C Flow)** |
| `0x00425b2b` | `FUN_00425b2b` | 0 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00425e5d` | `FUN_0040e002` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004266b2` | `FUN_004266b2` | 1 | 159 | `Core Subsystem Logic` | `None` | `CARRY4, CONCAT31, ROUND` | **High (Decompiled C Flow)** |
| `0x004273df` | `FUN_004273df` | 0 | 34 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00427496` | `FUN_00427496` | 0 | 138 | `Core Subsystem Logic` | `None` | `CONCAT31, WARNING` | **High (Decompiled C Flow)** |
| `0x004274d0` | `FUN_004274d0` | 0 | 22 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x004279bf` | `FUN_004279bf` | 1 | 383 | `Core Subsystem Logic` | `None` | `WARNING` | **High (Decompiled C Flow)** |
| `0x00427a28` | `FUN_00427a28` | 1 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00427a75` | `FUN_00427a75` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00427a7e` | `FUN_00427a7e` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00427a84` | `FUN_00427a84` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00427a8a` | `FUN_00427a8a` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00427a93` | `FUN_00427a93` | 0 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00427ad0` | `FUN_00427ad0` | 1 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00427d10` | `FUN_00427d10` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00427e13` | `FUN_00427e13` | 0 | 337 | `Core Subsystem Logic` | `None` | `CharUpperBuffW, FID_conflict__memcpy, WARNING` | **High (Decompiled C Flow)** |
| `0x00427e43` | `FUN_00427e43` | 0 | 337 | `Core Subsystem Logic` | `None` | `CharUpperBuffW, FID_conflict__memcpy, WARNING` | **High (Decompiled C Flow)** |
| `0x00427f16` | `FUN_00427f16` | 0 | 336 | `Core Subsystem Logic` | `None` | `CharUpperBuffW, FID_conflict__memcpy, WARNING` | **High (Decompiled C Flow)** |
| `0x004282d6` | `FUN_004282d6` | 0 | 181 | `Core Subsystem Logic` | `"Unterminated string"` | `CONCAT31, FID_conflict___iswspace_l, SetCurrentDirectoryW` | **High (Decompiled C Flow)** |
| `0x00428adf` | `FUN_00428adf` | 0 | 41 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00429f86` | `FUN_00429f86` | 57 | 1,274 | `Core Subsystem Logic` | `None` | `VariantCopy, CONCAT44, CONCAT13` | **High (Decompiled C Flow)** |
| `0x0042a281` | `FUN_0042a281` | 0 | 1,327 | `Core Subsystem Logic` | `None` | `VariantCopy, CONCAT44, CONCAT13` | **High (Decompiled C Flow)** |
| `0x0042a364` | `FUN_0042a364` | 0 | 1,321 | `Core Subsystem Logic` | `None` | `VariantCopy, CONCAT44, CONCAT13` | **High (Decompiled C Flow)** |
| `0x0042afca` | `FUN_0042afca` | 0 | 22 | `Helper Subroutine` | `None` | `DefWindowProcW` | **Medium (Decompiled C Flow)** |
| `0x0042b05e` | `FUN_0042b05e` | 0 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042b1a0` | `FUN_0042b1a0` | 23 | 967 | `Core Subsystem Logic` | `"䲋త䏇\f", "삄萏޻", "쒃蔄࿀\xf584Ȑ謀褓謐ы䢉謄ࡓ傉謈౛墉，謃⑌褌ు䒋␤߿뢀ý"` | `CONCAT31, VariantCopy, CONCAT44` | **High (Decompiled C Flow)** |
| `0x0042bac5` | `FUN_0042bac5` | 22 | 962 | `Core Subsystem Logic` | `"䲋త䏇\f", "삄萏޻", "쒃蔄࿀\xf584Ȑ謀褓謐ы䢉謄ࡓ傉謈౛墉，謃⑌褌ు䒋␤߿뢀ý"` | `CONCAT31, VariantCopy, CONCAT44` | **High (Decompiled C Flow)** |
| `0x0042bbdf` | `FUN_0042bbdf` | 0 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042be0a` | `FUN_0042be0a` | 0 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042c504` | `FUN_0042c504` | 2 | 104 | `Core Subsystem Logic` | `None` | `WARNING` | **High (Decompiled C Flow)** |
| `0x0042c58e` | `FUN_0042c58e` | 0 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042d09c` | `FUN_0042d09c` | 0 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042dec0` | `FUN_0042dec0` | 0 | 504 | `Core Subsystem Logic` | `None` | `CONCAT44, GetExitCodeProcess, PeekMessageW` | **High (Decompiled C Flow)** |
| `0x0042e124` | `FUN_0042e124` | 0 | 455 | `Core Subsystem Logic` | `None` | `CONCAT44, GetExitCodeProcess, PeekMessageW` | **High (Decompiled C Flow)** |
| `0x0042e158` | `FUN_0042e158` | 0 | 18 | `Helper Subroutine` | `None` | `TranslateMessage, DispatchMessageW` | **Medium (Decompiled C Flow)** |
| `0x0042e2fd` | `FUN_0042e2fd` | 2 | 134 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0042e645` | `FUN_0042e645` | 2 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042e688` | `FUN_0042e688` | 2 | 75 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0042e796` | `FUN_0042e796` | 2 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042e7e1` | `FUN_0042e7e1` | 5 | 84 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0042e9b5` | `FUN_0042e9b5` | 5 | 80 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0042eb5b` | `FUN_0042eb5b` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042eb62` | `FUN_0042eb62` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042eb69` | `FUN_0042eb69` | 5 | 24 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0042ebce` | `FUN_0042ebce` | 5 | 47 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042ec51` | `FUN_0042ec51` | 2 | 28 | `Helper Subroutine` | `"alpha"` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042eca2` | `FUN_0042eca2` | 2 | 33 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042ecee` | `FUN_0042ecee` | 2 | 87 | `Core Subsystem Logic` | `None` | `CONCAT11` | **High (Decompiled C Flow)** |
| `0x0042ee0a` | `FUN_0042ee0a` | 3 | 99 | `Core Subsystem Logic` | `None` | `CONCAT11` | **High (Decompiled C Flow)** |
| `0x0042ef5a` | `FUN_0042ef5a` | 4 | 169 | `Core Subsystem Logic` | `None` | `CONCAT11` | **High (Decompiled C Flow)** |
| `0x0042f272` | `FUN_0042f272` | 4 | 44 | `Helper Subroutine` | `None` | `CONCAT11` | **Medium (Decompiled C Flow)** |
| `0x0042f373` | `FUN_0042f373` | 7 | 235 | `Core Subsystem Logic` | `"Q\\E"` | `None` | **High (Decompiled C Flow)** |
| `0x0042f739` | `FUN_0042f739` | 4 | 52 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0042f7d2` | `FUN_0042f7d2` | 1 | 41 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042f85b` | `FUN_0042f85b` | 5 | 259 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0042fd00` | `FUN_0042fd00` | 1 | 28 | `Helper Subroutine` | `"Error text not found (please report)", "no error"` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042fd29` | `FUN_0042fd29` | 2 | 27 | `Helper Subroutine` | `None` | `StrokePath, EndPath, DeleteObject` | **Medium (Decompiled C Flow)** |
| `0x0042fda6` | `FUN_0042fda6` | 4 | 19 | `Helper Subroutine` | `None` | `ClientToScreen, DefDlgProcW, ImageList_DragMove` | **Medium (Decompiled C Flow)** |
| `0x0042fe05` | `FUN_0042fe05` | 3 | 18 | `Helper Subroutine` | `None` | `DefDlgProcW, CONCAT22, GetWindowLongW` | **Medium (Decompiled C Flow)** |
| `0x0042fe47` | `FUN_0042fe47` | 2 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042fe94` | `FUN_0042fe94` | 2 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042fed8` | `FUN_0042fed8` | 1 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042ff16` | `FUN_0042ff16` | 2 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042ff9f` | `FUN_0042ff9f` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042ffbe` | `FUN_0042ffbe` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0042ffda` | `FUN_0042ffda` | 1 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430003` | `FUN_00430003` | 2 | 42 | `Helper Subroutine` | `None` | `InvalidateRect` | **Medium (Decompiled C Flow)** |
| `0x0043009d` | `FUN_0043009d` | 4 | 60 | `Core Subsystem Logic` | `None` | `GlobalUnlock, OleLoadPicture, DeleteObject` | **High (Decompiled C Flow)** |
| `0x004301f8` | `FUN_004301f8` | 11 | 30 | `Helper Subroutine` | `None` | `ShowWindow, CreateWindowExW, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x0043028b` | `FUN_0043028b` | 3 | 138 | `Core Subsystem Logic` | `None` | `GetSystemMetrics, GetWindowRect, GetClientRect` | **High (Decompiled C Flow)** |
| `0x004305ae` | `FUN_004305ae` | 5 | 40 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430626` | `FUN_00430626` | 3 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430699` | `FUN_00430699` | 1 | 28 | `Helper Subroutine` | `None` | `IsWindowVisible, GetWindowRect, GetDlgCtrlID` | **Medium (Decompiled C Flow)** |
| `0x00430727` | `FUN_00430727` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430737` | `FUN_00430737` | 1 | 72 | `Core Subsystem Logic` | `None` | `LoadCursorW, SetCursor` | **High (Decompiled C Flow)** |
| `0x004308ef` | `FUN_004308ef` | 2 | 99 | `Core Subsystem Logic` | `None` | `SetTextColor, GetSysColorBrush, DrawFocusRect` | **High (Decompiled C Flow)** |
| `0x00430b0f` | `FUN_00430b0f` | 1 | 25 | `Helper Subroutine` | `None` | `CloseHandle, CreateProcessW` | **Medium (Decompiled C Flow)** |
| `0x00430b87` | `FUN_00430b87` | 3 | 27 | `Helper Subroutine` | `None` | `GetWindowRect, InvalidateRect, ScreenToClient` | **Medium (Decompiled C Flow)** |
| `0x00430c09` | `FUN_00430c09` | 2 | 21 | `Helper Subroutine` | `None` | `GetWindowLongW` | **Medium (Decompiled C Flow)** |
| `0x00430c46` | `FUN_00430c46` | 1 | 11 | `Helper Subroutine` | `None` | `GetClassLongW` | **Medium (Decompiled C Flow)** |
| `0x00430c57` | `FUN_00430c57` | 3 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430c7f` | `FUN_00430c7f` | 1 | 21 | `Helper Subroutine` | `"advapi32.dll", "RegDeleteKeyExW"` | `LoadLibraryA, GetProcAddress` | **Medium (Decompiled C Flow)** |
| `0x00430cb1` | `FUN_00430cb1` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430ccb` | `FUN_00430ccb` | 1 | 13 | `Helper Subroutine` | `None` | `FreeLibrary` | **Medium (Decompiled C Flow)** |
| `0x00430ce2` | `FUN_00430ce2` | 1 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430d1d` | `FUN_00430d1d` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430d31` | `FUN_00430d31` | 2 | 41 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430dc1` | `FUN_00430dc1` | 1 | 21 | `Helper Subroutine` | `"kernel32.dll", "GetSystemWow64DirectoryW"` | `LoadLibraryA, GetProcAddress` | **Medium (Decompiled C Flow)** |
| `0x00430df3` | `FUN_00430df3` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430e0d` | `FUN_00430e0d` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430e30` | `FUN_00430e30` | 1 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430e4d` | `FUN_00430e4d` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430e6a` | `FUN_00430e6a` | 1 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430e7b` | `FUN_00430e7b` | 1 | 21 | `Helper Subroutine` | `"GetModuleHandleExW", "kernel32.dll"` | `LoadLibraryA, GetProcAddress` | **Medium (Decompiled C Flow)** |
| `0x00430ead` | `FUN_00430ead` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430ec5` | `FUN_00430ec5` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430edf` | `FUN_00430edf` | 2 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430ef3` | `FUN_00430ef3` | 2 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00430f0e` | `FUN_00430f0e` | 4 | 128 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0043119b` | `FUN_0043119b` | 1 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004311fc` | `FUN_004311fc` | 2 | 24 | `Helper Subroutine` | `None` | `CoTaskMemAlloc` | **Medium (Decompiled C Flow)** |
| `0x00431245` | `FUN_00431245` | 2 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431285` | `FUN_00431285` | 2 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043129a` | `FUN_0043129a` | 1 | 21 | `Helper Subroutine` | `"ICMP.DLL", "IcmpSendEcho"` | `LoadLibraryA, GetProcAddress` | **Medium (Decompiled C Flow)** |
| `0x004312cc` | `FUN_004312cc` | 1 | 21 | `Helper Subroutine` | `"IcmpCloseHandle", "ICMP.DLL"` | `LoadLibraryA, GetProcAddress` | **Medium (Decompiled C Flow)** |
| `0x004312fe` | `FUN_004312fe` | 1 | 21 | `Helper Subroutine` | `"IcmpCreateFile", "ICMP.DLL"` | `LoadLibraryA, GetProcAddress` | **Medium (Decompiled C Flow)** |
| `0x00431330` | `FUN_00431330` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043134a` | `FUN_0043134a` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431364` | `FUN_00431364` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043137e` | `FUN_0043137e` | 3 | 23 | `Helper Subroutine` | `None` | `ClientToScreen, GetWindowRect` | **Medium (Decompiled C Flow)** |
| `0x004313ca` | `FUN_004313ca` | 4 | 91 | `Core Subsystem Logic` | `None` | `CreateCompatibleBitmap, CreateCompatibleDC, ReleaseDC` | **High (Decompiled C Flow)** |
| `0x0043156c` | `FUN_0043156c` | 4 | 41 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431613` | `FUN_00431613` | 4 | 60 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00431706` | `FUN_00431706` | 4 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431740` | `FUN_00431740` | 3 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431763` | `FUN_00431763` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043177e` | `FUN_0043177e` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431799` | `FUN_00431799` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004317b1` | `FUN_004317b1` | 2 | 33 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00431848` | `FUN_00431848` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431861` | `FUN_00431861` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431877` | `FUN_00431877` | 1 | 29 | `Helper Subroutine` | `None` | `InternetQueryOptionW` | **Medium (Decompiled C Flow)** |
| `0x004318eb` | `FUN_004318eb` | 1 | 20 | `Helper Subroutine` | `None` | `HttpQueryInfoW` | **Medium (Decompiled C Flow)** |
| `0x00431930` | `FUN_00431930` | 3 | 24 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00431995` | `FUN_00431995` | 1 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004319ac` | `FUN_004319ac` | 2 | 16 | `Helper Subroutine` | `None` | `WaitForSingleObject` | **Medium (Decompiled C Flow)** |
| `0x004319d2` | `FUN_004319d2` | 1 | 16 | `Helper Subroutine` | `None` | `SetEvent` | **Medium (Decompiled C Flow)** |
| `0x004319f5` | `FUN_004319f5` | 1 | 18 | `Helper Subroutine` | `None` | `CloseHandle, CreateEventW` | **Medium (Decompiled C Flow)** |
| `0x00431a2b` | `FUN_00431a2b` | 2 | 34 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431a86` | `FUN_00431a86` | 4 | 57 | `Core Subsystem Logic` | `"), iVar3 != 0)) {
        DVar4 = GetFileAttributesW(local_258.cFileName);
        BVar5 = SetFileAttributesW(local_258.cFileName,(DVar4 | param_2) & ~param_3);
        if (BVar5 == 0) {
          FindClose(pvVar2);
          return 0;
        }
        uVar6 = 1;
      }
      BVar5 = FindNextFileW(pvVar2,&local_258);
    } while (BVar5 != 0);
  }
  FindClose(pvVar2);
  if ((char)param_4 != '\0') {
    pvVar2 = FindFirstFileW(L", "), iVar3 != 0)) {
          SetCurrentDirectoryW(local_258.cFileName);
          cVar1 = FUN_00431a86(param_1,param_2,param_3,param_4);
          if (cVar1 == '\0') {
            FindClose(pvVar2);
            return 0;
          }
          SetCurrentDirectoryW(L", ");
      if ((iVar3 != 0) && (iVar3 = _wcscmp(local_258.cFileName,L"` | `FindNextFileW, SetCurrentDirectoryW, FindFirstFileW` | **High (Decompiled C Flow)** |
| `0x00431be8` | `FUN_00431be8` | 3 | 55 | `Core Subsystem Logic` | `"\\??\\%s"` | `CreateDirectoryW, RemoveDirectoryW, GetFullPathNameW` | **High (Decompiled C Flow)** |
| `0x00431d57` | `FUN_00431d57` | 4 | 13 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00431d7f` | `FUN_00431d7f` | 0 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431dad` | `FUN_00431dad` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431dc9` | `FUN_00431dc9` | 1 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431ddb` | `FUN_00431ddb` | 3 | 17 | `Helper Subroutine` | `None` | `CreateFileW, CloseHandle, SetFileTime` | **Medium (Decompiled C Flow)** |
| `0x00431e1f` | `FUN_00431e1f` | 1 | 14 | `Helper Subroutine` | `"aut"` | `GetTempPathW, GetTempFileNameW` | **Medium (Decompiled C Flow)** |
| `0x00431e58` | `FUN_00431e58` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431e71` | `FUN_00431e71` | 2 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431e9e` | `FUN_00431e9e` | 2 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00431ec8` | `FUN_00431ec8` | 1 | 49 | `Helper Subroutine` | `None` | `CONCAT44` | **Medium (Decompiled C Flow)** |
| `0x00431fbb` | `FUN_00431fbb` | 1 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432017` | `FUN_00432017` | 1 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043206e` | `FUN_0043206e` | 1 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004320a4` | `FUN_004320a4` | 2 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004320f8` | `FUN_004320f8` | 1 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043213d` | `FUN_0043213d` | 1 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004321a4` | `FUN_004321a4` | 2 | 27 | `Helper Subroutine` | `"EA06"` | `CONCAT31, CONCAT21, FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00432229` | `FUN_00432229` | 3 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432281` | `FUN_00432281` | 1 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004322cd` | `FUN_004322cd` | 1 | 51 | `Core Subsystem Logic` | `None` | `CONCAT44, SUB84` | **High (Decompiled C Flow)** |
| `0x004323c5` | `FUN_004323c5` | 2 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004323e1` | `FUN_004323e1` | 2 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432416` | `FUN_00432416` | 1 | 14 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00432447` | `FUN_00432447` | 1 | 47 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432508` | `FUN_00432508` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432520` | `FUN_00432520` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432538` | `FUN_00432538` | 2 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432559` | `FUN_00432559` | 1 | 18 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0043257b` | `FUN_0043257b` | 1 | 18 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0043259d` | `FUN_0043259d` | 1 | 18 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x004325be` | `FUN_004325be` | 1 | 18 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x004325e0` | `FUN_004325e0` | 3 | 25 | `Helper Subroutine` | `None` | `DuplicateHandle, GetCurrentProcess` | **Medium (Decompiled C Flow)** |
| `0x00432614` | `FUN_00432614` | 1 | 14 | `Helper Subroutine` | `None` | `CloseHandle` | **Medium (Decompiled C Flow)** |
| `0x00432631` | `FUN_00432631` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432651` | `FUN_00432651` | 1 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432664` | `FUN_00432664` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432684` | `FUN_00432684` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004326a4` | `FUN_004326a4` | 2 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004326ed` | `FUN_004326ed` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432704` | `FUN_00432704` | 1 | 24 | `Helper Subroutine` | `None` | `VariantClear` | **Medium (Decompiled C Flow)** |
| `0x00432770` | `FUN_00432770` | 4 | 19 | `Helper Subroutine` | `None` | `VariantCopy` | **Medium (Decompiled C Flow)** |
| `0x004327b5` | `FUN_004327b5` | 6 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432810` | `FUN_00432810` | 4 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043286f` | `FUN_0043286f` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043288e` | `FUN_0043288e` | 1 | 16 | `Helper Subroutine` | `None` | `InterlockedIncrement` | **Medium (Decompiled C Flow)** |
| `0x004328ae` | `FUN_004328ae` | 1 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004328ec` | `FUN_004328ec` | 3 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432929` | `FUN_00432929` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043293f` | `FUN_0043293f` | 1 | 21 | `Helper Subroutine` | `None` | `MultiByteToWideChar` | **Medium (Decompiled C Flow)** |
| `0x0043299a` | `FUN_0043299a` | 2 | 33 | `Helper Subroutine` | `None` | `MultiByteToWideChar` | **Medium (Decompiled C Flow)** |
| `0x00432a10` | `FUN_00432a10` | 4 | 78 | `Core Subsystem Logic` | `None` | `CONCAT31, GetLocalTime` | **High (Decompiled C Flow)** |
| `0x00432b92` | `FUN_00432b92` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432bc3` | `FUN_00432bc3` | 3 | 38 | `Helper Subroutine` | `None` | `CARRY4, CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00432c30` | `FUN_00432c30` | 2 | 49 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00432cc2` | `FUN_00432cc2` | 3 | 59 | `Core Subsystem Logic` | `None` | `CARRY4, CONCAT31` | **High (Decompiled C Flow)** |
| `0x00432d76` | `FUN_00432d76` | 2 | 39 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00432dfc` | `FUN_00432dfc` | 3 | 42 | `Helper Subroutine` | `"0123456789ABCDEF"` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432e88` | `FUN_00432e88` | 4 | 35 | `Helper Subroutine` | `"0123456789ABCDEF"` | `None` | **Medium (Decompiled C Flow)** |
| `0x00432ee9` | `FUN_00432ee9` | 3 | 50 | `Helper Subroutine` | `None` | `FID_conflict___iswspace_l` | **Medium (Decompiled C Flow)** |
| `0x00432fad` | `FUN_00432fad` | 4 | 23 | `Helper Subroutine` | `None` | `MonitorFromRect` | **Medium (Decompiled C Flow)** |
| `0x00432fee` | `FUN_00432fee` | 0 | 28 | `Helper Subroutine` | `None` | `GetLastError, OpenSCManagerW, UnlockServiceDatabase` | **Medium (Decompiled C Flow)** |
| `0x0043303f` | `FUN_0043303f` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043305f` | `FUN_0043305f` | 4 | 54 | `Core Subsystem Logic` | `",param_3);
  __swprintf(local_1c,L"` | `LoadResource, SizeofResource, CreateIconFromResourceEx` | **High (Decompiled C Flow)** |
| `0x004331a2` | `FUN_004331a2` | 1 | 44 | `Helper Subroutine` | `None` | `CONCAT44, Sleep, QueryPerformanceCounter` | **Medium (Decompiled C Flow)** |
| `0x00433244` | `FUN_00433244` | 3 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043326f` | `FUN_0043326f` | 6 | 69 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0043333c` | `FUN_0043333c` | 1 | 25 | `Helper Subroutine` | `");
  if (iVar1 == 0) {
    mouse_event(0x800,0,0,0x78,0);
    return CONCAT31((int3)((uint)extraout_EAX >> 8),1);
  }
  uVar2 = __wcsicmp(param_1,L"` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00433396` | `FUN_00433396` | 1 | 14 | `Helper Subroutine` | `None` | `SendMessageTimeoutW` | **Medium (Decompiled C Flow)** |
| `0x004333be` | `FUN_004333be` | 2 | 46 | `Helper Subroutine` | `"SeShutdownPrivilege"` | `InitiateSystemShutdownExW, GetLastError, AdjustTokenPrivileges` | **Medium (Decompiled C Flow)** |
| `0x00433493` | `FUN_00433493` | 2 | 51 | `Core Subsystem Logic` | `"0.0.0.0"` | `WSACleanup, WSAStartup, FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x00433584` | `FUN_00433584` | 2 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004335cd` | `FUN_004335cd` | 1 | 55 | `Core Subsystem Logic` | `None` | `CreateDirectoryW, GetLastError, GetFileAttributesW` | **High (Decompiled C Flow)** |
| `0x004336c5` | `FUN_004336c5` | 4 | 56 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00433784` | `FUN_00433784` | 5 | 56 | `Core Subsystem Logic` | `");
    pwVar1 = &local_210;
  }
  else {
    _wcscat(local_41c,L"` | `None` | **High (Decompiled C Flow)** |
| `0x00433908` | `FUN_00433908` | 2 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00433998` | `FUN_00433998` | 1 | 18 | `Helper Subroutine` | `None` | `CONCAT31, GetFileAttributesW` | **Medium (Decompiled C Flow)** |
| `0x004339b6` | `FUN_004339b6` | 1 | 23 | `Helper Subroutine` | `None` | `FindClose, FindFirstFileW, GetFileAttributesW` | **Medium (Decompiled C Flow)** |
| `0x004339fa` | `FUN_004339fa` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00433a13` | `FUN_00433a13` | 3 | 83 | `Core Subsystem Logic` | `");
    if (iVar3 == 0) {
      __swprintf(param_2,L", ");
    pwVar4 = _wcsstr(param_3,L", ");
      }
      else {
        local_10 = *local_c;
        FUN_00432e88(local_10,0,(int)(_Dest + 0x10),4);
        FUN_00432e88(local_10 >> 0x10,0,(int)(_Dest + 0x14),4);
      }
      _wcscat(_Dest,L"` | `CONCAT31, GetFileVersionInfoSizeW, VerQueryValueW` | **High (Decompiled C Flow)** |
| `0x00433c08` | `FUN_00433c08` | 3 | 35 | `Helper Subroutine` | `None` | `CONCAT31, SetFileTime, CreateFileW` | **Medium (Decompiled C Flow)** |
| `0x00433c6a` | `FUN_00433c6a` | 1 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00433c94` | `FUN_00433c94` | 2 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00433cda` | `FUN_00433cda` | 1 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00433d09` | `FUN_00433d09` | 1 | 19 | `Helper Subroutine` | `"#32770"` | `GetClassNameW` | **Medium (Decompiled C Flow)** |
| `0x00433d5f` | `FUN_00433d5f` | 1 | 31 | `Helper Subroutine` | `None` | `FID_conflict___iswdigit_l` | **Medium (Decompiled C Flow)** |
| `0x00433d9e` | `FUN_00433d9e` | 3 | 64 | `Core Subsystem Logic` | `None` | `CONCAT31, GetModuleBaseNameW, EnumProcesses` | **High (Decompiled C Flow)** |
| `0x00433ee0` | `FUN_00433ee0` | 3 | 47 | `Helper Subroutine` | `None` | `CONCAT31, Process32NextW, CreateToolhelp32Snapshot` | **Medium (Decompiled C Flow)** |
| `0x00433fce` | `FUN_00433fce` | 1 | 23 | `Helper Subroutine` | `None` | `GetWindowThreadProcessId, TerminateProcess, SendMessageTimeoutW` | **Medium (Decompiled C Flow)** |
| `0x00434034` | `FUN_00434034` | 2 | 33 | `Helper Subroutine` | `"%s (%d) : ==> %s: \n%s \n%s\n"` | `GetModuleHandleW, LoadStringW, FID_conflict__wprintf` | **Medium (Decompiled C Flow)** |
| `0x004340c3` | `FUN_004340c3` | 1 | 13 | `Helper Subroutine` | `None` | `FlushFileBuffers` | **Medium (Decompiled C Flow)** |
| `0x004340db` | `FUN_004340db` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004340f8` | `FUN_004340f8` | 1 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434137` | `FUN_00434137` | 2 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434179` | `FUN_00434179` | 3 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004341ba` | `FUN_004341ba` | 2 | 15 | `Helper Subroutine` | `None` | `DestroyIcon` | **Medium (Decompiled C Flow)** |
| `0x004341e6` | `FUN_004341e6` | 4 | 51 | `Core Subsystem Logic` | `"question", "stop", "info"` | `ExtractIconExW, LoadIconW` | **High (Decompiled C Flow)** |
| `0x004342dd` | `FUN_004342dd` | 4 | 23 | `Helper Subroutine` | `None` | `ReadProcessMemory` | **Medium (Decompiled C Flow)** |
| `0x00434319` | `FUN_00434319` | 4 | 23 | `Helper Subroutine` | `None` | `WriteProcessMemory` | **Medium (Decompiled C Flow)** |
| `0x00434355` | `FUN_00434355` | 2 | 25 | `Helper Subroutine` | `None` | `CloseHandle, VirtualFreeEx` | **Medium (Decompiled C Flow)** |
| `0x004343ad` | `FUN_004343ad` | 3 | 32 | `Helper Subroutine` | `None` | `GetWindowThreadProcessId, VirtualAllocEx, OpenProcess` | **Medium (Decompiled C Flow)** |
| `0x00434418` | `FUN_00434418` | 1 | 71 | `Core Subsystem Logic` | `"Shell_TrayWnd"` | `GetWindowThreadProcessId, ShowWindow, AttachThreadInput` | **High (Decompiled C Flow)** |
| `0x00434569` | `FUN_00434569` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434582` | `FUN_00434582` | 1 | 43 | `Helper Subroutine` | `None` | `CONCAT44, Sleep, QueryPerformanceCounter` | **Medium (Decompiled C Flow)** |
| `0x00434621` | `FUN_00434621` | 3 | 48 | `Helper Subroutine` | `None` | `GetWindowThreadProcessId, AttachThreadInput, GetForegroundWindow` | **Medium (Decompiled C Flow)** |
| `0x0043471d` | `FUN_0043471d` | 4 | 23 | `Helper Subroutine` | `None` | `SendInput` | **Medium (Decompiled C Flow)** |
| `0x0043477c` | `FUN_0043477c` | 1 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004347a9` | `FUN_004347a9` | 1 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004347d5` | `FUN_004347d5` | 3 | 30 | `Helper Subroutine` | `None` | `CONCAT31, MapVirtualKeyW, GetKeyState` | **Medium (Decompiled C Flow)** |
| `0x00434831` | `FUN_00434831` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434869` | `FUN_00434869` | 1 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043487c` | `FUN_0043487c` | 1 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043488e` | `FUN_0043488e` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004348aa` | `FUN_004348aa` | 1 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004348de` | `FUN_004348de` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434908` | `FUN_00434908` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043492f` | `FUN_0043492f` | 1 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434963` | `FUN_00434963` | 2 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004349d1` | `FUN_004349d1` | 1 | 22 | `Helper Subroutine` | `None` | `CONCAT31, FID_conflict___iswspace_l` | **Medium (Decompiled C Flow)** |
| `0x004349ff` | `FUN_004349ff` | 2 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434a13` | `FUN_00434a13` | 1 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434a40` | `FUN_00434a40` | 2 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434a5e` | `FUN_00434a5e` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434a8d` | `FUN_00434a8d` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434aa8` | `FUN_00434aa8` | 2 | 19 | `Helper Subroutine` | `None` | `FreeLibrary` | **Medium (Decompiled C Flow)** |
| `0x00434b02` | `FUN_00434b02` | 3 | 56 | `Core Subsystem Logic` | `"AU3_GetPluginDetails"` | `FreeLibrary, GetProcAddress, LoadLibraryA` | **High (Decompiled C Flow)** |
| `0x00434c09` | `FUN_00434c09` | 1 | 45 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434cc9` | `FUN_00434cc9` | 3 | 47 | `Helper Subroutine` | `"cdecl"` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434d99` | `FUN_00434d99` | 2 | 35 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434dda` | `FUN_00434dda` | 1 | 50 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00434ec4` | `FUN_00434ec4` | 2 | 55 | `Core Subsystem Logic` | `None` | `MultiByteToWideChar, SysAllocString, StringFromGUID2` | **High (Decompiled C Flow)** |
| `0x00434fd0` | `FUN_00434fd0` | 2 | 48 | `Helper Subroutine` | `None` | `MultiByteToWideChar, SysAllocString, StringFromGUID2` | **Medium (Decompiled C Flow)** |
| `0x004350c1` | `FUN_004350c1` | 1 | 18 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x004350fa` | `FUN_004350fa` | 1 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043513e` | `FUN_0043513e` | 1 | 20 | `Helper Subroutine` | `None` | `VariantCopy, VariantInit` | **Medium (Decompiled C Flow)** |
| `0x00435175` | `FUN_00435175` | 1 | 28 | `Helper Subroutine` | `None` | `SysStringLen` | **Medium (Decompiled C Flow)** |
| `0x004351cc` | `FUN_004351cc` | 1 | 23 | `Helper Subroutine` | `None` | `SysStringLen, WideCharToMultiByte` | **Medium (Decompiled C Flow)** |
| `0x00435215` | `FUN_00435215` | 1 | 49 | `Helper Subroutine` | `None` | `SafeArrayUnaccessData, SafeArrayAccessData, CLSIDFromString` | **Medium (Decompiled C Flow)** |
| `0x004352c2` | `FUN_004352c2` | 7 | 67 | `Core Subsystem Logic` | `None` | `SafeArrayUnaccessData, VariantClear, SafeArrayAccessData` | **High (Decompiled C Flow)** |
| `0x00435403` | `FUN_00435403` | 1 | 16 | `Helper Subroutine` | `None` | `VariantClear` | **Medium (Decompiled C Flow)** |
| `0x0043542d` | `FUN_0043542d` | 1 | 16 | `Helper Subroutine` | `None` | `VariantClear` | **Medium (Decompiled C Flow)** |
| `0x00435457` | `FUN_00435457` | 1 | 16 | `Helper Subroutine` | `None` | `VariantClear` | **Medium (Decompiled C Flow)** |
| `0x00435481` | `FUN_00435481` | 3 | 33 | `Helper Subroutine` | `None` | `VariantChangeType, VariantCopy` | **Medium (Decompiled C Flow)** |
| `0x0043550b` | `FUN_0043550b` | 3 | 47 | `Helper Subroutine` | `None` | `VariantCopyInd, VariantClear` | **Medium (Decompiled C Flow)** |
| `0x00435648` | `FUN_00435648` | 6 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435680` | `FUN_00435680` | 4 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004356b0` | `FUN_004356b0` | 2 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004356d8` | `FUN_004356d8` | 3 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435703` | `FUN_00435703` | 1 | 20 | `Helper Subroutine` | `None` | `InterlockedIncrement` | **Medium (Decompiled C Flow)** |
| `0x00435732` | `FUN_00435732` | 1 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004357b7` | `FUN_004357b7` | 4 | 78 | `Core Subsystem Logic` | `None` | `GetWindowRect, InvalidateRect, MoveWindow` | **High (Decompiled C Flow)** |
| `0x00435976` | `FUN_00435976` | 1 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043599e` | `FUN_0043599e` | 2 | 45 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435a50` | `FUN_00435a50` | 3 | 42 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00435b09` | `FUN_00435b09` | 3 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435b59` | `FUN_00435b59` | 1 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435bb6` | `FUN_00435bb6` | 3 | 63 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00435ce8` | `FUN_00435ce8` | 1 | 13 | `Helper Subroutine` | `None` | `InvalidateRect` | **Medium (Decompiled C Flow)** |
| `0x00435d0a` | `FUN_00435d0a` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435d35` | `FUN_00435d35` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435d6a` | `FUN_00435d6a` | 5 | 12 | `Helper Subroutine` | `None` | `MkParseDisplayName` | **Medium (Decompiled C Flow)** |
| `0x00435d87` | `FUN_00435d87` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435da2` | `FUN_00435da2` | 2 | 41 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435e6c` | `FUN_00435e6c` | 1 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435eb0` | `FUN_00435eb0` | 4 | 16 | `Helper Subroutine` | `None` | `OleSetMenuDescriptor, GetMenu` | **Medium (Decompiled C Flow)** |
| `0x00435eec` | `FUN_00435eec` | 2 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435f33` | `FUN_00435f33` | 2 | 15 | `Helper Subroutine` | `None` | `GetClientRect` | **Medium (Decompiled C Flow)** |
| `0x00435f58` | `FUN_00435f58` | 2 | 14 | `Helper Subroutine` | `None` | `GetClientRect, CopyRect` | **Medium (Decompiled C Flow)** |
| `0x00435f85` | `FUN_00435f85` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00435f99` | `FUN_00435f99` | 2 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00436045` | `FUN_00436045` | 2 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004360f5` | `FUN_004360f5` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00436108` | `FUN_00436108` | 6 | 21 | `Helper Subroutine` | `None` | `CopyRect` | **Medium (Decompiled C Flow)** |
| `0x00436177` | `FUN_00436177` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043618a` | `FUN_0043618a` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043619d` | `FUN_0043619d` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004361b0` | `FUN_004361b0` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004361e0` | `FUN_004361e0` | 1 | 13 | `Helper Subroutine` | `None` | `InvalidateRect` | **Medium (Decompiled C Flow)** |
| `0x00436204` | `FUN_00436204` | 2 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00436221` | `FUN_00436221` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00436233` | `FUN_00436233` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00436244` | `FUN_00436244` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00436255` | `FUN_00436255` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00436270` | `FUN_00436270` | 1 | 11 | `Helper Subroutine` | `None` | `RaiseException` | **Medium (Decompiled C Flow)** |
| `0x00436299` | `FUN_00436299` | 2 | 32 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00436327` | `FUN_00436327` | 1 | 13 | `Helper Subroutine` | `None` | `SendMessageTimeoutW` | **Medium (Decompiled C Flow)** |
| `0x0043634e` | `FUN_0043634e` | 1 | 13 | `Helper Subroutine` | `None` | `IsWindowEnabled` | **Medium (Decompiled C Flow)** |
| `0x00436366` | `FUN_00436366` | 1 | 13 | `Helper Subroutine` | `None` | `IsWindowVisible` | **Medium (Decompiled C Flow)** |
| `0x0043637e` | `FUN_0043637e` | 1 | 13 | `Helper Subroutine` | `None` | `CONCAT31, PostMessageW` | **Medium (Decompiled C Flow)** |
| `0x00436399` | `FUN_00436399` | 2 | 17 | `Helper Subroutine` | `None` | `CONCAT31, ShowWindow` | **Medium (Decompiled C Flow)** |
| `0x004363c7` | `FUN_004363c7` | 2 | 17 | `Helper Subroutine` | `None` | `CONCAT31, EnableWindow` | **Medium (Decompiled C Flow)** |
| `0x004363f5` | `FUN_004363f5` | 5 | 13 | `Helper Subroutine` | `None` | `MoveWindow` | **Medium (Decompiled C Flow)** |
| `0x0043641f` | `FUN_0043641f` | 1 | 18 | `Helper Subroutine` | `None` | `GetParent, GetWindowLongW` | **Medium (Decompiled C Flow)** |
| `0x00436446` | `FUN_00436446` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00436458` | `FUN_00436458` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043646a` | `FUN_0043646a` | 2 | 28 | `Helper Subroutine` | `None` | `GetWindowThreadProcessId, AttachThreadInput, GetCurrentThreadId` | **Medium (Decompiled C Flow)** |
| `0x004364b5` | `FUN_004364b5` | 2 | 20 | `Helper Subroutine` | `None` | `GetParent` | **Medium (Decompiled C Flow)** |
| `0x004364e6` | `FUN_004364e6` | 2 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00436508` | `FUN_00436508` | 1 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043652f` | `FUN_0043652f` | 2 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00436565` | `FUN_00436565` | 1 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00436577` | `FUN_00436577` | 2 | 15 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x0043659e` | `FUN_0043659e` | 3 | 69 | `Core Subsystem Logic` | `None` | `CONCAT31, SendMessageW` | **High (Decompiled C Flow)** |
| `0x00436748` | `FUN_00436748` | 1 | 11 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00436764` | `FUN_00436764` | 2 | 13 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00436787` | `FUN_00436787` | 1 | 11 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x004367a3` | `FUN_004367a3` | 1 | 14 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x004367cf` | `FUN_004367cf` | 1 | 11 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x004367eb` | `FUN_004367eb` | 4 | 34 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x004368a0` | `FUN_004368a0` | 2 | 30 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00436934` | `FUN_00436934` | 2 | 14 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00436958` | `FUN_00436958` | 2 | 14 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x0043697b` | `FUN_0043697b` | 1 | 13 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x0043699d` | `FUN_0043699d` | 2 | 23 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x004369d7` | `FUN_004369d7` | 2 | 18 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00436a0b` | `FUN_00436a0b` | 5 | 58 | `Core Subsystem Logic` | `None` | `CONCAT31, Sleep, GetWindowRect` | **High (Decompiled C Flow)** |
| `0x00436b19` | `FUN_00436b19` | 0 | 18 | `Helper Subroutine` | `None` | `HeapAlloc, GetProcessHeap` | **Medium (Decompiled C Flow)** |
| `0x00436b2b` | `FUN_00436b2b` | 3 | 28 | `Helper Subroutine` | `None` | `GetLastError, GetTokenInformation` | **Medium (Decompiled C Flow)** |
| `0x00436b91` | `FUN_00436b91` | 1 | 16 | `Helper Subroutine` | `None` | `HeapAlloc, GetProcessHeap` | **Medium (Decompiled C Flow)** |
| `0x00436ba9` | `FUN_00436ba9` | 1 | 18 | `Helper Subroutine` | `None` | `HeapFree, GetProcessHeap` | **Medium (Decompiled C Flow)** |
| `0x00436bc5` | `FUN_00436bc5` | 3 | 28 | `Helper Subroutine` | `None` | `GetLastError, GetTokenInformation` | **Medium (Decompiled C Flow)** |
| `0x00436c2b` | `FUN_00436c2b` | 1 | 15 | `Helper Subroutine` | `None` | `WaitForSingleObject, CloseHandle, UnloadUserProfile` | **Medium (Decompiled C Flow)** |
| `0x00436c6e` | `FUN_00436c6e` | 3 | 38 | `Helper Subroutine` | `None` | `DuplicateHandle, CreateThread, GetCurrentProcess` | **Medium (Decompiled C Flow)** |
| `0x00436cd7` | `FUN_00436cd7` | 5 | 13 | `Helper Subroutine` | `None` | `LogonUserW` | **Medium (Decompiled C Flow)** |
| `0x00436d09` | `FUN_00436d09` | 2 | 50 | `Helper Subroutine` | `None` | `CopySid, GetLengthSid` | **Medium (Decompiled C Flow)** |
| `0x00436dbf` | `FUN_00436dbf` | 2 | 21 | `Helper Subroutine` | `None` | `InitializeAcl` | **Medium (Decompiled C Flow)** |
| `0x00436df7` | `FUN_00436df7` | 2 | 21 | `Helper Subroutine` | `None` | `InitializeSecurityDescriptor` | **Medium (Decompiled C Flow)** |
| `0x00436e2b` | `FUN_00436e2b` | 4 | 28 | `Helper Subroutine` | `None` | `GetUserObjectSecurity, GetLastError` | **Medium (Decompiled C Flow)** |
| `0x00436e94` | `FUN_00436e94` | 9 | 53 | `Core Subsystem Logic` | `None` | `DestroyEnvironmentBlock, CreateProcessWithLogonW, CreateEnvironmentBlock` | **High (Decompiled C Flow)** |
| `0x00436f47` | `FUN_00436f47` | 0 | 92 | `Core Subsystem Logic` | `"SeIncreaseQuotaPrivilege", "SeAssignPrimaryTokenPrivilege"` | `CloseHandle, OpenThreadToken, GetCurrentProcess` | **High (Decompiled C Flow)** |
| `0x00437063` | `FUN_00437063` | 2 | 12 | `Helper Subroutine` | `None` | `VariantCopy, VariantClear` | **Medium (Decompiled C Flow)** |
| `0x00437081` | `FUN_00437081` | 1 | 13 | `Helper Subroutine` | `None` | `VariantClear` | **Medium (Decompiled C Flow)** |
| `0x00437095` | `FUN_00437095` | 1 | 13 | `Helper Subroutine` | `None` | `VariantInit` | **Medium (Decompiled C Flow)** |
| `0x004370ab` | `FUN_004370ab` | 2 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004370df` | `FUN_004370df` | 1 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004370f4` | `FUN_004370f4` | 1 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00437144` | `FUN_00437144` | 4 | 61 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00437262` | `FUN_00437262` | 10 | 5,071 | `Core Subsystem Logic` | `None` | `CONCAT31, SBORROW4, FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x0043ef7e` | `FUN_0043ef7e` | 2 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0043efd3` | `FUN_0043efd3` | 3 | 64 | `Core Subsystem Logic` | `None` | `CONCAT11` | **High (Decompiled C Flow)** |
| `0x0043f0d4` | `FUN_0043f0d4` | 3 | 75 | `Core Subsystem Logic` | `None` | `CONCAT11` | **High (Decompiled C Flow)** |
| `0x0043f203` | `FUN_0043f203` | 4 | 61 | `Core Subsystem Logic` | `None` | `CONCAT11` | **High (Decompiled C Flow)** |
| `0x0043f2e8` | `FUN_0043f2e8` | 5 | 550 | `Core Subsystem Logic` | `"{0,"` | `None` | **High (Decompiled C Flow)** |
| `0x0043feb0` | `FUN_0043feb0` | 5 | 40 | `Helper Subroutine` | `None` | `CONCAT11` | **Medium (Decompiled C Flow)** |
| `0x0043ff53` | `FUN_0043ff53` | 4 | 175 | `Core Subsystem Logic` | `None` | `CONCAT11` | **High (Decompiled C Flow)** |
| `0x00440293` | `FUN_00440293` | 5 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00440306` | `FUN_00440306` | 4 | 12 | `Helper Subroutine` | `None` | `DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x00440338` | `FUN_00440338` | 4 | 12 | `Helper Subroutine` | `None` | `DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x0044036a` | `FUN_0044036a` | 4 | 20 | `Helper Subroutine` | `None` | `DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x004403ae` | `FUN_004403ae` | 1 | 52 | `Core Subsystem Logic` | `None` | `GetWindowRect, MoveWindow` | **High (Decompiled C Flow)** |
| `0x0044048e` | `FUN_0044048e` | 4 | 15 | `Helper Subroutine` | `None` | `DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x004404e8` | `FUN_004404e8` | 4 | 117 | `Core Subsystem Logic` | `None` | `ShowWindow, GetSystemMetrics, CONCAT22` | **High (Decompiled C Flow)** |
| `0x00440826` | `FUN_00440826` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00440847` | `FUN_00440847` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00440863` | `FUN_00440863` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00440880` | `FUN_00440880` | 9 | 59 | `Core Subsystem Logic` | `"static"` | `None` | **High (Decompiled C Flow)** |
| `0x0044097a` | `FUN_0044097a` | 5 | 41 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00440a0d` | `FUN_00440a0d` | 3 | 57 | `Core Subsystem Logic` | `None` | `ShowWindow, EnableWindow, SendMessageW` | **High (Decompiled C Flow)** |
| `0x00440b82` | `FUN_00440b82` | 4 | 42 | `Helper Subroutine` | `None` | `CONCAT31, InvalidateRect, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00440c49` | `FUN_00440c49` | 10 | 54 | `Core Subsystem Logic` | `"SysAnimate32"` | `CONCAT31, DestroyWindow, SendMessageW` | **High (Decompiled C Flow)** |
| `0x00440d32` | `FUN_00440d32` | 5 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00440d98` | `FUN_00440d98` | 2 | 49 | `Helper Subroutine` | `None` | `GetWindowLongW, SetWindowLongW, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00440edc` | `FUN_00440edc` | 2 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00440f0a` | `FUN_00440f0a` | 8 | 36 | `Helper Subroutine` | `None` | `ReleaseDC, DeleteObject, GetDC` | **Medium (Decompiled C Flow)** |
| `0x00441018` | `FUN_00441018` | 3 | 24 | `Helper Subroutine` | `None` | `GetWindowLongW` | **Medium (Decompiled C Flow)** |
| `0x00441078` | `FUN_00441078` | 3 | 44 | `Helper Subroutine` | `None` | `GetSystemMetrics, SetWindowLongW, GetWindowLongW` | **Medium (Decompiled C Flow)** |
| `0x00441165` | `FUN_00441165` | 2 | 79 | `Core Subsystem Logic` | `None` | `EnableWindow, ShowWindow, LockWindowUpdate` | **High (Decompiled C Flow)** |
| `0x00441361` | `FUN_00441361` | 1 | 17 | `Helper Subroutine` | `None` | `DestroyWindow` | **Medium (Decompiled C Flow)** |
| `0x004413aa` | `FUN_004413aa` | 1 | 32 | `Helper Subroutine` | `None` | `DeleteObject` | **Medium (Decompiled C Flow)** |
| `0x00441432` | `FUN_00441432` | 2 | 37 | `Helper Subroutine` | `None` | `CreateSolidBrush` | **Medium (Decompiled C Flow)** |
| `0x004414b5` | `FUN_004414b5` | 2 | 22 | `Helper Subroutine` | `None` | `SetBkColor, GetSysColor` | **Medium (Decompiled C Flow)** |
| `0x004414f4` | `FUN_004414f4` | 3 | 21 | `Helper Subroutine` | `None` | `PostMessageW` | **Medium (Decompiled C Flow)** |
| `0x00441544` | `FUN_00441544` | 3 | 35 | `Helper Subroutine` | `None` | `CreateAcceleratorTableW, GetForegroundWindow, DestroyAcceleratorTable` | **Medium (Decompiled C Flow)** |
| `0x004415d1` | `FUN_004415d1` | 2 | 31 | `Helper Subroutine` | `None` | `PostMessageW` | **Medium (Decompiled C Flow)** |
| `0x00441672` | `FUN_00441672` | 3 | 71 | `Core Subsystem Logic` | `None` | `GetWindowRect, MessageBeep, ClientToScreen` | **High (Decompiled C Flow)** |
| `0x004417bf` | `FUN_004417bf` | 2 | 135 | `Core Subsystem Logic` | `None` | `GetSysColorBrush, SetTextColor, CreateSolidBrush` | **High (Decompiled C Flow)** |
| `0x00441af5` | `FUN_00441af5` | 4 | 34 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00441b7c` | `FUN_00441b7c` | 2 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441c58` | `FUN_00441c58` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441c7b` | `FUN_00441c7b` | 2 | 64 | `Script / Win32 Host Logic` | `None` | `CONCAT31, RegOpenKeyExW, RegCloseKey` | **High (Verified Logic)** |
| `0x00441da2` | `FUN_00441da2` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441db4` | `FUN_00441db4` | 2 | 50 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441e23` | `FUN_00441e23` | 1 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441e49` | `FUN_00441e49` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441e6a` | `FUN_00441e6a` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441e8d` | `FUN_00441e8d` | 2 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441eba` | `FUN_00441eba` | 3 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441f1e` | `FUN_00441f1e` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441f49` | `FUN_00441f49` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441f6c` | `FUN_00441f6c` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441f8f` | `FUN_00441f8f` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441fb2` | `FUN_00441fb2` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00441fd6` | `FUN_00441fd6` | 5 | 48 | `Helper Subroutine` | `None` | `GetWindowRect, GetForegroundWindow, GetDesktopWindow` | **Medium (Decompiled C Flow)** |
| `0x004420f6` | `FUN_004420f6` | 2 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442140` | `FUN_00442140` | 3 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004421ab` | `FUN_004421ab` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004421bd` | `FUN_004421bd` | 2 | 44 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442253` | `FUN_00442253` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442272` | `FUN_00442272` | 1 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004422ae` | `FUN_004422ae` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004422cb` | `FUN_004422cb` | 4 | 19 | `Helper Subroutine` | `None` | `CONCAT31, GetLastError` | **Medium (Decompiled C Flow)** |
| `0x004422fe` | `FUN_004422fe` | 2 | 51 | `Core Subsystem Logic` | `None` | `CARRY4, InternetQueryDataAvailable, InternetReadFile` | **High (Decompiled C Flow)** |
| `0x004423da` | `FUN_004423da` | 2 | 52 | `Core Subsystem Logic` | `None` | `CONCAT31, CARRY4, InternetReadFile` | **High (Decompiled C Flow)** |
| `0x004424f3` | `FUN_004424f3` | 2 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442516` | `FUN_00442516` | 3 | 25 | `Helper Subroutine` | `None` | `InternetSetOptionW` | **Medium (Decompiled C Flow)** |
| `0x0044256c` | `FUN_0044256c` | 2 | 52 | `Core Subsystem Logic` | `"<local>"` | `CONCAT31, InternetOpenW, InternetSetOptionW` | **High (Decompiled C Flow)** |
| `0x0044260e` | `FUN_0044260e` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442651` | `FUN_00442651` | 1 | 15 | `Helper Subroutine` | `None` | `InternetCloseHandle` | **Medium (Decompiled C Flow)** |
| `0x0044268e` | `FUN_0044268e` | 1 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004426a9` | `FUN_004426a9` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004426bb` | `FUN_004426bb` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004426cd` | `FUN_004426cd` | 7 | 103 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00442886` | `FUN_00442886` | 4 | 56 | `Core Subsystem Logic` | `",&local_25c);
    if (pvVar2 != (HANDLE)0xffffffff) {
      do {
        if (((((byte)local_25c.dwFileAttributes & 0x10) != 0) &&
            (iVar3 = _wcscmp(local_25c.cFileName,L", "), iVar3 != 0)) {
          SetCurrentDirectoryW(local_25c.cFileName);
          cVar1 = FUN_00442886(param_1,param_2,param_3,param_4);
          if (cVar1 == '\0') {
            FindClose(pvVar2);
            return 0;
          }
          SetCurrentDirectoryW(L", "), iVar3 != 0)) {
        uVar4 = FUN_00433c08(local_25c.cFileName,param_2,param_3);
        if ((char)uVar4 == '\0') {
          FindClose(pvVar2);
          return 0;
        }
        uVar6 = 1;
      }
      BVar5 = FindNextFileW(pvVar2,&local_25c);
    } while (BVar5 != 0);
  }
  FindClose(pvVar2);
  if ((char)param_4 != '\0') {
    pvVar2 = FindFirstFileW(L"` | `FindNextFileW, SetCurrentDirectoryW, FindFirstFileW` | **High (Decompiled C Flow)** |
| `0x004429ef` | `FUN_004429ef` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442a01` | `FUN_00442a01` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442a17` | `FUN_00442a17` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442a34` | `FUN_00442a34` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442a55` | `FUN_00442a55` | 2 | 10 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442a67` | `FUN_00442a67` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442a83` | `FUN_00442a83` | 1 | 41 | `Helper Subroutine` | `None` | `TranslateMessage, PeekMessageW, DispatchMessageW` | **Medium (Decompiled C Flow)** |
| `0x00442b7b` | `FUN_00442b7b` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442b97` | `FUN_00442b97` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442bb4` | `FUN_00442bb4` | 2 | 34 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00442c29` | `FUN_00442c29` | 1 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442c5a` | `FUN_00442c5a` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442caf` | `FUN_00442caf` | 2 | 38 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442d48` | `FUN_00442d48` | 1 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442e0c` | `FUN_00442e0c` | 0 | 42 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442ee0` | `FUN_00442ee0` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442f10` | `FUN_00442f10` | 2 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442f36` | `FUN_00442f36` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00442f4c` | `FUN_00442f4c` | 1 | 54 | `Core Subsystem Logic` | `None` | `CONCAT22, CONCAT31` | **High (Decompiled C Flow)** |
| `0x00442fec` | `FUN_00442fec` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443006` | `FUN_00443006` | 1 | 44 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443106` | `FUN_00443106` | 1 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044318e` | `FUN_0044318e` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004431ad` | `FUN_004431ad` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004431cb` | `FUN_004431cb` | 2 | 25 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00443206` | `FUN_00443206` | 1 | 24 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00443234` | `FUN_00443234` | 1 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443260` | `FUN_00443260` | 2 | 18 | `Helper Subroutine` | `None` | `InterlockedExchange, InitializeCriticalSectionAndSpinCount` | **Medium (Decompiled C Flow)** |
| `0x004432c0` | `FUN_004432c0` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004432e1` | `FUN_004432e1` | 5 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044334f` | `FUN_0044334f` | 3 | 51 | `Core Subsystem Logic` | `"nul"` | `GetStdHandle, CreatePipe, CreateFileW` | **High (Decompiled C Flow)** |
| `0x00443442` | `FUN_00443442` | 5 | 51 | `Core Subsystem Logic` | `"nul"` | `GetStdHandle, CreatePipe, CreateFileW` | **High (Decompiled C Flow)** |
| `0x00443537` | `FUN_00443537` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443561` | `FUN_00443561` | 3 | 28 | `Helper Subroutine` | `None` | `WriteFile` | **Medium (Decompiled C Flow)** |
| `0x004435b9` | `FUN_004435b9` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004435d1` | `FUN_004435d1` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443607` | `FUN_00443607` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044363d` | `FUN_0044363d` | 2 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004436d6` | `FUN_004436d6` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004436f8` | `FUN_004436f8` | 3 | 27 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00443758` | `FUN_00443758` | 2 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004437bd` | `FUN_004437bd` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004437e8` | `FUN_004437e8` | 1 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443833` | `FUN_00443833` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443845` | `FUN_00443845` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443857` | `FUN_00443857` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443869` | `FUN_00443869` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044387b` | `FUN_0044387b` | 0 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044389a` | `FUN_0044389a` | 3 | 49 | `Helper Subroutine` | `"\r\n"` | `GetTextExtentPoint32W` | **Medium (Decompiled C Flow)** |
| `0x0044395e` | `FUN_0044395e` | 1 | 24 | `Helper Subroutine` | `None` | `EnumResourceNamesW, LoadImageW` | **Medium (Decompiled C Flow)** |
| `0x004439c1` | `FUN_004439c1` | 2 | 28 | `Helper Subroutine` | `None` | `GetWindowThreadProcessId, AttachThreadInput, GetCurrentThreadId` | **Medium (Decompiled C Flow)** |
| `0x004439fb` | `FUN_004439fb` | 2 | 21 | `Helper Subroutine` | `None` | `GetClassNameW` | **Medium (Decompiled C Flow)** |
| `0x00443a61` | `FUN_00443a61` | 1 | 14 | `Helper Subroutine` | `None` | `EnumChildWindows` | **Medium (Decompiled C Flow)** |
| `0x00443a87` | `FUN_00443a87` | 2 | 36 | `Helper Subroutine` | `None` | `IsWindowVisible, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00443b32` | `FUN_00443b32` | 2 | 15 | `Helper Subroutine` | `None` | `EnumChildWindows` | **Medium (Decompiled C Flow)** |
| `0x00443b61` | `FUN_00443b61` | 1 | 45 | `Helper Subroutine` | `"BUTTON"` | `SetActiveWindow, Sleep, EnumThreadWindows` | **Medium (Decompiled C Flow)** |
| `0x00443c87` | `FUN_00443c87` | 5 | 34 | `Helper Subroutine` | `None` | `GetCurrentThreadId, WaitForSingleObject, MessageBoxW` | **Medium (Decompiled C Flow)** |
| `0x00443d19` | `FUN_00443d19` | 3 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443d61` | `FUN_00443d61` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443d73` | `FUN_00443d73` | 1 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443db4` | `FUN_00443db4` | 1 | 23 | `Helper Subroutine` | `None` | `SetFilePointerEx` | **Medium (Decompiled C Flow)** |
| `0x00443df9` | `FUN_00443df9` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443e19` | `FUN_00443e19` | 1 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443e36` | `FUN_00443e36` | 3 | 21 | `Helper Subroutine` | `None` | `WriteFile, CARRY4` | **Medium (Decompiled C Flow)** |
| `0x00443e69` | `FUN_00443e69` | 3 | 27 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00443ec4` | `FUN_00443ec4` | 3 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443ee5` | `FUN_00443ee5` | 4 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443f0a` | `FUN_00443f0a` | 2 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443f76` | `FUN_00443f76` | 2 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443f9b` | `FUN_00443f9b` | 2 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443fbe` | `FUN_00443fbe` | 3 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00443fdf` | `FUN_00443fdf` | 1 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00444006` | `FUN_00444006` | 2 | 39 | `Helper Subroutine` | `None` | `GetMenuItemInfoW` | **Medium (Decompiled C Flow)** |
| `0x004440e0` | `FUN_004440e0` | 3 | 62 | `Core Subsystem Logic` | `None` | `GetMenuItemInfoW` | **High (Decompiled C Flow)** |
| `0x0044420e` | `FUN_0044420e` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044422d` | `FUN_0044422d` | 2 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044429f` | `FUN_0044429f` | 1 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00444310` | `FUN_00444310` | 1 | 33 | `Helper Subroutine` | `None` | `GetForegroundWindow, IsWindow` | **Medium (Decompiled C Flow)** |
| `0x00444362` | `FUN_00444362` | 2 | 48 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x004443fc` | `FUN_004443fc` | 2 | 96 | `Core Subsystem Logic` | `None` | `GetParent, SetKeyboardState, GetKeyboardState` | **High (Decompiled C Flow)** |
| `0x004445f4` | `FUN_004445f4` | 2 | 94 | `Core Subsystem Logic` | `None` | `GetParent, SetKeyboardState, GetKeyboardState` | **High (Decompiled C Flow)** |
| `0x004447e0` | `FUN_004447e0` | 2 | 77 | `Core Subsystem Logic` | `None` | `GetAsyncKeyState, GetKeyboardState, GetKeyState` | **High (Decompiled C Flow)** |
| `0x00444980` | `FUN_00444980` | 1 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00444a4e` | `FUN_00444a4e` | 1 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00444a7e` | `FUN_00444a7e` | 1 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00444abd` | `FUN_00444abd` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00444ad7` | `FUN_00444ad7` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00444af8` | `FUN_00444af8` | 2 | 31 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00444b5f` | `FUN_00444b5f` | 1 | 33 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00444bbb` | `FUN_00444bbb` | 1 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00444bfc` | `FUN_00444bfc` | 3 | 102 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00444d96` | `FUN_00444d96` | 1 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00444dd6` | `FUN_00444dd6` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00444df3` | `FUN_00444df3` | 2 | 34 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00444e90` | `FUN_00444e90` | 2 | 22 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00444ed6` | `FUN_00444ed6` | 1 | 24 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00444f21` | `FUN_00444f21` | 3 | 35 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00444f80` | `FUN_00444f80` | 3 | 32 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00444fd2` | `FUN_00444fd2` | 2 | 290 | `Core Subsystem Logic` | `"InterfaceDispatch", "AddRef", "Release"` | `None` | **High (Decompiled C Flow)** |
| `0x004455ed` | `FUN_004455ed` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044560a` | `FUN_0044560a` | 1 | 29 | `Helper Subroutine` | `None` | `InterlockedDecrement` | **Medium (Decompiled C Flow)** |
| `0x00445643` | `FUN_00445643` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00445660` | `FUN_00445660` | 1 | 69 | `Core Subsystem Logic` | `None` | `DestroyWindow, IsWindow, OleSetContainedObject` | **High (Decompiled C Flow)** |
| `0x004457c1` | `FUN_004457c1` | 1 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004457df` | `FUN_004457df` | 2 | 42 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00445870` | `FUN_00445870` | 2 | 42 | `Helper Subroutine` | `None` | `IsWindowVisible, SendMessageW, CharUpperBuffW` | **Medium (Decompiled C Flow)** |
| `0x00445934` | `FUN_00445934` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00445948` | `FUN_00445948` | 2 | 22 | `Helper Subroutine` | `None` | `EnumChildWindows` | **Medium (Decompiled C Flow)** |
| `0x0044599e` | `FUN_0044599e` | 2 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004459fb` | `FUN_004459fb` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00445a11` | `FUN_00445a11` | 3 | 30 | `Helper Subroutine` | `None` | `CONCAT31, GetParent, InvalidateRect` | **Medium (Decompiled C Flow)** |
| `0x00445a61` | `FUN_00445a61` | 1 | 20 | `Helper Subroutine` | `None` | `GetWindowLongW` | **Medium (Decompiled C Flow)** |
| `0x00445aa7` | `FUN_00445aa7` | 2 | 28 | `Helper Subroutine` | `None` | `GetWindowThreadProcessId, AttachThreadInput, GetCurrentThreadId` | **Medium (Decompiled C Flow)** |
| `0x00445ae0` | `FUN_00445ae0` | 2 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00445b19` | `FUN_00445b19` | 2 | 25 | `Helper Subroutine` | `None` | `GetClassNameW, GetFocus` | **Medium (Decompiled C Flow)** |
| `0x00445b98` | `FUN_00445b98` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00445bac` | `FUN_00445bac` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00445bc3` | `FUN_00445bc3` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00445be4` | `FUN_00445be4` | 2 | 45 | `Helper Subroutine` | `"largeicons", "list", "details"` | `GetClassNameW, CONCAT31, GetParent` | **Medium (Decompiled C Flow)** |
| `0x00445cb9` | `FUN_00445cb9` | 3 | 46 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00445db6` | `FUN_00445db6` | 1 | 25 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00445dfe` | `FUN_00445dfe` | 2 | 13 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00445e20` | `FUN_00445e20` | 2 | 22 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00445e52` | `FUN_00445e52` | 2 | 39 | `Helper Subroutine` | `None` | `CONCAT31, Sleep, MapVirtualKeyW` | **Medium (Decompiled C Flow)** |
| `0x00445f03` | `FUN_00445f03` | 1 | 15 | `Helper Subroutine` | `None` | `SetFocus` | **Medium (Decompiled C Flow)** |
| `0x00445f35` | `FUN_00445f35` | 3 | 104 | `Core Subsystem Logic` | `None` | `GetAclInformation, AddAce, GetAce` | **High (Decompiled C Flow)** |
| `0x00446124` | `FUN_00446124` | 3 | 104 | `Core Subsystem Logic` | `None` | `GetAclInformation, AddAce, GetAce` | **High (Decompiled C Flow)** |
| `0x00446313` | `FUN_00446313` | 9 | 122 | `Core Subsystem Logic` | `"winsta0", "winsta0\\default", "default"` | `CloseWindowStation, DuplicateTokenEx, CreateProcessAsUserW` | **High (Decompiled C Flow)** |
| `0x004465bb` | `FUN_004465bb` | 9 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00446606` | `FUN_00446606` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00446618` | `FUN_00446618` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044663b` | `FUN_0044663b` | 7 | 513 | `Core Subsystem Logic` | `None` | `FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x00447157` | `FUN_00447157` | 5 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044719b` | `FUN_0044719b` | 5 | 39 | `Helper Subroutine` | `None` | `ExtCreatePen, DeleteObject, SelectObject` | **Medium (Decompiled C Flow)** |
| `0x00447275` | `FUN_00447275` | 4 | 22 | `Helper Subroutine` | `None` | `StrokePath, EndPath, MoveToEx` | **Medium (Decompiled C Flow)** |
| `0x004472f1` | `FUN_004472f1` | 6 | 20 | `Helper Subroutine` | `None` | `StrokePath, EndPath, MoveToEx` | **Medium (Decompiled C Flow)** |
| `0x0044734f` | `FUN_0044734f` | 2 | 115 | `Core Subsystem Logic` | `None` | `MoveToEx, Rectangle, SetPixel` | **High (Decompiled C Flow)** |
| `0x004475cc` | `FUN_004475cc` | 2 | 71 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0044770d` | `FUN_0044770d` | 2 | 69 | `Core Subsystem Logic` | `None` | `BeginPath, PolyDraw` | **High (Decompiled C Flow)** |
| `0x0044786a` | `FUN_0044786a` | 3 | 20 | `Helper Subroutine` | `None` | `DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x004478ac` | `FUN_004478ac` | 4 | 41 | `Helper Subroutine` | `None` | `DefDlgProcW, CONCAT22, GetCursorPos` | **Medium (Decompiled C Flow)** |
| `0x004479a0` | `FUN_004479a0` | 4 | 45 | `Helper Subroutine` | `None` | `GetClientRect, CONCAT22, GetCursorPos` | **Medium (Decompiled C Flow)** |
| `0x00447abc` | `FUN_00447abc` | 2 | 31 | `Helper Subroutine` | `None` | `DefDlgProcW, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00447b4e` | `FUN_00447b4e` | 2 | 15 | `Helper Subroutine` | `None` | `DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x00447b89` | `FUN_00447b89` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00447ba8` | `FUN_00447ba8` | 1 | 59 | `Core Subsystem Logic` | `None` | `Rectangle, EndPaint, SetViewportOrgEx` | **High (Decompiled C Flow)** |
| `0x00447d22` | `FUN_00447d22` | 2 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00447d4d` | `FUN_00447d4d` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00447d63` | `FUN_00447d63` | 2 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00447da4` | `FUN_00447da4` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00447dc1` | `FUN_00447dc1` | 2 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00447e05` | `FUN_00447e05` | 2 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00447e8e` | `FUN_00447e8e` | 8 | 69 | `Core Subsystem Logic` | `None` | `InvalidateRect` | **High (Decompiled C Flow)** |
| `0x00448046` | `FUN_00448046` | 3 | 50 | `Helper Subroutine` | `None` | `CONCAT31, CreatePopupMenu` | **Medium (Decompiled C Flow)** |
| `0x00448123` | `FUN_00448123` | 4 | 105 | `Core Subsystem Logic` | `None` | `CONCAT31, SendMessageW, GetWindowLongW` | **High (Decompiled C Flow)** |
| `0x0044835a` | `FUN_0044835a` | 4 | 74 | `Core Subsystem Logic` | `None` | `CONCAT31, SendMessageW` | **High (Decompiled C Flow)** |
| `0x00448480` | `FUN_00448480` | 7 | 66 | `Core Subsystem Logic` | `None` | `CONCAT31, DrawMenuBar, GetMenuItemInfoW` | **High (Decompiled C Flow)** |
| `0x004485cb` | `FUN_004485cb` | 6 | 64 | `Core Subsystem Logic` | `None` | `CONCAT31, DrawMenuBar, GetMenuItemInfoW` | **High (Decompiled C Flow)** |
| `0x0044870c` | `FUN_0044870c` | 2 | 263 | `Core Subsystem Logic` | `None` | `EnableWindow, DrawMenuBar, GetMenuItemInfoW` | **High (Decompiled C Flow)** |
| `0x00448d62` | `FUN_00448d62` | 2 | 110 | `Core Subsystem Logic` | `None` | `ShowWindow, GetWindowLongW, SetWindowLongW` | **High (Decompiled C Flow)** |
| `0x00448fa2` | `FUN_00448fa2` | 2 | 22 | `Helper Subroutine` | `None` | `PostMessageW` | **Medium (Decompiled C Flow)** |
| `0x0044900d` | `FUN_0044900d` | 2 | 62 | `Core Subsystem Logic` | `None` | `GetWindowLongW, SetWindowLongW, InvalidateRect` | **High (Decompiled C Flow)** |
| `0x00449175` | `FUN_00449175` | 1 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004491b9` | `FUN_004491b9` | 3 | 276 | `Core Subsystem Logic` | `None` | `GetMenuItemInfoW, ROUND, SetWindowTextW` | **High (Decompiled C Flow)** |
| `0x0044982a` | `FUN_0044982a` | 3 | 70 | `Core Subsystem Logic` | `None` | `ShowWindow, SetWindowLongW, SendMessageW` | **High (Decompiled C Flow)** |
| `0x004499db` | `FUN_004499db` | 5 | 70 | `Core Subsystem Logic` | `None` | `GetWindowRect, SendMessageW, MoveWindow` | **High (Decompiled C Flow)** |
| `0x00449b77` | `FUN_00449b77` | 2 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00449c00` | `FUN_00449c00` | 3 | 46 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00449d2e` | `FUN_00449d2e` | 1 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00449d86` | `FUN_00449d86` | 2 | 68 | `Core Subsystem Logic` | `None` | `CONCAT31, GetMenuItemInfoW` | **High (Decompiled C Flow)** |
| `0x00449e8b` | `FUN_00449e8b` | 9 | 46 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00449f40` | `FUN_00449f40` | 4 | 20 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00449f8f` | `FUN_00449f8f` | 2 | 41 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a032` | `FUN_0044a032` | 3 | 116 | `Core Subsystem Logic` | `None` | `SetTextColor, ReleaseDC, GetPixel` | **High (Decompiled C Flow)** |
| `0x0044a2d2` | `FUN_0044a2d2` | 0 | 33 | `Helper Subroutine` | `None` | `GetFocus, GetForegroundWindow, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x0044a357` | `FUN_0044a357` | 3 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a397` | `FUN_0044a397` | 3 | 36 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a403` | `FUN_0044a403` | 2 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a444` | `FUN_0044a444` | 2 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a4cd` | `FUN_0044a4cd` | 1 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a4e8` | `FUN_0044a4e8` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a4f7` | `FUN_0044a4f7` | 2 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a545` | `FUN_0044a545` | 2 | 59 | `Core Subsystem Logic` | `None` | `CONCAT22` | **High (Decompiled C Flow)** |
| `0x0044a625` | `FUN_0044a625` | 2 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a664` | `FUN_0044a664` | 2 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a6a5` | `FUN_0044a6a5` | 2 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a72e` | `FUN_0044a72e` | 3 | 27 | `Helper Subroutine` | `None` | `Beep` | **Medium (Decompiled C Flow)** |
| `0x0044a77d` | `FUN_0044a77d` | 3 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a79e` | `FUN_0044a79e` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a7bc` | `FUN_0044a7bc` | 3 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a801` | `FUN_0044a801` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a816` | `FUN_0044a816` | 3 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a835` | `FUN_0044a835` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044a856` | `FUN_0044a856` | 3 | 53 | `Core Subsystem Logic` | `None` | `HttpSendRequestW, CONCAT31, HttpQueryInfoW` | **High (Decompiled C Flow)** |
| `0x0044a983` | `FUN_0044a983` | 4 | 54 | `Core Subsystem Logic` | `None` | `CONCAT31, InternetConnectW, FtpOpenFileW` | **High (Decompiled C Flow)** |
| `0x0044aa86` | `FUN_0044aa86` | 4 | 74 | `Core Subsystem Logic` | `None` | `HttpSendRequestW, CONCAT31, HttpQueryInfoW` | **High (Decompiled C Flow)** |
| `0x0044ac3d` | `FUN_0044ac3d` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044ac82` | `FUN_0044ac82` | 1 | 16 | `Helper Subroutine` | `None` | `CloseHandle` | **Medium (Decompiled C Flow)** |
| `0x0044acc3` | `FUN_0044acc3` | 2 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044ad24` | `FUN_0044ad24` | 2 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044ad65` | `FUN_0044ad65` | 5 | 53 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0044ae3e` | `FUN_0044ae3e` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044ae5b` | `FUN_0044ae5b` | 2 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044aeb0` | `FUN_0044aeb0` | 2 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044af39` | `FUN_0044af39` | 1 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044af6c` | `FUN_0044af6c` | 2 | 34 | `Helper Subroutine` | `None` | `GetLastError, FormatMessageW` | **Medium (Decompiled C Flow)** |
| `0x0044afd1` | `FUN_0044afd1` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044afef` | `FUN_0044afef` | 3 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b040` | `FUN_0044b040` | 1 | 35 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b0bf` | `FUN_0044b0bf` | 1 | 45 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b1a9` | `FUN_0044b1a9` | 1 | 76 | `Core Subsystem Logic` | `");
    param_1[7] = (int)pFVar2;
    if (pFVar2 == (FILE *)0x0) {
      return 2;
    }
  }
  else {
    param_1[7] = 0;
  }
  if (param_1[6] == 0) {
    pFVar2 = __wfopen((wchar_t *)((int)param_1 + 0x22e),L"` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0044b304` | `FUN_0044b304` | 0 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b366` | `FUN_0044b366` | 0 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b3ac` | `FUN_0044b3ac` | 3 | 23 | `Helper Subroutine` | `None` | `CONCAT44` | **Medium (Decompiled C Flow)** |
| `0x0044b3d9` | `FUN_0044b3d9` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b3f6` | `FUN_0044b3f6` | 2 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b41c` | `FUN_0044b41c` | 1 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b469` | `FUN_0044b469` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b489` | `FUN_0044b489` | 1 | 50 | `Helper Subroutine` | `None` | `LeaveCriticalSection, ROUND, InterlockedExchange` | **Medium (Decompiled C Flow)** |
| `0x0044b5cb` | `FUN_0044b5cb` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b5e8` | `FUN_0044b5e8` | 1 | 23 | `Helper Subroutine` | `None` | `CONCAT31, LeaveCriticalSection, InterlockedExchange` | **Medium (Decompiled C Flow)** |
| `0x0044b63b` | `FUN_0044b63b` | 1 | 25 | `Helper Subroutine` | `None` | `LeaveCriticalSection, InterlockedExchange, EnterCriticalSection` | **Medium (Decompiled C Flow)** |
| `0x0044b6ab` | `FUN_0044b6ab` | 1 | 18 | `Helper Subroutine` | `None` | `CreateThread` | **Medium (Decompiled C Flow)** |
| `0x0044b6d6` | `FUN_0044b6d6` | 1 | 65 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0044b785` | `FUN_0044b785` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b79b` | `FUN_0044b79b` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b7c1` | `FUN_0044b7c1` | 1 | 33 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b821` | `FUN_0044b821` | 1 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b877` | `FUN_0044b877` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b8a3` | `FUN_0044b8a3` | 2 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b8d4` | `FUN_0044b8d4` | 5 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b911` | `FUN_0044b911` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b92d` | `FUN_0044b92d` | 1 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b951` | `FUN_0044b951` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b960` | `FUN_0044b960` | 1 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044b98c` | `FUN_0044b98c` | 1 | 52 | `Core Subsystem Logic` | `"RIGHT", "LEFT", "MENU"` | `None` | **High (Decompiled C Flow)** |
| `0x0044ba68` | `FUN_0044ba68` | 1 | 28 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0044bacc` | `FUN_0044bacc` | 1 | 28 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0044bb30` | `FUN_0044bb30` | 2 | 38 | `Helper Subroutine` | `None` | `CONCAT31, RemoveDirectoryW, SHFileOperationW` | **Medium (Decompiled C Flow)** |
| `0x0044bbd2` | `FUN_0044bbd2` | 3 | 63 | `Core Subsystem Logic` | `"\\*.*"` | `SHFileOperationW, MoveFileW` | **High (Decompiled C Flow)** |
| `0x0044bd27` | `FUN_0044bd27` | 4 | 94 | `Core Subsystem Logic` | `"\\*.*"` | `FindNextFileW, CopyFileW, FindFirstFileW` | **High (Decompiled C Flow)** |
| `0x0044bf8b` | `FUN_0044bf8b` | 0 | 51 | `Core Subsystem Logic` | `"\\*.*"` | `FindNextFileW, FindFirstFileW, DeleteFileW` | **High (Decompiled C Flow)** |
| `0x0044c0a3` | `FUN_0044c0a3` | 2 | 59 | `Core Subsystem Logic` | `None` | `ROUND, FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x0044c1b5` | `FUN_0044c1b5` | 2 | 30 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0044c228` | `FUN_0044c228` | 3 | 37 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0044c285` | `FUN_0044c285` | 1 | 15 | `Helper Subroutine` | `None` | `CONCAT44` | **Medium (Decompiled C Flow)** |
| `0x0044c29d` | `FUN_0044c29d` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044c2b3` | `FUN_0044c2b3` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044c2c9` | `FUN_0044c2c9` | 1 | 58 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0044c37a` | `FUN_0044c37a` | 2 | 70 | `Core Subsystem Logic` | `None` | `SendInput, SetKeyboardState, GetKeyboardState` | **High (Decompiled C Flow)** |
| `0x0044c514` | `FUN_0044c514` | 2 | 73 | `Core Subsystem Logic` | `None` | `SendInput, SetKeyboardState, GetKeyboardState` | **High (Decompiled C Flow)** |
| `0x0044c6d7` | `FUN_0044c6d7` | 2 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044c6f6` | `FUN_0044c6f6` | 2 | 46 | `Helper Subroutine` | `None` | `VkKeyScanW, CONCAT31, MapVirtualKeyW` | **Medium (Decompiled C Flow)** |
| `0x0044c777` | `FUN_0044c777` | 2 | 30 | `Helper Subroutine` | `None` | `MapVirtualKeyW` | **Medium (Decompiled C Flow)** |
| `0x0044c7c0` | `FUN_0044c7c0` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044c7dd` | `FUN_0044c7dd` | 2 | 45 | `Script / Win32 Host Logic` | `"#requireadmin", "#OnAutoItStartRegister", "#notrayicon"` | `None` | **High (Verified Logic)** |
| `0x0044c8cd` | `FUN_0044c8cd` | 1 | 18 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0044c901` | `FUN_0044c901` | 2 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044c94a` | `FUN_0044c94a` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044c974` | `FUN_0044c974` | 4 | 36 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0044ca07` | `FUN_0044ca07` | 3 | 67 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0044cb39` | `FUN_0044cb39` | 1 | 23 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0044cb87` | `FUN_0044cb87` | 4 | 44 | `Helper Subroutine` | `None` | `CreateDispTypeInfo, CreateStdDispatch` | **Medium (Decompiled C Flow)** |
| `0x0044cc34` | `FUN_0044cc34` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044cc51` | `FUN_0044cc51` | 2 | 32 | `Helper Subroutine` | `None` | `ReleaseDC, GetDC, GetDeviceCaps` | **Medium (Decompiled C Flow)** |
| `0x0044ccd4` | `FUN_0044ccd4` | 0 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044ccf1` | `FUN_0044ccf1` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044cd0e` | `FUN_0044cd0e` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044cd1c` | `FUN_0044cd1c` | 3 | 34 | `Helper Subroutine` | `None` | `CONCAT31, GetWindowRect, ScreenToClient` | **Medium (Decompiled C Flow)** |
| `0x0044cd93` | `FUN_0044cd93` | 2 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044cdaf` | `FUN_0044cdaf` | 2 | 22 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0044cde9` | `FUN_0044cde9` | 3 | 14 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0044ce43` | `FUN_0044ce43` | 0 | 31 | `Helper Subroutine` | `None` | `SafeArrayCreateVector, FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0044cecd` | `FUN_0044cecd` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044cef6` | `FUN_0044cef6` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0044cf17` | `FUN_0044cf17` | 9 | 2,474 | `Core Subsystem Logic` | `"DEFINE", "Q\\E"` | `CONCAT31, FID_conflict__memcpy, CONCAT11` | **High (Decompiled C Flow)** |
| `0x0045039b` | `FUN_0045039b` | 4 | 44 | `Helper Subroutine` | `None` | `GetParent, DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x004504a4` | `FUN_004504a4` | 3 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00450517` | `FUN_00450517` | 2 | 44 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004505f0` | `FUN_004505f0` | 10 | 92 | `Core Subsystem Logic` | `"SysListView32", ",uVar2,param_5,param_6,param_7,param_8,
                        param_3,'\0');
  *param_2 = pHVar3;
  if (pHVar3 == (HWND)0x0) {
    return 0;
  }
  if (param_10._3_1_ != '\0') {
    SendMessageW(pHVar3,0x1036,0x10,0x10);
    lParam = lParam | 0x10;
  }
  SendMessageW((HWND)*param_2,0x1036,0,lParam);
  if (param_1[99] != 0) {
    SetWindowPos((HWND)*param_2,(HWND)0x0,0,0,0,0,0x13);
  }
  local_18 = local_2024;
  local_24 = 0xf;
  local_20 = 0;
  param_8 = param_4;
  while( true ) {
    bVar1 = FUN_00430626(local_2024,&param_8,&DAT_004a8644);
    if (!bVar1) break;
    sVar4 = _wcslen(local_2024);
    _wcscat(local_2024,L"` | `CONCAT31, SendMessageW, CONCAT13` | **High (Decompiled C Flow)** |
| `0x004507b7` | `FUN_004507b7` | 9 | 66 | `Core Subsystem Logic` | `"SysTreeView32"` | `CONCAT31, SetWindowLongW, GetWindowLongW` | **High (Decompiled C Flow)** |
| `0x004508f9` | `FUN_004508f9` | 9 | 45 | `Helper Subroutine` | `"SysTabControl32"` | `CONCAT31, SetWindowPos` | **Medium (Decompiled C Flow)** |
| `0x004509d8` | `FUN_004509d8` | 5 | 46 | `Helper Subroutine` | `"msctls_updown32"` | `CONCAT31, DestroyWindow, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00450acc` | `FUN_00450acc` | 9 | 37 | `Helper Subroutine` | `"msctls_trackbar32"` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00450b7c` | `FUN_00450b7c` | 9 | 37 | `Helper Subroutine` | `"Msctls_Progress32"` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00450c41` | `FUN_00450c41` | 10 | 58 | `Core Subsystem Logic` | `"static"` | `SetLayeredWindowAttributes, CreateCompatibleDC, DeleteDC` | **High (Decompiled C Flow)** |
| `0x00450d6b` | `FUN_00450d6b` | 10 | 48 | `Helper Subroutine` | `"SysMonthCal32"` | `CONCAT31, SendMessageW, SetWindowPos` | **Medium (Decompiled C Flow)** |
| `0x00450e5d` | `FUN_00450e5d` | 10 | 41 | `Helper Subroutine` | `"SysDateTimePick32"` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00450f30` | `FUN_00450f30` | 10 | 43 | `Helper Subroutine` | `"Listbox"` | `CONCAT31, MoveWindow, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00451006` | `FUN_00451006` | 10 | 41 | `Helper Subroutine` | `"Combobox"` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x004510c5` | `FUN_004510c5` | 10 | 39 | `Helper Subroutine` | `"button"` | `CONCAT31, GetSysColor` | **Medium (Decompiled C Flow)** |
| `0x00451159` | `FUN_00451159` | 10 | 37 | `Helper Subroutine` | `"button"` | `CONCAT31, GetSysColor` | **Medium (Decompiled C Flow)** |
| `0x004511e7` | `FUN_004511e7` | 10 | 40 | `Helper Subroutine` | `"button"` | `CONCAT31, GetSysColor` | **Medium (Decompiled C Flow)** |
| `0x00451282` | `FUN_00451282` | 10 | 43 | `Helper Subroutine` | `"edit"` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00451321` | `FUN_00451321` | 10 | 48 | `Helper Subroutine` | `"edit"` | `GetWindowTextLengthW, CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x004513e1` | `FUN_004513e1` | 10 | 34 | `Helper Subroutine` | `"static"` | `CONCAT31, GetSysColor` | **Medium (Decompiled C Flow)** |
| `0x00451465` | `FUN_00451465` | 10 | 40 | `Helper Subroutine` | `"button"` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00451507` | `FUN_00451507` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00451554` | `FUN_00451554` | 3 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004515b4` | `FUN_004515b4` | 6 | 51 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x004516ae` | `FUN_004516ae` | 6 | 38 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045174d` | `FUN_0045174d` | 2 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045178a` | `FUN_0045178a` | 2 | 34 | `Helper Subroutine` | `None` | `CONCAT31, Sleep` | **Medium (Decompiled C Flow)** |
| `0x00451808` | `FUN_00451808` | 5 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00451877` | `FUN_00451877` | 6 | 49 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00451930` | `FUN_00451930` | 1 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045195e` | `FUN_0045195e` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045197b` | `FUN_0045197b` | 2 | 40 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00451a0d` | `FUN_00451a0d` | 1 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00451aa8` | `FUN_00451aa8` | 3 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00451b19` | `FUN_00451b19` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00451b42` | `FUN_00451b42` | 5 | 89 | `Core Subsystem Logic` | `None` | `GetLastError, VariantCopy, SysAllocString` | **High (Decompiled C Flow)** |
| `0x00451d2b` | `FUN_00451d2b` | 4 | 181 | `Core Subsystem Logic` | `None` | `SysFreeString` | **High (Decompiled C Flow)** |
| `0x0045213b` | `FUN_0045213b` | 2 | 34 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x004521b3` | `FUN_004521b3` | 2 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004521f7` | `FUN_004521f7` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00452214` | `FUN_00452214` | 2 | 40 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004522e2` | `FUN_004522e2` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004522f8` | `FUN_004522f8` | 2 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045233c` | `FUN_0045233c` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00452359` | `FUN_00452359` | 2 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045239d` | `FUN_0045239d` | 1 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004523db` | `FUN_004523db` | 2 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00452464` | `FUN_00452464` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00452492` | `FUN_00452492` | 6 | 84 | `Core Subsystem Logic` | `");
      if ((iVar4 != 0) && (iVar4 = _wcscmp(local_27c.cFileName,L"` | `CONCAT31, CARRY4, FindNextFileW` | **High (Decompiled C Flow)** |
| `0x00452620` | `FUN_00452620` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045263d` | `FUN_0045263d` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00452653` | `FUN_00452653` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00452670` | `FUN_00452670` | 0 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045268e` | `FUN_0045268e` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004526ab` | `FUN_004526ab` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004526cf` | `FUN_004526cf` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004526ec` | `FUN_004526ec` | 1 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00452719` | `FUN_00452719` | 3 | 56 | `Core Subsystem Logic` | `"FILE"` | `None` | **High (Decompiled C Flow)** |
| `0x004528bd` | `FUN_004528bd` | 4 | 92 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00452ac7` | `FUN_00452ac7` | 3 | 153 | `Core Subsystem Logic` | `");
  if (iVar1 == 0) {
    iVar1 = FUN_00452719(param_1,param_2,awStack_10628);
    if (iVar1 == 0) {
      __wsplitpath(param_3,(wchar_t *)auStack_111a8,awStack_10210,awStack_10418,awStack_10830);
      _wcscpy(awStack_10a40,(wchar_t *)auStack_111a8);
      _wcscat(awStack_10a40,awStack_10210);
      __wsplitpath(awStack_10628,(wchar_t *)auStack_111a8,awStack_10210,awStack_10418,awStack_10830)
      ;
      _wcscat(awStack_10a40,awStack_10418);
      _wcscat(awStack_10a40,awStack_10830);
      param_3 = awStack_10a40;
LAB_00452c47:
      _fread(&cStack_111c1,1,1,(FILE *)*param_1);
      _fread(&uStack_111c0,4,1,(FILE *)*param_1);
      uVar3 = uStack_111c0 ^ 0x87bc;
      uStack_111bc = uVar3;
      _fread(&uStack_111c0,4,1,(FILE *)*param_1);
      _fread(&uStack_111c0,4,1,(FILE *)*param_1);
      auStack_111a8[0] = uStack_111c0 ^ 0xa685;
      _fread(&FStack_111a0.dwHighDateTime,4,1,(FILE *)*param_1);
      _fread(&FStack_111a0,4,1,(FILE *)*param_1);
      _fread(&FStack_11198.dwHighDateTime,4,1,(FILE *)*param_1);
      _fread(&FStack_11198,4,1,(FILE *)*param_1);
      FUN_00431e1f(aWStack_10d28);
      pFStack_111b8 = __wfopen(aWStack_10d28,L"` | `CopyFileW, DeleteFileW` | **High (Decompiled C Flow)** |
| `0x00452f05` | `FUN_00452f05` | 1 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00452f37` | `FUN_00452f37` | 4 | 85 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x0045308a` | `FUN_0045308a` | 2 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004530c9` | `FUN_004530c9` | 2 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004530e8` | `FUN_004530e8` | 1 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453132` | `FUN_00453132` | 2 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004531b1` | `FUN_004531b1` | 1 | 79 | `Core Subsystem Logic` | `"%.15g", "0x%p", "False"` | `None` | **High (Decompiled C Flow)** |
| `0x004533b1` | `FUN_004533b1` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004533eb` | `FUN_004533eb` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045340c` | `FUN_0045340c` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453443` | `FUN_00453443` | 2 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004534c0` | `FUN_004534c0` | 2 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004534e3` | `FUN_004534e3` | 3 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453512` | `FUN_00453512` | 2 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453545` | `FUN_00453545` | 1 | 17 | `Helper Subroutine` | `None` | `DeleteCriticalSection, CloseHandle` | **Medium (Decompiled C Flow)** |
| `0x00453586` | `FUN_00453586` | 1 | 34 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045360e` | `FUN_0045360e` | 4 | 40 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453694` | `FUN_00453694` | 2 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004536cb` | `FUN_004536cb` | 1 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004536f7` | `FUN_004536f7` | 1 | 12 | `Helper Subroutine` | `None` | `CharLowerBuffW` | **Medium (Decompiled C Flow)** |
| `0x00453717` | `FUN_00453717` | 2 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045377f` | `FUN_0045377f` | 3 | 50 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045383c` | `FUN_0045383c` | 1 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453893` | `FUN_00453893` | 3 | 81 | `Core Subsystem Logic` | `None` | `CONCAT31, SHFileOperationW, MoveFileW` | **High (Decompiled C Flow)** |
| `0x00453a8b` | `FUN_00453a8b` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453abd` | `FUN_00453abd` | 2 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453b16` | `FUN_00453b16` | 2 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453b6f` | `FUN_00453b6f` | 2 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453bc6` | `FUN_00453bc6` | 2 | 33 | `Helper Subroutine` | `None` | `CONCAT31, Sleep` | **Medium (Decompiled C Flow)** |
| `0x00453c57` | `FUN_00453c57` | 2 | 105 | `Core Subsystem Logic` | `None` | `SetKeyboardState, GetKeyboardState, GetAsyncKeyState` | **High (Decompiled C Flow)** |
| `0x00453e8d` | `FUN_00453e8d` | 3 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453ef0` | `FUN_00453ef0` | 3 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00453f64` | `FUN_00453f64` | 3 | 52 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00454014` | `FUN_00454014` | 5 | 49 | `Helper Subroutine` | `"Line %d  (File \", "):\n\n", "%s (%d) : ==> %s.: \n%s \n%s\n"` | `GetModuleHandleW, LoadStringW, FID_conflict__wprintf` | **Medium (Decompiled C Flow)** |
| `0x0045412d` | `FUN_0045412d` | 3 | 33 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x004541a8` | `FUN_004541a8` | 2 | 26 | `Helper Subroutine` | `None` | `WideCharToMultiByte` | **Medium (Decompiled C Flow)** |
| `0x00454224` | `FUN_00454224` | 2 | 48 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004542ed` | `FUN_004542ed` | 7 | 174 | `Core Subsystem Logic` | `"AU3_FreeVar"` | `GetProcAddress, SUB84` | **High (Decompiled C Flow)** |
| `0x00454639` | `FUN_00454639` | 1 | 90 | `Core Subsystem Logic` | `None` | `CONCAT44, SendDlgItemMessageW, GetWindowRect` | **High (Decompiled C Flow)** |
| `0x00454855` | `FUN_00454855` | 1 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00454879` | `FUN_00454879` | 2 | 53 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045491b` | `FUN_0045491b` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045493c` | `FUN_0045493c` | 13 | 217 | `Core Subsystem Logic` | `None` | `FID_conflict__memcpy, CONCAT11` | **High (Decompiled C Flow)** |
| `0x00454cfc` | `FUN_00454cfc` | 4 | 18 | `Helper Subroutine` | `None` | `DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x00454d4a` | `FUN_00454d4a` | 4 | 43 | `Helper Subroutine` | `None` | `CONCAT22, DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x00454e33` | `FUN_00454e33` | 3 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00454e8d` | `FUN_00454e8d` | 4 | 116 | `Core Subsystem Logic` | `".dll", ".exe", ".icl"` | `DestroyIcon, FreeLibrary, CONCAT31` | **High (Decompiled C Flow)** |
| `0x004550fc` | `FUN_004550fc` | 2 | 271 | `Core Subsystem Logic` | `None` | `DestroyIcon, GetMenuItemCount, DeleteMenu` | **High (Decompiled C Flow)** |
| `0x004557e0` | `FUN_004557e0` | 6 | 94 | `Core Subsystem Logic` | `"tooltips_class32"` | `DestroyWindow, GetWindowRect, CreateWindowExW` | **High (Decompiled C Flow)** |
| `0x00455a89` | `FUN_00455a89` | 3 | 305 | `Core Subsystem Logic` | `"%d/%02d/%02d"` | `GetMenuItemInfoW, GetWindowLongW, GetWindowTextW` | **High (Decompiled C Flow)** |
| `0x004561da` | `FUN_004561da` | 7 | 84 | `Core Subsystem Logic` | `None` | `DestroyIcon, LoadImageW, InvalidateRect` | **High (Decompiled C Flow)** |
| `0x00456391` | `FUN_00456391` | 3 | 71 | `Core Subsystem Logic` | `None` | `GetWindowLongW, GetAsyncKeyState, GetCursorPos` | **High (Decompiled C Flow)** |
| `0x004564ef` | `FUN_004564ef` | 1 | 49 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004565b2` | `FUN_004565b2` | 3 | 180 | `Core Subsystem Logic` | `"tooltips_class32"` | `GetMonitorInfoW, IsWindowVisible, DestroyWindow` | **High (Decompiled C Flow)** |
| `0x00456929` | `FUN_00456929` | 1 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045699f` | `FUN_0045699f` | 1 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00456a0d` | `FUN_00456a0d` | 2 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00456a5a` | `FUN_00456a5a` | 2 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00456aa6` | `FUN_00456aa6` | 2 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00456b2a` | `FUN_00456b2a` | 2 | 33 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00456b8f` | `FUN_00456b8f` | 2 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00456bf4` | `FUN_00456bf4` | 2 | 32 | `Helper Subroutine` | `None` | `IsCharUpperW` | **Medium (Decompiled C Flow)** |
| `0x00456c57` | `FUN_00456c57` | 2 | 32 | `Helper Subroutine` | `None` | `IsCharLowerW` | **Medium (Decompiled C Flow)** |
| `0x00456cba` | `FUN_00456cba` | 2 | 33 | `Helper Subroutine` | `None` | `FID_conflict___iswxdigit_l` | **Medium (Decompiled C Flow)** |
| `0x00456d1f` | `FUN_00456d1f` | 2 | 32 | `Helper Subroutine` | `None` | `FID_conflict___iswdigit_l` | **Medium (Decompiled C Flow)** |
| `0x00456d84` | `FUN_00456d84` | 2 | 32 | `Helper Subroutine` | `None` | `IsCharAlphaNumericW` | **Medium (Decompiled C Flow)** |
| `0x00456de7` | `FUN_00456de7` | 2 | 32 | `Helper Subroutine` | `None` | `IsCharAlphaW` | **Medium (Decompiled C Flow)** |
| `0x00456e4a` | `FUN_00456e4a` | 1 | 71 | `Core Subsystem Logic` | `");
    pwVar4 = (wchar_t *)0x0;
    if (iVar2 != 0) {
      pwVar3 = (wchar_t *)_wcscmp(_Str1,L"` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00456f09` | `FUN_00456f09` | 2 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00456f38` | `FUN_00456f38` | 1 | 88 | `Core Subsystem Logic` | `");
  pwVar2 = (wchar_t *)0x0;
  if (iVar1 == 0) goto switchD_00456fcc_caseD_2c;
  iVar1 = _wcscmp(_Str1,L"` | `FID_conflict___iswdigit_l` | **High (Decompiled C Flow)** |
| `0x00457067` | `FUN_00457067` | 2 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00457096` | `FUN_00457096` | 1 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004570fc` | `FUN_004570fc` | 1 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045713e` | `FUN_0045713e` | 1 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00457190` | `FUN_00457190` | 1 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004571e4` | `FUN_004571e4` | 2 | 90 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00457368` | `FUN_00457368` | 2 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004573de` | `FUN_004573de` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045740d` | `FUN_0045740d` | 2 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00457451` | `FUN_00457451` | 3 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004574b4` | `FUN_004574b4` | 2 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004574f6` | `FUN_004574f6` | 3 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00457557` | `FUN_00457557` | 2 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004575bf` | `FUN_004575bf` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004575f1` | `FUN_004575f1` | 4 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00457655` | `FUN_00457655` | 4 | 30 | `Helper Subroutine` | `None` | `VirtualFree` | **Medium (Decompiled C Flow)** |
| `0x004576e0` | `FUN_004576e0` | 4 | 25 | `Helper Subroutine` | `None` | `FreeLibrary` | **Medium (Decompiled C Flow)** |
| `0x0045774c` | `FUN_0045774c` | 3 | 45 | `Helper Subroutine` | `None` | `LoadLibraryW` | **Medium (Decompiled C Flow)** |
| `0x004577e9` | `FUN_004577e9` | 5 | 143 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x00457ad9` | `FUN_00457ad9` | 2 | 62 | `Core Subsystem Logic` | `None` | `CloseHandle, SetPriorityClass, OpenProcess` | **High (Decompiled C Flow)** |
| `0x00457be5` | `FUN_00457be5` | 4 | 32 | `Helper Subroutine` | `None` | `GetLastError` | **Medium (Decompiled C Flow)** |
| `0x00457c53` | `FUN_00457c53` | 5 | 107 | `Core Subsystem Logic` | `None` | `ShellExecuteExW, CloseHandle` | **High (Decompiled C Flow)** |
| `0x00457e22` | `FUN_00457e22` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00457e3f` | `FUN_00457e3f` | 3 | 45 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00457ee2` | `FUN_00457ee2` | 3 | 36 | `Helper Subroutine` | `None` | `CONCAT31, GetTime` | **Medium (Decompiled C Flow)** |
| `0x00457f66` | `FUN_00457f66` | 1 | 85 | `Core Subsystem Logic` | `None` | `GetEnvironmentVariableW` | **High (Decompiled C Flow)** |
| `0x004580c4` | `FUN_004580c4` | 1 | 204 | `Core Subsystem Logic` | `None` | `GetModuleFileNameW, StringFromGUID2, QueryPathOfRegTypeLib` | **High (Decompiled C Flow)** |
| `0x0045861f` | `FUN_0045861f` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00458651` | `FUN_00458651` | 5 | 66 | `Script / Win32 Host Logic` | `None` | `RegConnectRegistryW, RegOpenKeyExW, RegQueryValueExW` | **High (Verified Logic)** |
| `0x004587e8` | `FUN_004587e8` | 1 | 50 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045893c` | `FUN_0045893c` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045896e` | `FUN_0045896e` | 2 | 15 | `Helper Subroutine` | `None` | `WSACleanup` | **Medium (Decompiled C Flow)** |
| `0x004589ac` | `FUN_004589ac` | 2 | 16 | `Helper Subroutine` | `None` | `WSAStartup` | **Medium (Decompiled C Flow)** |
| `0x004589fe` | `FUN_004589fe` | 4 | 25 | `Helper Subroutine` | `None` | `WSAGetLastError` | **Medium (Decompiled C Flow)** |
| `0x00458a61` | `FUN_00458a61` | 4 | 39 | `Helper Subroutine` | `None` | `WSAGetLastError, WSAFDIsSet` | **Medium (Decompiled C Flow)** |
| `0x00458b35` | `FUN_00458b35` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00458b67` | `FUN_00458b67` | 2 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00458bc9` | `FUN_00458bc9` | 2 | 101 | `Core Subsystem Logic` | `None` | `CONCAT44, ROUND, MessageBoxW` | **High (Decompiled C Flow)** |
| `0x00458d56` | `FUN_00458d56` | 1 | 45 | `Helper Subroutine` | `None` | `Shell_NotifyIconW` | **Medium (Decompiled C Flow)** |
| `0x00458e32` | `FUN_00458e32` | 4 | 23 | `Helper Subroutine` | `None` | `OutSetVolume` | **Medium (Decompiled C Flow)** |
| `0x00458eab` | `FUN_00458eab` | 2 | 56 | `Core Subsystem Logic` | `None` | `LoadCursorW, GetCursorInfo` | **High (Decompiled C Flow)** |
| `0x00459001` | `FUN_00459001` | 2 | 44 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004590bd` | `FUN_004590bd` | 3 | 138 | `Script / Win32 Host Logic` | `"AutoIt v3", "msctls_progress32", "static"` | `ShowWindow, SystemParametersInfoW, CreateWindowExW` | **High (Verified Logic)** |
| `0x00459407` | `FUN_00459407` | 3 | 40 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x004594bd` | `FUN_004594bd` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004594d3` | `FUN_004594d3` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004594e9` | `FUN_004594e9` | 3 | 258 | `Script / Win32 Host Logic` | `"AutoIt v3", "static", "DISPLAY"` | `ShowWindow, OleLoadPicture, CreateWindowExW` | **High (Verified Logic)** |
| `0x00459a7e` | `FUN_00459a7e` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00459a94` | `FUN_00459a94` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00459aaa` | `FUN_00459aaa` | 2 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00459add` | `FUN_00459add` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00459b06` | `FUN_00459b06` | 2 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00459b41` | `FUN_00459b41` | 2 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00459b7c` | `FUN_00459b7c` | 4 | 33 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00459c06` | `FUN_00459c06` | 3 | 49 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00459d36` | `FUN_00459d36` | 3 | 92 | `Core Subsystem Logic` | `None` | `GetCursorPos` | **High (Decompiled C Flow)** |
| `0x00459ef1` | `FUN_00459ef1` | 4 | 44 | `Helper Subroutine` | `None` | `ReleaseDC, GetDC, GetPixel` | **Medium (Decompiled C Flow)** |
| `0x00459fc0` | `FUN_00459fc0` | 3 | 94 | `Core Subsystem Logic` | `None` | `CONCAT44, GetForegroundWindow, IsWindow` | **High (Decompiled C Flow)** |
| `0x0045a10f` | `FUN_0045a10f` | 2 | 65 | `Core Subsystem Logic` | `None` | `GlobalUnlock, SetClipboardData, GlobalLock` | **High (Decompiled C Flow)** |
| `0x0045a26c` | `FUN_0045a26c` | 2 | 20 | `Helper Subroutine` | `None` | `SendMessageTimeoutW` | **Medium (Decompiled C Flow)** |
| `0x0045a2c6` | `FUN_0045a2c6` | 2 | 30 | `Helper Subroutine` | `None` | `SetEnvironmentVariableW` | **Medium (Decompiled C Flow)** |
| `0x0045a312` | `FUN_0045a312` | 2 | 23 | `Helper Subroutine` | `None` | `GetEnvironmentVariableW` | **Medium (Decompiled C Flow)** |
| `0x0045a370` | `FUN_0045a370` | 4 | 18 | `Helper Subroutine` | `None` | `BlockInput` | **Medium (Decompiled C Flow)** |
| `0x0045a3ac` | `FUN_0045a3ac` | 0 | 18 | `Helper Subroutine` | `None` | `GetWindowTextW` | **Medium (Decompiled C Flow)** |
| `0x0045a3fe` | `FUN_0045a3fe` | 1 | 14 | `Helper Subroutine` | `None` | `SetWindowTextW` | **Medium (Decompiled C Flow)** |
| `0x0045a423` | `FUN_0045a423` | 3 | 66 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045a52f` | `FUN_0045a52f` | 2 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a54c` | `FUN_0045a54c` | 2 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a5aa` | `FUN_0045a5aa` | 2 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a608` | `FUN_0045a608` | 2 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a647` | `FUN_0045a647` | 2 | 70 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x0045a768` | `FUN_0045a768` | 2 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a7a7` | `FUN_0045a7a7` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a7e6` | `FUN_0045a7e6` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a825` | `FUN_0045a825` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a864` | `FUN_0045a864` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a8a3` | `FUN_0045a8a3` | 2 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a8e2` | `FUN_0045a8e2` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a921` | `FUN_0045a921` | 2 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a960` | `FUN_0045a960` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045a99f` | `FUN_0045a99f` | 4 | 90 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045ab6b` | `FUN_0045ab6b` | 4 | 36 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045abcf` | `FUN_0045abcf` | 4 | 98 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045ada1` | `FUN_0045ada1` | 4 | 34 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045adf3` | `FUN_0045adf3` | 4 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045ae22` | `FUN_0045ae22` | 4 | 34 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045ae74` | `FUN_0045ae74` | 4 | 34 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045aec6` | `FUN_0045aec6` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045aef8` | `FUN_0045aef8` | 4 | 17 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045af26` | `FUN_0045af26` | 2 | 33 | `Helper Subroutine` | `None` | `IsWindow, SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045af70` | `FUN_0045af70` | 4 | 28 | `Helper Subroutine` | `None` | `IsWindow, SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045afe3` | `FUN_0045afe3` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b004` | `FUN_0045b004` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b036` | `FUN_0045b036` | 2 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b0b7` | `FUN_0045b0b7` | 2 | 33 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b13f` | `FUN_0045b13f` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b171` | `FUN_0045b171` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b1a3` | `FUN_0045b1a3` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b1d5` | `FUN_0045b1d5` | 3 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b26a` | `FUN_0045b26a` | 3 | 36 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b33b` | `FUN_0045b33b` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b36a` | `FUN_0045b36a` | 2 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b3be` | `FUN_0045b3be` | 4 | 38 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b445` | `FUN_0045b445` | 1 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b49e` | `FUN_0045b49e` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b4b7` | `FUN_0045b4b7` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b4d0` | `FUN_0045b4d0` | 4 | 31 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0045b556` | `FUN_0045b556` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b578` | `FUN_0045b578` | 2 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b59e` | `FUN_0045b59e` | 2 | 37 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0045b606` | `FUN_0045b606` | 4 | 23 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045b641` | `FUN_0045b641` | 2 | 89 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045b775` | `FUN_0045b775` | 4 | 50 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045b80a` | `FUN_0045b80a` | 4 | 42 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045b89d` | `FUN_0045b89d` | 2 | 60 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045b97b` | `FUN_0045b97b` | 4 | 32 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0045b9ce` | `FUN_0045b9ce` | 4 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045ba01` | `FUN_0045ba01` | 2 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045ba54` | `FUN_0045ba54` | 4 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045ba9c` | `FUN_0045ba9c` | 4 | 45 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045bb27` | `FUN_0045bb27` | 4 | 73 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045bc38` | `FUN_0045bc38` | 4 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045bc8a` | `FUN_0045bc8a` | 2 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045bd04` | `FUN_0045bd04` | 4 | 25 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045bd53` | `FUN_0045bd53` | 4 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045bd91` | `FUN_0045bd91` | 4 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045bdcf` | `FUN_0045bdcf` | 2 | 67 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045bedf` | `FUN_0045bedf` | 4 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045bf17` | `FUN_0045bf17` | 4 | 31 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045bf7a` | `FUN_0045bf7a` | 2 | 78 | `Core Subsystem Logic` | `None` | `CONCAT44, SUB84` | **High (Decompiled C Flow)** |
| `0x0045c09c` | `FUN_0045c09c` | 3 | 38 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045c105` | `FUN_0045c105` | 4 | 35 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045c158` | `FUN_0045c158` | 4 | 35 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045c1c4` | `FUN_0045c1c4` | 4 | 26 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045c218` | `FUN_0045c218` | 4 | 28 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045c26c` | `FUN_0045c26c` | 4 | 34 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045c2be` | `FUN_0045c2be` | 4 | 29 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045c317` | `FUN_0045c317` | 4 | 26 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0045c362` | `FUN_0045c362` | 6 | 27 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0045c3c1` | `FUN_0045c3c1` | 2 | 67 | `Core Subsystem Logic` | `None` | `WritePrivateProfileStringW, GetPrivateProfileSectionW, WritePrivateProfileSectionW` | **High (Decompiled C Flow)** |
| `0x0045c51e` | `FUN_0045c51e` | 4 | 33 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045c587` | `FUN_0045c587` | 2 | 20 | `Helper Subroutine` | `None` | `SetCurrentDirectoryW` | **Medium (Decompiled C Flow)** |
| `0x0045c5c0` | `FUN_0045c5c0` | 4 | 78 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045c730` | `FUN_0045c730` | 4 | 72 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045c862` | `FUN_0045c862` | 4 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045c8c1` | `FUN_0045c8c1` | 2 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045c8fc` | `FUN_0045c8fc` | 2 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045c937` | `FUN_0045c937` | 4 | 34 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045c9a0` | `FUN_0045c9a0` | 3 | 34 | `Helper Subroutine` | `None` | `GetShortPathNameW` | **Medium (Decompiled C Flow)** |
| `0x0045ca50` | `FUN_0045ca50` | 3 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045cafa` | `FUN_0045cafa` | 3 | 78 | `Core Subsystem Logic` | `");
    if (iVar2 != 0) {
      iVar2 = _wcscmp(local_258.cFileName,L"` | `FindNextFileW, FindFirstFileW, FindClose` | **High (Decompiled C Flow)** |
| `0x0045cc7a` | `FUN_0045cc7a` | 1 | 34 | `Helper Subroutine` | `";
  }
  else {
    _Str1 = (wchar_t *)FUN_0045340c(*(longlong **)(*(int *)(param_1 + 4) + 4));
  }
  pwVar3 = local_408;
  pwVar4 = _Str1;
  pWVar1 = (LPCWSTR)FUN_0045340c((longlong *)**(undefined4 **)(param_1 + 4));
  uVar2 = FUN_00433a13(pWVar1,pwVar3,pwVar4);
  if ((char)uVar2 == '\x01') {
    FUN_0040e710();
    return 0;
  }
  _wcscmp(_Str1,L"` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045cd1e` | `FUN_0045cd1e` | 2 | 128 | `Core Subsystem Logic` | `"*.*"` | `CONCAT31, GetCurrentDirectoryW, SetCurrentDirectoryW` | **High (Decompiled C Flow)** |
| `0x0045cfb1` | `FUN_0045cfb1` | 1 | 52 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045d0d9` | `FUN_0045d0d9` | 2 | 23 | `Helper Subroutine` | `None` | `SHEmptyRecycleBinW` | **Medium (Decompiled C Flow)** |
| `0x0045d11d` | `FUN_0045d11d` | 2 | 34 | `Helper Subroutine` | `None` | `SHFileOperationW` | **Medium (Decompiled C Flow)** |
| `0x0045d1af` | `FUN_0045d1af` | 4 | 63 | `Core Subsystem Logic` | `None` | `GetLastError, CreateHardLinkW, DeleteFileW` | **High (Decompiled C Flow)** |
| `0x0045d2c7` | `FUN_0045d2c7` | 2 | 42 | `Helper Subroutine` | `None` | `SetErrorMode, SetVolumeLabelW` | **Medium (Decompiled C Flow)** |
| `0x0045d36d` | `FUN_0045d36d` | 1 | 46 | `Helper Subroutine` | `None` | `SetErrorMode, GetVolumeInformationW` | **Medium (Decompiled C Flow)** |
| `0x0045d448` | `FUN_0045d448` | 1 | 47 | `Helper Subroutine` | `"%lu"` | `SetErrorMode, GetVolumeInformationW` | **Medium (Decompiled C Flow)** |
| `0x0045d53e` | `FUN_0045d53e` | 1 | 46 | `Helper Subroutine` | `None` | `SetErrorMode, GetVolumeInformationW` | **Medium (Decompiled C Flow)** |
| `0x0045d619` | `FUN_0045d619` | 1 | 75 | `Core Subsystem Logic` | `None` | `GetLastError, WARNING, SetErrorMode` | **High (Decompiled C Flow)** |
| `0x0045d86d` | `FUN_0045d86d` | 3 | 52 | `Core Subsystem Logic` | `None` | `CONCAT44, GetDiskFreeSpaceExW, SetErrorMode` | **High (Decompiled C Flow)** |
| `0x0045d94b` | `FUN_0045d94b` | 1 | 58 | `Core Subsystem Logic` | `None` | `SetErrorMode, GetDriveTypeW` | **High (Decompiled C Flow)** |
| `0x0045da73` | `FUN_0045da73` | 2 | 89 | `Core Subsystem Logic` | `"close", "closed", "open"` | `SendStringW, GetDriveTypeW` | **High (Decompiled C Flow)** |
| `0x0045dc4c` | `FUN_0045dc4c` | 1 | 119 | `Core Subsystem Logic` | `None` | `CoUninitialize, SHGetDesktopFolder, SHBrowseForFolderW` | **High (Decompiled C Flow)** |
| `0x0045de8f` | `FUN_0045de8f` | 2 | 30 | `Helper Subroutine` | `None` | `FindFirstFileW, FindClose` | **Medium (Decompiled C Flow)** |
| `0x0045df23` | `FUN_0045df23` | 2 | 106 | `Core Subsystem Logic` | `"*.*"` | `LocalFileTimeToFileTime, CONCAT31, GetLocalTime` | **High (Decompiled C Flow)** |
| `0x0045e17d` | `FUN_0045e17d` | 3 | 37 | `Helper Subroutine` | `None` | `FindClose` | **Medium (Decompiled C Flow)** |
| `0x0045e227` | `FUN_0045e227` | 3 | 72 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0045e332` | `FUN_0045e332` | 2 | 53 | `Core Subsystem Logic` | `None` | `WritePrivateProfileStringW` | **High (Decompiled C Flow)** |
| `0x0045e413` | `FUN_0045e413` | 2 | 37 | `Helper Subroutine` | `None` | `WritePrivateProfileStringW` | **Medium (Decompiled C Flow)** |
| `0x0045e4a5` | `FUN_0045e4a5` | 1 | 37 | `Helper Subroutine` | `None` | `GetPrivateProfileStringW` | **Medium (Decompiled C Flow)** |
| `0x0045e538` | `FUN_0045e538` | 2 | 80 | `Core Subsystem Logic` | `"Line %d  (File \", "%s (%d) : ==> %s:\n%s\n%s\n", "%s (%d) : ==> %s:\n"` | `LoadStringW, FID_conflict__wprintf, MessageBoxW` | **High (Decompiled C Flow)** |
| `0x0045e737` | `FUN_0045e737` | 3 | 87 | `Core Subsystem Logic` | `"Line %d  (File \", "%s (%d) : ==> %s:\n%s\n%s\n", "%s (%d) : ==> %s:\n"` | `LoadStringW, FID_conflict__wprintf, MessageBoxW` | **High (Decompiled C Flow)** |
| `0x0045e951` | `FUN_0045e951` | 1 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045e987` | `FUN_0045e987` | 1 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045e9d5` | `FUN_0045e9d5` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045ea0f` | `FUN_0045ea0f` | 2 | 252 | `Core Subsystem Logic` | `"%4d%02d%02d%02d%02d%02d"` | `CONCAT31, VariantCopy, VariantInit` | **High (Decompiled C Flow)** |
| `0x0045ef07` | `FUN_0045ef07` | 4 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045ef7b` | `FUN_0045ef7b` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045ef9c` | `FUN_0045ef9c` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0045efb9` | `FUN_0045efb9` | 1 | 19 | `Helper Subroutine` | `None` | `InterlockedDecrement` | **Medium (Decompiled C Flow)** |
| `0x0045efe4` | `FUN_0045efe4` | 7 | 219 | `Core Subsystem Logic` | `None` | `FID_conflict__iswalnum, FID_conflict___iswdigit_l` | **High (Decompiled C Flow)** |
| `0x0045f508` | `FUN_0045f508` | 4 | 32 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0045f56d` | `FUN_0045f56d` | 2 | 37 | `Helper Subroutine` | `"close PlayMe", "play PlayMe", "play PlayMe wait"` | `SendStringW` | **Medium (Decompiled C Flow)** |
| `0x0045f645` | `FUN_0045f645` | 2 | 26 | `Helper Subroutine` | `None` | `WideCharToMultiByte` | **Medium (Decompiled C Flow)** |
| `0x0045f6bb` | `FUN_0045f6bb` | 2 | 42 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0045f72f` | `FUN_0045f72f` | 3 | 33 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0045f790` | `FUN_0045f790` | 3 | 115 | `Core Subsystem Logic` | `None` | `GetMenuItemInfoW, SetMenuDefaultItem, SetMenuItemInfoW` | **High (Decompiled C Flow)** |
| `0x0045fa41` | `FUN_0045fa41` | 2 | 68 | `Core Subsystem Logic` | `None` | `GetMenuItemInfoW, DeleteMenu` | **High (Decompiled C Flow)** |
| `0x0045fbac` | `FUN_0045fbac` | 6 | 92 | `Core Subsystem Logic` | `None` | `GetMenuItemInfoW, GetMenuItemCount, InsertMenuItemW` | **High (Decompiled C Flow)** |
| `0x0045fd57` | `FUN_0045fd57` | 3 | 120 | `Core Subsystem Logic` | `None` | `CONCAT31, GetMenuItemInfoW, Sleep` | **High (Decompiled C Flow)** |
| `0x0045ffc2` | `FUN_0045ffc2` | 4 | 34 | `Helper Subroutine` | `None` | `CONCAT31, CONCAT11` | **Medium (Decompiled C Flow)** |
| `0x0046001e` | `FUN_0046001e` | 2 | 281 | `Core Subsystem Logic` | `");
      if (iVar4 == 0) {
        bVar1 = true;
      }
      else {
        iVar4 = __wcsicmp(pwVar9,L", ");
    if (iVar4 == 0) {
      local_5 = '\x01';
    }
    else {
      iVar4 = __wcsicmp(pwVar9,L", ");
        if (iVar4 == 0) {
          local_6 = '\x01';
        }
        else {
          iVar4 = __wcsicmp(pwVar9,L"` | `None` | **High (Decompiled C Flow)** |
| `0x004606a6` | `FUN_004606a6` | 3 | 87 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00460879` | `FUN_00460879` | 3 | 77 | `Core Subsystem Logic` | `"Line %d  (File \", "):\n\n", "%s (%d) : ==> %s: \n%s \n%s\n"` | `GetModuleHandleW, LoadStringW, FID_conflict__wprintf` | **High (Decompiled C Flow)** |
| `0x00460a29` | `FUN_00460a29` | 2 | 26 | `Helper Subroutine` | `None` | `MultiByteToWideChar` | **Medium (Decompiled C Flow)** |
| `0x00460aab` | `FUN_00460aab` | 3 | 76 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00460bba` | `FUN_00460bba` | 2 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00460bda` | `FUN_00460bda` | 1 | 12 | `Helper Subroutine` | `None` | `EndDialog` | **Medium (Decompiled C Flow)** |
| `0x00460c01` | `FUN_00460c01` | 1 | 26 | `Helper Subroutine` | `None` | `KillTimer, GetWindowTextW, MessageBeep` | **Medium (Decompiled C Flow)** |
| `0x00460c91` | `FUN_00460c91` | 2 | 14 | `Helper Subroutine` | `None` | `EndDialog` | **Medium (Decompiled C Flow)** |
| `0x00460cc1` | `FUN_00460cc1` | 1 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00460d41` | `FUN_00460d41` | 5 | 128 | `Script / Win32 Host Logic` | `"AutoIt3GUI", "Container"` | `OleSetContainedObject` | **High (Verified Logic)** |
| `0x00461014` | `FUN_00461014` | 2 | 146 | `Core Subsystem Logic` | `"ThumbnailClass"` | `GetClassNameW, GetWindowRect, GetWindowTextW` | **High (Decompiled C Flow)** |
| `0x0046130d` | `FUN_0046130d` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00461321` | `FUN_00461321` | 0 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00461383` | `FUN_00461383` | 1 | 36 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x0046142e` | `FUN_0046142e` | 1 | 14 | `Helper Subroutine` | `None` | `GetClassNameW` | **Medium (Decompiled C Flow)** |
| `0x00461465` | `FUN_00461465` | 4 | 37 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0046150f` | `FUN_0046150f` | 4 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00461554` | `FUN_00461554` | 2 | 36 | `Helper Subroutine` | `"%s%d"` | `GetClassNameW, CONCAT31, GetFocus` | **Medium (Decompiled C Flow)** |
| `0x0046163e` | `FUN_0046163e` | 2 | 160 | `Core Subsystem Logic` | `"%s%u"` | `GetClassNameW, GetParent, GetWindowRect` | **High (Decompiled C Flow)** |
| `0x004619ea` | `FUN_004619ea` | 2 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004619fe` | `FUN_004619fe` | 3 | 21 | `Helper Subroutine` | `None` | `EnumChildWindows, CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00461a5b` | `FUN_00461a5b` | 5 | 75 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00461b9a` | `FUN_00461b9a` | 2 | 28 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00461c4a` | `FUN_00461c4a` | 2 | 39 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00461d2b` | `FUN_00461d2b` | 3 | 43 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00461dfa` | `FUN_00461dfa` | 2 | 55 | `Core Subsystem Logic` | `None` | `SendMessageW` | **High (Decompiled C Flow)** |
| `0x00461ee9` | `FUN_00461ee9` | 2 | 26 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00461f53` | `FUN_00461f53` | 3 | 53 | `Core Subsystem Logic` | `None` | `CONCAT31, SendMessageW` | **High (Decompiled C Flow)** |
| `0x00462034` | `FUN_00462034` | 3 | 31 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x004620ea` | `FUN_004620ea` | 2 | 28 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x0046216f` | `FUN_0046216f` | 1 | 38 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00462237` | `FUN_00462237` | 4 | 383 | `Core Subsystem Logic` | `"LF)", "BSR_ANYCRLF)", "ANYCRLF)"` | `CONCAT11` | **High (Decompiled C Flow)** |
| `0x0046297f` | `FUN_0046297f` | 4 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004629b7` | `FUN_004629b7` | 5 | 19 | `Helper Subroutine` | `None` | `DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x00462a31` | `FUN_00462a31` | 2 | 144 | `Core Subsystem Logic` | `None` | `CONCAT31, GetWindowLongW, IsDlgButtonChecked` | **High (Decompiled C Flow)** |
| `0x00462d06` | `FUN_00462d06` | 6 | 53 | `Core Subsystem Logic` | `None` | `CONCAT31, GetActiveWindow, EnumChildWindows` | **High (Decompiled C Flow)** |
| `0x00462dfd` | `FUN_00462dfd` | 2 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00462e96` | `FUN_00462e96` | 1 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00462f0c` | `FUN_00462f0c` | 2 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00462f4d` | `FUN_00462f4d` | 4 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00462f90` | `FUN_00462f90` | 4 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00462fc8` | `FUN_00462fc8` | 6 | 65 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x004630c5` | `FUN_004630c5` | 3 | 102 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x004632bc` | `FUN_004632bc` | 1 | 103 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00463514` | `FUN_00463514` | 1 | 32 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00463583` | `FUN_00463583` | 1 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004635f5` | `FUN_004635f5` | 1 | 37 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00463690` | `FUN_00463690` | 1 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004636fa` | `FUN_004636fa` | 1 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00463763` | `FUN_00463763` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046379b` | `FUN_0046379b` | 2 | 74 | `Core Subsystem Logic` | `");
            if ((char)uVar2 == '\0') {
              uVar2 = FUN_00445ae0((int)&stack0x0000000c,L", ");
          if ((char)uVar2 == '\0') {
            uVar2 = FUN_00445ae0((int)&stack0x0000000c,L", ");
              if ((char)uVar2 == '\0') {
                uVar2 = FUN_00445ae0((int)&stack0x0000000c,L"` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00463980` | `FUN_00463980` | 5 | 42 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00463a6d` | `FUN_00463a6d` | 3 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00463ad5` | `FUN_00463ad5` | 2 | 745 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x004646e0` | `FUN_004646e0` | 2 | 55 | `Core Subsystem Logic` | `",1,1,0xffffffff,-1,-1);
  if ((uVar1 != 0) && (uVar1 < (uint)param_1[1])) {
    FUN_0040bc70(&local_14);
    FUN_00461465(&local_14,param_1,uVar1 + 1,(param_1[1] - uVar1) + -1);
    FUN_0040c600(param_1,uVar1);
    uVar2 = FUN_00445ae0((int)&local_14,L", ");
      if ((char)uVar2 == '\0') {
        uVar2 = FUN_00445ae0((int)&local_14,L", ");
    if ((char)uVar2 == '\0') {
      uVar2 = FUN_00445ae0((int)&local_14,L"` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00464812` | `FUN_00464812` | 3 | 99 | `Core Subsystem Logic` | `None` | `FreeLibrary, GetProcAddress, LoadLibraryW` | **High (Decompiled C Flow)** |
| `0x004649a3` | `FUN_004649a3` | 5 | 211 | `Core Subsystem Logic` | `None` | `GetCurrentDirectoryW, CreateProcessW, CloseHandle` | **High (Decompiled C Flow)** |
| `0x00464e7c` | `FUN_00464e7c` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00464e95` | `FUN_00464e95` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00464eae` | `FUN_00464eae` | 3 | 101 | `Core Subsystem Logic` | `"SeDebugPrivilege"` | `TerminateProcess, GetLastError, GetCurrentProcess` | **High (Decompiled C Flow)** |
| `0x004650df` | `FUN_004650df` | 3 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00465124` | `FUN_00465124` | 6 | 25 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00465177` | `FUN_00465177` | 3 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004651a9` | `FUN_004651a9` | 2 | 26 | `Helper Subroutine` | `None` | `MultiByteToWideChar` | **Medium (Decompiled C Flow)** |
| `0x00465225` | `FUN_00465225` | 4 | 39 | `Helper Subroutine` | `"255.255.255.255"` | `CONCAT31, CONCAT22` | **Medium (Decompiled C Flow)** |
| `0x004652be` | `FUN_004652be` | 4 | 63 | `Core Subsystem Logic` | `None` | `WSAGetLastError` | **High (Decompiled C Flow)** |
| `0x004653c8` | `FUN_004653c8` | 4 | 47 | `Helper Subroutine` | `None` | `WSAGetLastError` | **Medium (Decompiled C Flow)** |
| `0x00465489` | `FUN_00465489` | 2 | 157 | `Core Subsystem Logic` | `None` | `GlobalFree, GlobalAlloc, WSACleanup` | **High (Decompiled C Flow)** |
| `0x004657fe` | `FUN_004657fe` | 3 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00465847` | `FUN_00465847` | 3 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004658b5` | `FUN_004658b5` | 3 | 46 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046596a` | `FUN_0046596a` | 3 | 59 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00465a62` | `FUN_00465a62` | 3 | 517 | `Core Subsystem Logic` | `"WinTitleMatchMode", "d0r0,3", "TrayAutoPause"` | `None` | **High (Decompiled C Flow)** |
| `0x00466552` | `FUN_00466552` | 3 | 89 | `Core Subsystem Logic` | `None` | `GetTime` | **High (Decompiled C Flow)** |
| `0x00466715` | `FUN_00466715` | 2 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00466734` | `FUN_00466734` | 4 | 36 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004667e1` | `FUN_004667e1` | 2 | 63 | `Core Subsystem Logic` | `None` | `InternetCrackUrlW, CONCAT31` | **High (Decompiled C Flow)** |
| `0x0046690e` | `FUN_0046690e` | 2 | 52 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00466a39` | `FUN_00466a39` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00466a4b` | `FUN_00466a4b` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00466a9a` | `FUN_00466a9a` | 3 | 57 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00466b71` | `FUN_00466b71` | 3 | 51 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00466c20` | `FUN_00466c20` | 4 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00466c7a` | `FUN_00466c7a` | 4 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00466cd4` | `FUN_00466cd4` | 3 | 50 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00466d83` | `FUN_00466d83` | 3 | 66 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x00466e47` | `FUN_00466e47` | 4 | 31 | `Helper Subroutine` | `None` | `CONCAT31, SUB84` | **Medium (Decompiled C Flow)** |
| `0x00466ec9` | `FUN_00466ec9` | 3 | 33 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00466f4a` | `FUN_00466f4a` | 3 | 24 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x00466faf` | `FUN_00466faf` | 2 | 22 | `Helper Subroutine` | `None` | `GetLastError` | **Medium (Decompiled C Flow)** |
| `0x00467001` | `FUN_00467001` | 2 | 43 | `Helper Subroutine` | `None` | `FindNextFileW` | **Medium (Decompiled C Flow)** |
| `0x00467131` | `FUN_00467131` | 1 | 29 | `Helper Subroutine` | `None` | `WNetGetConnectionW` | **Medium (Decompiled C Flow)** |
| `0x004671b9` | `FUN_004671b9` | 2 | 25 | `Helper Subroutine` | `None` | `Sleep, WNetCancelConnection2W` | **Medium (Decompiled C Flow)** |
| `0x00467215` | `FUN_00467215` | 2 | 106 | `Core Subsystem Logic` | `"LPT"` | `WNetUseConnectionW` | **High (Decompiled C Flow)** |
| `0x00467408` | `FUN_00467408` | 5 | 192 | `Core Subsystem Logic` | `");
  while (pwVar2 != (wchar_t *)0x0) {
    FUN_00402160();
    uVar4 = FUN_00431a2b(&iStack_302a0,(short *)&DAT_0048ab38);
    uStack_302a4 = uVar4;
    uVar5 = FUN_00431a2b(&iStack_302a0,(short *)&DAT_0048ab3c);
    uVar13 = (undefined1)unaff_EDI;
    if (((uVar4 == 0xffffffff) || (uVar5 == 0xffffffff)) || (uVar5 < uVar4)) {
      uVar12 = 0;
      goto LAB_00467823;
    }
    FUN_0040bd50(&iStack_302a0);
    FUN_0040d200();
    FUN_00461465(&iStack_30280,&iStack_302a0,uStack_302a4 + 1,(uVar5 - uStack_302a4) + -1);
    FUN_0040bd50(&iStack_30280);
    FUN_0040d200();
    pwVar2 = _wcstok((wchar_t *)0x0,L"` | `GetOpenFileNameW, GetSaveFileNameW, SUB84` | **High (Decompiled C Flow)** |
| `0x00467861` | `FUN_00467861` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046787c` | `FUN_0046787c` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00467897` | `FUN_00467897` | 4 | 116 | `Core Subsystem Logic` | `None` | `GetLastError` | **High (Decompiled C Flow)** |
| `0x00467a9d` | `FUN_00467a9d` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00467ac4` | `FUN_00467ac4` | 1 | 89 | `Core Subsystem Logic` | `None` | `CONCAT44, CONCAT31, CONCAT71` | **High (Decompiled C Flow)** |
| `0x00467c5c` | `FUN_00467c5c` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00467c75` | `FUN_00467c75` | 0 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00467c8e` | `FUN_00467c8e` | 2 | 220 | `Core Subsystem Logic` | `None` | `CONCAT31, SafeArrayUnaccessData, SafeArrayGetVartype` | **High (Decompiled C Flow)** |
| `0x00468070` | `FUN_00468070` | 2 | 34 | `Helper Subroutine` | `None` | `VariantCopy, VariantInit, VariantClear` | **Medium (Decompiled C Flow)** |
| `0x004680ed` | `FUN_004680ed` | 1 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046810f` | `FUN_0046810f` | 3 | 25 | `Helper Subroutine` | `None` | `LeaveCriticalSection, EnterCriticalSection, FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00468162` | `FUN_00468162` | 2 | 25 | `Helper Subroutine` | `None` | `LeaveCriticalSection, EnterCriticalSection, FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x004681c6` | `FUN_004681c6` | 3 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004681fd` | `FUN_004681fd` | 2 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046822a` | `FUN_0046822a` | 7 | 123 | `Core Subsystem Logic` | `None` | `CONCAT13, FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x004684dc` | `FUN_004684dc` | 6 | 194 | `Core Subsystem Logic` | `None` | `SUB82, SUB81, SUB84` | **High (Decompiled C Flow)** |
| `0x00468848` | `FUN_00468848` | 5 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046886c` | `FUN_0046886c` | 4 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046888b` | `FUN_0046888b` | 2 | 56 | `Core Subsystem Logic` | `None` | `OutputDebugStringW` | **High (Decompiled C Flow)** |
| `0x00468961` | `FUN_00468961` | 2 | 22 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x004689aa` | `FUN_004689aa` | 3 | 22 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x004689f4` | `FUN_004689f4` | 2 | 33 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00468a72` | `FUN_00468a72` | 1 | 43 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00468b0e` | `FUN_00468b0e` | 3 | 120 | `Core Subsystem Logic` | `",0xffffffff,0xffffffff,0);
      }
      piVar1[0x274] = 3;
      FUN_0045fbac(piVar1,0,(LPWSTR)piVar1[0x1f],0xffffffff,0xffffffff,0);
      piVar1[0x274] = 5;
      FUN_0045fbac(piVar1,0,L"` | `GetMenuItemInfoW, GetMenuItemCount, TrackPopupMenuEx` | **High (Decompiled C Flow)** |
| `0x00468d9e` | `FUN_00468d9e` | 6 | 122 | `Core Subsystem Logic` | `None` | `VkKeyScanW, CONCAT31` | **High (Decompiled C Flow)** |
| `0x00468f70` | `FUN_00468f70` | 3 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00468fe1` | `FUN_00468fe1` | 2 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046906d` | `FUN_0046906d` | 3 | 50 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00469143` | `FUN_00469143` | 4 | 46 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046921b` | `FUN_0046921b` | 2 | 13 | `Helper Subroutine` | `None` | `DialogBoxParamW` | **Medium (Decompiled C Flow)** |
| `0x00469251` | `FUN_00469251` | 4 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00469296` | `FUN_00469296` | 1 | 60 | `Core Subsystem Logic` | `"LAST", "ALL", "CLASSNAME="` | `None` | **High (Decompiled C Flow)** |
| `0x004693f5` | `FUN_004693f5` | 2 | 23 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0046943f` | `FUN_0046943f` | 3 | 163 | `Core Subsystem Logic` | `");
            if ((char)uVar5 != '\0') {
              lParam[0x22] = lParam[0x22] | 0x20;
              uVar5 = FUN_00413190(local_30[0]);
              lParam[0x33] = uVar5;
              goto LAB_004694d0;
            }
            uVar5 = FUN_00445ae0((int)local_20,L", ");
            if ((char)uVar5 != '\0') {
              lParam[0x22] = lParam[0x22] | 0x80;
              uVar5 = FUN_00413190(local_30[0]);
              lParam[0x38] = uVar5;
              goto LAB_004694d0;
            }
            uVar5 = FUN_00445ae0((int)local_20,L", "REGEXPCLASS"` | `CONCAT31, EnumChildWindows, FID_conflict___iswdigit_l` | **High (Decompiled C Flow)** |
| `0x00469839` | `FUN_00469839` | 3 | 34 | `Helper Subroutine` | `None` | `CONCAT31, SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x004698be` | `FUN_004698be` | 2 | 18 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x004698f8` | `FUN_004698f8` | 3 | 22 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x0046993e` | `FUN_0046993e` | 5 | 80 | `Core Subsystem Logic` | `None` | `CONCAT31, SendMessageW` | **High (Decompiled C Flow)** |
| `0x00469ae8` | `FUN_00469ae8` | 3 | 21 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00469b4b` | `FUN_00469b4b` | 2 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00469b64` | `FUN_00469b64` | 2 | 18 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00469bb5` | `FUN_00469bb5` | 2 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00469bf3` | `FUN_00469bf3` | 2 | 52 | `Core Subsystem Logic` | `None` | `CONCAT31, GetParent, SendMessageW` | **High (Decompiled C Flow)** |
| `0x00469cdb` | `FUN_00469cdb` | 1 | 57 | `Core Subsystem Logic` | `None` | `CONCAT31, SendMessageW` | **High (Decompiled C Flow)** |
| `0x00469df3` | `FUN_00469df3` | 2 | 52 | `Core Subsystem Logic` | `None` | `CONCAT31, GetParent, SendMessageW` | **High (Decompiled C Flow)** |
| `0x00469ed9` | `FUN_00469ed9` | 3 | 32 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00469f6a` | `FUN_00469f6a` | 2 | 31 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x00469ff3` | `FUN_00469ff3` | 2 | 31 | `Helper Subroutine` | `None` | `SendMessageW` | **Medium (Decompiled C Flow)** |
| `0x0046a07e` | `FUN_0046a07e` | 4 | 136 | `Core Subsystem Logic` | `None` | `GetMenuItemInfoW, GetFocus, GetMenuItemCount` | **High (Decompiled C Flow)** |
| `0x0046a38e` | `FUN_0046a38e` | 5 | 33 | `Helper Subroutine` | `None` | `DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x0046a42b` | `FUN_0046a42b` | 9 | 55 | `Core Subsystem Logic` | `None` | `CONCAT31, SetWindowLongW` | **High (Decompiled C Flow)** |
| `0x0046a533` | `FUN_0046a533` | 3 | 51 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046a5df` | `FUN_0046a5df` | 3 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046a604` | `FUN_0046a604` | 3 | 51 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046a6b3` | `FUN_0046a6b3` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046a6ca` | `FUN_0046a6ca` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046a6e1` | `FUN_0046a6e1` | 1 | 132 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046aa81` | `FUN_0046aa81` | 2 | 63 | `Core Subsystem Logic` | `None` | `FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x0046ab9c` | `FUN_0046ab9c` | 1 | 89 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046adb6` | `FUN_0046adb6` | 2 | 36 | `Helper Subroutine` | `None` | `FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0046ae3d` | `FUN_0046ae3d` | 2 | 17 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046ae76` | `FUN_0046ae76` | 4 | 66 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046afc3` | `FUN_0046afc3` | 3 | 65 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046b10f` | `FUN_0046b10f` | 6 | 81 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046b280` | `FUN_0046b280` | 2 | 100 | `Script / Win32 Host Logic` | `None` | `RegEnumValueW, RegCloseKey, RegConnectRegistryW` | **High (Verified Logic)** |
| `0x0046b4cf` | `FUN_0046b4cf` | 1 | 86 | `Script / Win32 Host Logic` | `None` | `RegConnectRegistryW, RegOpenKeyExW, RegEnumKeyExW` | **High (Verified Logic)** |
| `0x0046b6ab` | `FUN_0046b6ab` | 2 | 129 | `Script / Win32 Host Logic` | `None` | `RegDeleteValueW, RegCloseKey, RegConnectRegistryW` | **High (Verified Logic)** |
| `0x0046b9d7` | `FUN_0046b9d7` | 2 | 212 | `Core Subsystem Logic` | `";
        pwVar4 = (wchar_t *)FUN_0045340c(*(longlong **)(*(int *)(param_1 + 4) + 8));
        iVar5 = __wcsicmp(pwVar4,pwVar14);
        if (iVar5 == 0) {
          pwVar4 = (wchar_t *)FUN_0045340c(*(longlong **)(*(int *)(param_1 + 4) + 0xc));
          sVar6 = _wcslen(pwVar4);
          plVar11 = *(longlong **)(*(int *)(param_1 + 4) + 4);
          DVar15 = sVar6 * 2 + 2;
          pBVar7 = (BYTE *)FUN_0045340c(*(longlong **)(*(int *)(param_1 + 4) + 0xc));
          DVar13 = 2;
          DVar12 = 0;
          pWVar8 = (LPCWSTR)FUN_0045340c(plVar11);
          LVar3 = RegSetValueExW(local_58,pWVar8,DVar12,DVar13,pBVar7,DVar15);
          if (LVar3 == 0) goto LAB_0046be74;
LAB_0046be50:
LAB_0046be5c:
          FUN_00403cd0(LVar3,0);
        }
        else {
          pwVar14 = L", ";
          pwVar4 = (wchar_t *)FUN_0045340c(*(longlong **)(*(int *)(param_1 + 4) + 8));
          iVar5 = __wcsicmp(pwVar4,pwVar14);
          if (iVar5 == 0) {
            pwVar4 = (wchar_t *)FUN_0045340c(*(longlong **)(*(int *)(param_1 + 4) + 0xc));
            sVar6 = _wcslen(pwVar4);
            plVar11 = *(longlong **)(*(int *)(param_1 + 4) + 4);
            DVar15 = sVar6 * 2 + 2;
            pBVar7 = (BYTE *)FUN_0045340c(*(longlong **)(*(int *)(param_1 + 4) + 0xc));
            DVar12 = 1;
            goto LAB_0046bc53;
          }
          pwVar14 = L", ";
          pwVar4 = (wchar_t *)FUN_0045340c(*(longlong **)(*(int *)(param_1 + 4) + 8));
          iVar5 = __wcsicmp(pwVar4,pwVar14);
          if (iVar5 == 0) {
            uVar9 = FUN_004533b1(*(longlong **)(*(int *)(param_1 + 4) + 0xc));
            local_48._0_4_ = uVar9 + 2;
            pwVar4 = operator_new(-(uint)((int)((ulonglong)(uint)local_48 * 2 >> 0x20) != 0) |
                                  (uint)((ulonglong)(uint)local_48 * 2));
            iVar5 = uVar9 + 1;
            pwVar14 = (wchar_t *)FUN_0045340c(*(longlong **)(*(int *)(param_1 + 4) + 0xc));
            FUN_00433244(pwVar4,pwVar14,iVar5);
            uVar10 = 0;
            (pwVar4 + uVar9)[0] = L'\0';
            (pwVar4 + uVar9)[1] = L'\0';
            if (uVar9 != 0) {
              do {
                if (pwVar4[uVar10] == L'\n') {
                  pwVar4[uVar10] = L'\0';
                }
                uVar10 = uVar10 + 1;
              } while (uVar10 < uVar9);
              if (uVar9 != 0) {
                uVar9 = (uint)local_48;
              }
            }
            DVar15 = uVar9 * 2;
            DVar13 = 7;
            DVar12 = 0;
            pwVar14 = pwVar4;
            pWVar8 = (LPCWSTR)FUN_0045340c(*(longlong **)(*(int *)(param_1 + 4) + 4));
            LVar3 = RegSetValueExW(local_58,pWVar8,DVar12,DVar13,(BYTE *)pwVar14,DVar15);
            if (LVar3 != 0) {
              FUN_00403cd0(LVar3,0);
              FUN_00408f40();
              param_2[2] = 1;
              *param_2 = 0;
            }
            FUN_004111dc(pwVar4);
            goto LAB_0046be74;
          }
          pwVar14 = L"` | `CONCAT44, RegCloseKey, RegConnectRegistryW` | **High (Decompiled C Flow)** |
| `0x0046beb2` | `FUN_0046beb2` | 2 | 199 | `Script / Win32 Host Logic` | `None` | `RegConnectRegistryW, RegOpenKeyExW, RegQueryValueExW` | **High (Verified Logic)** |
| `0x0046c366` | `FUN_0046c366` | 2 | 53 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0046c43e` | `FUN_0046c43e` | 2 | 104 | `Core Subsystem Logic` | `None` | `CONCAT44` | **High (Decompiled C Flow)** |
| `0x0046c5fa` | `FUN_0046c5fa` | 3 | 118 | `Core Subsystem Logic` | `"NULL Pointer assignment", "Failed to create object", "Invalid parameter"` | `CoUninitialize, SUB81, CoInitialize` | **High (Decompiled C Flow)** |
| `0x0046c84c` | `FUN_0046c84c` | 4 | 138 | `Core Subsystem Logic` | `"get__NewEnum", "Null Object assignment in FOR..IN loop", "_NewEnum"` | `VariantClear, VariantInit` | **High (Decompiled C Flow)** |
| `0x0046cb5f` | `FUN_0046cb5f` | 6 | 165 | `Core Subsystem Logic` | `"NULL Pointer assignment"` | `CLSIDFromProgID, CoCreateInstanceEx, CoInitializeSecurity` | **High (Decompiled C Flow)** |
| `0x0046cef3` | `FUN_0046cef3` | 3 | 122 | `Core Subsystem Logic` | `None` | `GetActiveObject, CLSIDFromProgID, MkParseDisplayName` | **High (Decompiled C Flow)** |
| `0x0046d1a6` | `FUN_0046d1a6` | 4 | 29 | `Helper Subroutine` | `None` | `WSAGetLastError` | **Medium (Decompiled C Flow)** |
| `0x0046d230` | `FUN_0046d230` | 4 | 85 | `Core Subsystem Logic` | `None` | `WSAGetLastError, FID_conflict__memcpy, WSAFDIsSet` | **High (Decompiled C Flow)** |
| `0x0046d402` | `FUN_0046d402` | 1 | 36 | `Helper Subroutine` | `None` | `WSAGetLastError, FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x0046d4c2` | `FUN_0046d4c2` | 2 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046d4fc` | `FUN_0046d4fc` | 2 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046d536` | `FUN_0046d536` | 3 | 156 | `Core Subsystem Logic` | `None` | `GetLastError, RegisterHotKey, UnregisterHotKey` | **High (Decompiled C Flow)** |
| `0x0046d85a` | `FUN_0046d85a` | 3 | 248 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x0046dcb4` | `FUN_0046dcb4` | 0 | 118 | `Core Subsystem Logic` | `None` | `DragQueryFileW, IsClipboardFormatAvailable, OpenClipboard` | **High (Decompiled C Flow)** |
| `0x0046df7c` | `FUN_0046df7c` | 4 | 46 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046e042` | `FUN_0046e042` | 4 | 78 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046e1a6` | `FUN_0046e1a6` | 4 | 117 | `Core Subsystem Logic` | `">>>AUTOIT SCRIPT<<<", ");
  }
  _wcscpy((wchar_t *)local_428,local_18);
  _wcscat((wchar_t *)local_428,local_a3c);
  _wcscat((wchar_t *)local_428,local_21c);
  _wcscat((wchar_t *)local_428,local_62c);
  pwVar12 = local_838;
  pwVar7 = (wchar_t *)local_428;
  pwVar5 = L", ");
      pwVar12 = (wchar_t *)FUN_0045340c((longlong *)**(undefined4 **)(iVar8 + 4));
      _wcscat(local_21c,pwVar12);
    }
    pwVar12 = (wchar_t *)FUN_0045340c(*(longlong **)(*(int *)(iVar8 + 4) + 4));
    _wcscpy((wchar_t *)local_428,pwVar12);
    uVar10 = FUN_00433998((LPCWSTR)local_428);
    if (((char)uVar10 == '\0') ||
       (sVar4 = _wcslen((wchar_t *)local_428), (&sStack_42a)[sVar4] == 0x5c)) {
      cVar1 = '\0';
      uVar10 = FUN_0045340c(*(longlong **)(*(int *)(iVar8 + 4) + 4));
      cVar1 = FUN_0044bd27(local_21c,uVar10,(char)param_3,cVar1);
      if (cVar1 != '\0') {
        return 0;
      }
    }
LAB_0046e2c8:
    FUN_00408f40();
    param_4[2] = 1;
    *param_4 = 0;
    return 0;
  }
  iVar9 = FUN_0040f760(*(wchar_t **)(param_1 + 200));
  if (iVar9 != 0) {
    FUN_00403cd0(iVar9,0);
    goto LAB_0046e2c8;
  }
  pwVar7 = local_62c;
  pwVar6 = local_21c;
  pwVar11 = local_a3c;
  pwVar12 = local_18;
  pwVar5 = (wchar_t *)FUN_0045340c(*(longlong **)(*(int *)(iVar8 + 4) + 4));
  __wsplitpath(pwVar5,pwVar12,pwVar11,pwVar6,pwVar7);
  if ((local_21c[0] == L'\0') && (local_62c[0] == L'\0')) {
    _wcscpy(local_21c,L"` | `None` | **High (Decompiled C Flow)** |
| `0x0046e48d` | `FUN_0046e48d` | 2 | 147 | `Core Subsystem Logic` | `".lnk"` | `CONCAT31, CoUninitialize, CoInitialize` | **High (Decompiled C Flow)** |
| `0x0046e785` | `FUN_0046e785` | 4 | 95 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046e91c` | `FUN_0046e91c` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046e933` | `FUN_0046e933` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046e94a` | `FUN_0046e94a` | 3 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046e991` | `FUN_0046e991` | 2 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046e9ce` | `FUN_0046e9ce` | 2 | 22 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0046ea17` | `FUN_0046ea17` | 2 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046ea4a` | `FUN_0046ea4a` | 3 | 22 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0046ea94` | `FUN_0046ea94` | 3 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046eacf` | `FUN_0046eacf` | 2 | 96 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046ec4e` | `FUN_0046ec4e` | 4 | 58 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046ed8e` | `FUN_0046ed8e` | 8 | 263 | `Core Subsystem Logic` | `");
                  if ((char)uVar6 == '\0') {
                    uVar6 = FUN_00445ae0((int)local_38,L", ");
            if ((char)uVar6 == '\0') {
              uVar6 = FUN_00445ae0((int)local_38,L", ");
    if ((char)uVar6 == '\0') {
      uVar6 = FUN_00445ae0((int)local_38,L"` | `EnumChildWindows, GetDesktopWindow, EnumWindows` | **High (Decompiled C Flow)** |
| `0x0046f3c1` | `FUN_0046f3c1` | 2 | 53 | `Core Subsystem Logic` | `None` | `IsWindow, SUB84` | **High (Decompiled C Flow)** |
| `0x0046f46d` | `FUN_0046f46d` | 1 | 42 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046f59a` | `FUN_0046f59a` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046f5be` | `FUN_0046f5be` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046f5e2` | `FUN_0046f5e2` | 3 | 145 | `Core Subsystem Logic` | `None` | `VirtualAlloc, FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x0046f8cb` | `FUN_0046f8cb` | 3 | 55 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046f993` | `FUN_0046f993` | 3 | 103 | `Core Subsystem Logic` | `None` | `FID_conflict__memcpy` | **High (Decompiled C Flow)** |
| `0x0046fba4` | `FUN_0046fba4` | 2 | 96 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0046fd6c` | `FUN_0046fd6c` | 2 | 23 | `Helper Subroutine` | `None` | `CONCAT31` | **Medium (Decompiled C Flow)** |
| `0x0046fdbf` | `FUN_0046fdbf` | 1 | 33 | `Helper Subroutine` | `None` | `GetForegroundWindow` | **Medium (Decompiled C Flow)** |
| `0x0046fe32` | `FUN_0046fe32` | 1 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046fe6f` | `FUN_0046fe6f` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046fe90` | `FUN_0046fe90` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046feb1` | `FUN_0046feb1` | 1 | 35 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046ff07` | `FUN_0046ff07` | 1 | 15 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046ff3a` | `FUN_0046ff3a` | 1 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046ff4b` | `FUN_0046ff4b` | 3 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0046ffda` | `FUN_0046ffda` | 1 | 13 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047000b` | `FUN_0047000b` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00470028` | `FUN_00470028` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00470053` | `FUN_00470053` | 7 | 275 | `Core Subsystem Logic` | `None` | `CONCAT31, DispCallFunc, VariantCopy` | **High (Decompiled C Flow)** |
| `0x00470738` | `FUN_00470738` | 1 | 62 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00470870` | `FUN_00470870` | 2 | 52 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00470928` | `FUN_00470928` | 1 | 104 | `Core Subsystem Logic` | `None` | `DestroyIcon, ImageList_Destroy, DestroyWindow` | **High (Decompiled C Flow)** |
| `0x00470b6c` | `FUN_00470b6c` | 9 | 65 | `Core Subsystem Logic` | `None` | `VariantInit` | **High (Decompiled C Flow)** |
| `0x00470cc8` | `FUN_00470cc8` | 4 | 92 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00470e55` | `FUN_00470e55` | 1 | 21 | `Helper Subroutine` | `None` | `VariantClear` | **Medium (Decompiled C Flow)** |
| `0x00470e96` | `FUN_00470e96` | 2 | 84 | `Core Subsystem Logic` | `"\r\n"` | `DragQueryFileW, DragFinish, SendMessageW` | **High (Decompiled C Flow)** |
| `0x004710f1` | `FUN_004710f1` | 5 | 67 | `Core Subsystem Logic` | `None` | `SetWindowTextW, DefDlgProcW, ImageList_DragLeave` | **High (Decompiled C Flow)** |
| `0x004712f3` | `FUN_004712f3` | 4 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00471311` | `FUN_00471311` | 4 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047132f` | `FUN_0047132f` | 1 | 15 | `Helper Subroutine` | `None` | `DefDlgProcW` | **Medium (Decompiled C Flow)** |
| `0x00471359` | `FUN_00471359` | 10 | 53 | `Core Subsystem Logic` | `"static"` | `CONCAT31, DestroyWindow` | **High (Decompiled C Flow)** |
| `0x0047144e` | `FUN_0047144e` | 5 | 278 | `Core Subsystem Logic` | `None` | `GetClientRect, ExtractIconExW, DestroyIcon` | **High (Decompiled C Flow)** |
| `0x00471b57` | `FUN_00471b57` | 1 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00471bc9` | `FUN_00471bc9` | 8 | 152 | `Script / Win32 Host Logic` | `"AutoIt v3 GUI"` | `SystemParametersInfoW, CreateWindowExW, GetClientRect` | **High (Verified Logic)** |
| `0x00471f53` | `FUN_00471f53` | 2 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00471fac` | `FUN_00471fac` | 2 | 66 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x004720db` | `FUN_004720db` | 3 | 521 | `Core Subsystem Logic` | `";
    puVar12 = local_294;
    puVar6 = FUN_00441e23(local_2cc);
    FUN_00451aa8(puVar6,puVar12,pwVar13);
    FUN_0040e6a0();
    FUN_00402250(local_294);
    FUN_00402250(&param_3);
    return 0;
  case 7:
    pwVar13 = L", ",&local_274,0x104);
    break;
  case 0x54:
    GetEnvironmentVariableW(L", ",&local_274,0x104);
    break;
  default:
    goto switchD_004721da_caseD_57;
  case 0x59:
    iVar11 = *(int *)(uVar5 + 0x148);
    FUN_00408f40();
    pHVar3->unused = iVar11;
LAB_00472dad:
    pHVar3[2].unused = 1;
switchD_004721da_caseD_57:
    FUN_00402250(&param_3);
    return 0;
  case 0x5a:
    break;
  case 0x5b:
    param_2 = (HDC)GetCurrentProcessId();
    unique0x10000c65 = (double)(int)param_2;
    if ((int)param_2 < 0) {
      unique0x10000c55 = unique0x10000c65 + _DAT_0048cd18;
    }
    FUN_00408f40();
    *(double *)pHVar3 = stack0xfffffff4;
    pHVar3[2].unused = 3;
    FUN_00402250(&param_3);
    return 0;
  case 0x5f:
    FUN_0040f250(extraout_ECX,L"` | `GetCurrentDirectoryW, GetDeviceCaps, GetUserNameW` | **High (Decompiled C Flow)** |
| `0x00472f47` | `FUN_00472f47` | 2 | 141 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x004731e1` | `FUN_004731e1` | 3 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00473210` | `FUN_00473210` | 2 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00473253` | `FUN_00473253` | 4 | 72 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x004733b7` | `FUN_004733b7` | 2 | 86 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047354c` | `FUN_0047354c` | 1 | 36 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004735f4` | `FUN_004735f4` | 3 | 19 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00473636` | `FUN_00473636` | 3 | 24 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00473698` | `FUN_00473698` | 2 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004736c6` | `FUN_004736c6` | 2 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00473739` | `FUN_00473739` | 4 | 40 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004737e5` | `FUN_004737e5` | 4 | 76 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x0047390f` | `FUN_0047390f` | 2 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00473950` | `FUN_00473950` | 2 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00473a07` | `FUN_00473a07` | 1 | 35 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00473ad9` | `FUN_00473ad9` | 7 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00473b76` | `FUN_00473b76` | 0 | 28 | `Helper Subroutine` | `None` | `SafeArrayCreateVector, FID_conflict__memcpy` | **Medium (Decompiled C Flow)** |
| `0x00473bf3` | `FUN_00473bf3` | 9 | 286 | `Core Subsystem Logic` | `None` | `SelectObject, ReleaseDC, GetDC` | **High (Decompiled C Flow)** |
| `0x0047438b` | `FUN_0047438b` | 3 | 50 | `Helper Subroutine` | `None` | `GetCaretPos, GetForegroundWindow, ClientToScreen` | **Medium (Decompiled C Flow)** |
| `0x00474476` | `FUN_00474476` | 2 | 25 | `Helper Subroutine` | `None` | `GetTime` | **Medium (Decompiled C Flow)** |
| `0x004744d3` | `FUN_004744d3` | 1 | 102 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047469a` | `FUN_0047469a` | 1 | 103 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00474837` | `FUN_00474837` | 1 | 184 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00474d55` | `FUN_00474d55` | 2 | 61 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00474e7f` | `FUN_00474e7f` | 2 | 63 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00474fad` | `FUN_00474fad` | 4 | 53 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x00475077` | `FUN_00475077` | 4 | 258 | `Core Subsystem Logic` | `None` | `GetCurrentProcess, TerminateProcess, SUB84` | **High (Decompiled C Flow)** |
| `0x00475596` | `FUN_00475596` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004755ad` | `FUN_004755ad` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004755c4` | `FUN_004755c4` | 1 | 86 | `Core Subsystem Logic` | `None` | `Process32NextW, CreateToolhelp32Snapshot, CloseHandle` | **High (Decompiled C Flow)** |
| `0x004757a7` | `FUN_004757a7` | 2 | 138 | `Core Subsystem Logic` | `None` | `GetProcessIoCounters, GetCurrentProcessId, CloseHandle` | **High (Decompiled C Flow)** |
| `0x00475a67` | `FUN_00475a67` | 3 | 126 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00475cf6` | `FUN_00475cf6` | 3 | 245 | `Script / Win32 Host Logic` | `"Can\'t install a new Errorhandler when one is still active.", "Failed to create the Error Handler", "Incorrect Parameter format"` | `None` | **High (Verified Logic)** |
| `0x00476399` | `FUN_00476399` | 4 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004763ca` | `FUN_004763ca` | 3 | 49 | `Helper Subroutine` | `None` | `WSAGetLastError` | **Medium (Decompiled C Flow)** |
| `0x004764d1` | `FUN_004764d1` | 2 | 62 | `Core Subsystem Logic` | `None` | `WSAGetLastError` | **High (Decompiled C Flow)** |
| `0x00476619` | `FUN_00476619` | 4 | 76 | `Core Subsystem Logic` | `None` | `WSAGetLastError` | **High (Decompiled C Flow)** |
| `0x0047679f` | `FUN_0047679f` | 4 | 145 | `Core Subsystem Logic` | `None` | `FID_conflict__memcpy, WSAGetLastError, WSAFDIsSet` | **High (Decompiled C Flow)** |
| `0x00476b17` | `FUN_00476b17` | 3 | 67 | `Core Subsystem Logic` | `None` | `WSAGetLastError` | **High (Decompiled C Flow)** |
| `0x00476ca4` | `FUN_00476ca4` | 2 | 36 | `Helper Subroutine` | `None` | `Sleep, GlobalMemoryStatusEx` | **Medium (Decompiled C Flow)** |
| `0x00476d8d` | `FUN_00476d8d` | 3 | 59 | `Core Subsystem Logic` | `None` | `GetForegroundWindow, GetCursorPos` | **High (Decompiled C Flow)** |
| `0x00476e95` | `FUN_00476e95` | 4 | 156 | `Core Subsystem Logic` | `None` | `GetForegroundWindow, IsWindow, SUB84` | **High (Decompiled C Flow)** |
| `0x00477145` | `FUN_00477145` | 2 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00477167` | `FUN_00477167` | 3 | 54 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x0047722a` | `FUN_0047722a` | 2 | 56 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00477328` | `FUN_00477328` | 3 | 139 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x00477638` | `FUN_00477638` | 4 | 61 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00477749` | `FUN_00477749` | 4 | 103 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x00477927` | `FUN_00477927` | 2 | 60 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x00477a44` | `FUN_00477a44` | 4 | 94 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00477bcb` | `FUN_00477bcb` | 4 | 154 | `Core Subsystem Logic` | `None` | `WARNING` | **High (Decompiled C Flow)** |
| `0x00477f72` | `FUN_00477f72` | 2 | 71 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x004780be` | `FUN_004780be` | 1 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004780e6` | `FUN_004780e6` | 3 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00478115` | `FUN_00478115` | 2 | 12 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00478141` | `FUN_00478141` | 3 | 16 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00478172` | `FUN_00478172` | 2 | 105 | `Core Subsystem Logic` | `None` | `CONCAT31, SetErrorMode` | **High (Decompiled C Flow)** |
| `0x0047839d` | `FUN_0047839d` | 1 | 102 | `Core Subsystem Logic` | `".lnk"` | `CoUninitialize, CoInitialize, CoCreateInstance` | **High (Decompiled C Flow)** |
| `0x00478656` | `FUN_00478656` | 1 | 112 | `Core Subsystem Logic` | `"all", "network", "cdrom"` | `GetDriveTypeW` | **High (Decompiled C Flow)** |
| `0x004788bd` | `FUN_004788bd` | 1 | 115 | `Core Subsystem Logic` | `"%02d", "%4d", "%4d%02d%02d%02d%02d%02d"` | `FileTimeToLocalFileTime, FindFirstFileW, FileTimeToSystemTime` | **High (Decompiled C Flow)** |
| `0x00478b47` | `FUN_00478b47` | 2 | 86 | `Core Subsystem Logic` | `None` | `GetPrivateProfileSectionNamesW` | **High (Decompiled C Flow)** |
| `0x00478d00` | `FUN_00478d00` | 2 | 129 | `Core Subsystem Logic` | `None` | `WritePrivateProfileStringW, WritePrivateProfileSectionW` | **High (Decompiled C Flow)** |
| `0x00478f9a` | `FUN_00478f9a` | 2 | 134 | `Core Subsystem Logic` | `None` | `GetPrivateProfileSectionW` | **High (Decompiled C Flow)** |
| `0x00479230` | `FUN_00479230` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047925f` | `FUN_0047925f` | 2 | 58 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00479362` | `FUN_00479362` | 0 | 83 | `Core Subsystem Logic` | `None` | `VariantCopy, SafeArrayDestroyDescriptor, SafeArrayDestroyData` | **High (Decompiled C Flow)** |
| `0x00479500` | `FUN_00479500` | 4 | 104 | `Core Subsystem Logic` | `None` | `VariantCopy, SysAllocString, VariantInit` | **High (Decompiled C Flow)** |
| `0x00479714` | `FUN_00479714` | 1 | 20 | `Helper Subroutine` | `None` | `VariantClear` | **Medium (Decompiled C Flow)** |
| `0x0047974b` | `FUN_0047974b` | 6 | 184 | `Core Subsystem Logic` | `"NULL Pointer assignment", "Not an Object type"` | `ZEXT48, VariantClear, VariantInit` | **High (Decompiled C Flow)** |
| `0x00479b09` | `FUN_00479b09` | 3 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479c30` | `FUN_00479c30` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479c47` | `FUN_00479c47` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479c5e` | `FUN_00479c5e` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479c75` | `FUN_00479c75` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479c8c` | `FUN_00479c8c` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479ca3` | `FUN_00479ca3` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479cba` | `FUN_00479cba` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479cd1` | `FUN_00479cd1` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479ce8` | `FUN_00479ce8` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479cff` | `FUN_00479cff` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479d16` | `FUN_00479d16` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479d2d` | `FUN_00479d2d` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479d44` | `FUN_00479d44` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479d5b` | `FUN_00479d5b` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479d72` | `FUN_00479d72` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479d89` | `FUN_00479d89` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479da0` | `FUN_00479da0` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479db7` | `FUN_00479db7` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479dce` | `FUN_00479dce` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479de5` | `FUN_00479de5` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479dfc` | `FUN_00479dfc` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479e13` | `FUN_00479e13` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479e2a` | `FUN_00479e2a` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479e41` | `FUN_00479e41` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479e58` | `FUN_00479e58` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479e6f` | `FUN_00479e6f` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479e86` | `FUN_00479e86` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479e9d` | `FUN_00479e9d` | 3 | 11 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479eb4` | `FUN_00479eb4` | 3 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00479f2f` | `FUN_00479f2f` | 3 | 50 | `Helper Subroutine` | `None` | `FlashWindow` | **Medium (Decompiled C Flow)** |
| `0x0047a00c` | `FUN_0047a00c` | 3 | 37 | `Helper Subroutine` | `None` | `GetWindowThreadProcessId` | **Medium (Decompiled C Flow)** |
| `0x0047a09f` | `FUN_0047a09f` | 3 | 70 | `Core Subsystem Logic` | `None` | `GetWindowTextW` | **High (Decompiled C Flow)** |
| `0x0047a26a` | `FUN_0047a26a` | 4 | 37 | `Helper Subroutine` | `None` | `SetLayeredWindowAttributes, GetWindowLongW, SetWindowLongW` | **Medium (Decompiled C Flow)** |
| `0x0047a330` | `FUN_0047a330` | 3 | 56 | `Core Subsystem Logic` | `None` | `IsWindowVisible, IsIconic, IsWindowEnabled` | **High (Decompiled C Flow)** |
| `0x0047a3ee` | `FUN_0047a3ee` | 2 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047a4a5` | `FUN_0047a4a5` | 3 | 30 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047a515` | `FUN_0047a515` | 3 | 44 | `Helper Subroutine` | `None` | `GetClientRect` | **Medium (Decompiled C Flow)** |
| `0x0047a5ff` | `FUN_0047a5ff` | 2 | 27 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047a66e` | `FUN_0047a66e` | 3 | 98 | `Core Subsystem Logic` | `None` | `GetMenuItemCount, GetMenu, GetMenuItemID` | **High (Decompiled C Flow)** |
| `0x0047a8b6` | `FUN_0047a8b6` | 3 | 54 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047a9cd` | `FUN_0047a9cd` | 3 | 38 | `Helper Subroutine` | `None` | `SetWindowPos` | **Medium (Decompiled C Flow)** |
| `0x0047aa6e` | `FUN_0047aa6e` | 2 | 69 | `Core Subsystem Logic` | `None` | `SUB84` | **High (Decompiled C Flow)** |
| `0x0047abd3` | `FUN_0047abd3` | 3 | 31 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047ac6d` | `FUN_0047ac6d` | 3 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047acf9` | `FUN_0047acf9` | 3 | 35 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047ad67` | `FUN_0047ad67` | 3 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047add6` | `FUN_0047add6` | 3 | 25 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047ae43` | `FUN_0047ae43` | 3 | 105 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047b042` | `FUN_0047b042` | 3 | 36 | `Helper Subroutine` | `None` | `ShowWindow` | **Medium (Decompiled C Flow)** |
| `0x0047b0f7` | `FUN_0047b0f7` | 3 | 45 | `Helper Subroutine` | `None` | `GetForegroundWindow` | **Medium (Decompiled C Flow)** |
| `0x0047b1db` | `FUN_0047b1db` | 3 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047b226` | `FUN_0047b226` | 3 | 28 | `Helper Subroutine` | `None` | `GetForegroundWindow` | **Medium (Decompiled C Flow)** |
| `0x0047b291` | `FUN_0047b291` | 6 | 22 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047b2f4` | `FUN_0047b2f4` | 4 | 28 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047b359` | `FUN_0047b359` | 2 | 103 | `Core Subsystem Logic` | `None` | `CONCAT44, SUB84` | **High (Decompiled C Flow)** |
| `0x0047b52c` | `FUN_0047b52c` | 3 | 23 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047b588` | `FUN_0047b588` | 3 | 35 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047b623` | `FUN_0047b623` | 3 | 137 | `Core Subsystem Logic` | `"EXPAND", "COLLAPSE", "GETITEMCOUNT"` | `None` | **High (Decompiled C Flow)** |
| `0x0047b954` | `FUN_0047b954` | 3 | 166 | `Core Subsystem Logic` | `"SELECTINVERT", "GETITEMCOUNT", "SELECT"` | `None` | **High (Decompiled C Flow)** |
| `0x0047bd15` | `FUN_0047bd15` | 3 | 238 | `Core Subsystem Logic` | `"ISVISIBLE", "GETSELECTED", "GETCURRENTCOL"` | `None` | **High (Decompiled C Flow)** |
| `0x0047c296` | `FUN_0047c296` | 3 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047c2db` | `FUN_0047c2db` | 3 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047c320` | `FUN_0047c320` | 3 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047c365` | `FUN_0047c365` | 3 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047c3aa` | `FUN_0047c3aa` | 3 | 58 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047c496` | `FUN_0047c496` | 3 | 55 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047c5ba` | `FUN_0047c5ba` | 2 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047c65d` | `FUN_0047c65d` | 3 | 35 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047c6d0` | `FUN_0047c6d0` | 3 | 66 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047c7dc` | `FUN_0047c7dc` | 3 | 20 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047c81c` | `FUN_0047c81c` | 3 | 318 | `Core Subsystem Logic` | `None` | `GetParent, ImageList_SetDragCursorImage, ImageList_BeginDrag` | **High (Decompiled C Flow)** |
| `0x0047d2a5` | `FUN_0047d2a5` | 2 | 42 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047d33e` | `FUN_0047d33e` | 4 | 47 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047d40f` | `FUN_0047d40f` | 3 | 79 | `Core Subsystem Logic` | `None` | `Sleep, InterlockedDecrement, InterlockedIncrement` | **High (Decompiled C Flow)** |
| `0x0047d583` | `FUN_0047d583` | 7 | 72 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047d79b` | `FUN_0047d79b` | 2 | 235 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047dcbb` | `FUN_0047dcbb` | 4 | 55 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047ddc2` | `FUN_0047ddc2` | 5 | 93 | `Core Subsystem Logic` | `"AUTOITCALLVARIABLE%d", "CALLARGARRAY"` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0047dfb9` | `FUN_0047dfb9` | 1 | 29 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047e012` | `FUN_0047e012` | 1 | 42 | `Helper Subroutine` | `None` | `SUB84` | **Medium (Decompiled C Flow)** |
| `0x0047e0f9` | `FUN_0047e0f9` | 2 | 69 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047e250` | `FUN_0047e250` | 3 | 117 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047e4e3` | `FUN_0047e4e3` | 3 | 39 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047e5aa` | `FUN_0047e5aa` | 7 | 59 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0047e6ac` | `FUN_0047e6ac` | 3 | 85 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047e844` | `FUN_0047e844` | 6 | 115 | `Core Subsystem Logic` | `"GUI_RUNDEFMSG"` | `None` | **High (Decompiled C Flow)** |
| `0x0047ea6f` | `FUN_0047ea6f` | 4 | 165 | `Core Subsystem Logic` | `None` | `DefDlgProcW` | **High (Decompiled C Flow)** |
| `0x0047f096` | `FUN_0047f096` | 3 | 34 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0047f135` | `FUN_0047f135` | 4 | 135 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047f38e` | `FUN_0047f38e` | 3 | 170 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047f68a` | `FUN_0047f68a` | 2 | 101 | `Core Subsystem Logic` | `None` | `CONCAT31, CONCAT13` | **High (Decompiled C Flow)** |
| `0x0047f85e` | `FUN_0047f85e` | 3 | 73 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047f9a6` | `FUN_0047f9a6` | 3 | 69 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x0047faae` | `FUN_0047faae` | 4 | 122 | `Core Subsystem Logic` | `";
  FUN_00408e80(param_4);
  while( true ) {
    if (*(short *)(*(int *)((param_2->n1).decVal.Hi32 + *(int *)pwVar3 * 4) + 8) != 0x48) {
      FUN_0046fe32((int)&local_3c);
      puVar2 = *(undefined4 **)((param_2->n1).decVal.Hi32 + *(int *)pwVar3 * 4);
      if (*(short *)(puVar2 + 2) == 0x47) {
        param_3 = L"` | `None` | **High (Decompiled C Flow)** |
| `0x0047fcff` | `FUN_0047fcff` | 6 | 104 | `Core Subsystem Logic` | `None` | `CONCAT31` | **High (Decompiled C Flow)** |
| `0x0047fea2` | `FUN_0047fea2` | 4 | 351 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x004805bf` | `FUN_004805bf` | 4 | 245 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00480a8d` | `FUN_00480a8d` | 4 | 303 | `Core Subsystem Logic` | `None` | `None` | **High (Decompiled C Flow)** |
| `0x00481167` | `FUN_00481167` | 3 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004811c5` | `FUN_004811c5` | 3 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00481221` | `FUN_00481221` | 3 | 21 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0048127d` | `FUN_0048127d` | 3 | 44 | `Helper Subroutine` | `None` | `OpenProcess` | **Medium (Decompiled C Flow)** |
| `0x0048136b` | `FUN_0048136b` | 3 | 26 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004813fa` | `FUN_004813fa` | 2 | 37 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004814b8` | `FUN_004814b8` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x00481511` | `FUN_00481511` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x0048156a` | `FUN_0048156a` | 2 | 18 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
| `0x004815c3` | `FUN_004815c3` | 2 | 14 | `Helper Subroutine` | `None` | `None` | **Medium (Decompiled C Flow)** |
