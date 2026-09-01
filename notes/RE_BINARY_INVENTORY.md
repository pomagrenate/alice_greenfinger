# ALICE GREENFINGERS - COMPLETE BINARY INVENTORY (STEP 1)

*Generated on 2026-09-01 13:07:41*

## AliceGreenfingers.exe (Unpacked Executable)
- **File Size:** 732,733 bytes
- **Architecture:** x86 (32-bit)
- **Image Base:** `0x400000`
- **Address of Entry Point (RVA):** `0x165c1`
- **TLS Directory Present:** `False`
- **Base Relocations Present:** `False`
- **Resource Directory Entry Count:** 22
- **Imported DLL Count:** 16
- **Exported Symbol Count:** 0

### Memory Sections & Characteristics
| Section Name | Virtual Address | Virtual Size | Raw Size | Executable | Readable | Writable | Characteristics |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `.text` | `0x1000` | `0x8061c` | `0x80800` | `True` | `True` | `False` | `0x60000020` |
| `.rdata` | `0x82000` | `0xdfc0` | `0xe000` | `False` | `True` | `False` | `0x40000040` |
| `.data` | `0x90000` | `0x1a758` | `0x6800` | `False` | `True` | `True` | `0xc0000040` |
| `.rsrc` | `0xab000` | `0x1d7e8` | `0x1d800` | `False` | `True` | `False` | `0x40000040` |

### Imported Libraries & Functions (Summary)
- **`KERNEL32.DLL`** (159 functions imported): `HeapAlloc, Sleep, GetCurrentThreadId, RaiseException, MulDiv, GetVersionExW...`
- **`ADVAPI32.dll`** (34 functions imported): `RegEnumValueW, RegDeleteValueW, RegDeleteKeyW, RegEnumKeyExW, RegSetValueExW, RegCreateKeyExW...`
- **`COMCTL32.dll`** (11 functions imported): `ImageList_Remove, ImageList_SetDragCursorImage, ImageList_BeginDrag, ImageList_DragEnter, ImageList_DragLeave, ImageList_EndDrag...`
- **`COMDLG32.dll`** (2 functions imported): `GetSaveFileNameW, GetOpenFileNameW`
- **`GDI32.dll`** (35 functions imported): `DeleteObject, AngleArc, GetTextExtentPoint32W, ExtCreatePen, StrokeAndFillPath, StrokePath...`
- **`MPR.dll`** (4 functions imported): `WNetCancelConnection2W, WNetGetConnectionW, WNetAddConnection2W, WNetUseConnectionW`
- **`ole32.dll`** (20 functions imported): `OleSetMenuDescriptor, MkParseDisplayName, OleSetContainedObject, CLSIDFromString, StringFromGUID2, CoInitialize...`
- **`OLEAUT32.dll`** (24 functions imported): `VariantChangeType, VariantCopyInd, DispCallFunc, CreateStdDispatch, CreateDispTypeInfo, SysFreeString...`
- **`PSAPI.DLL`** (4 functions imported): `EnumProcesses, GetModuleBaseNameW, GetProcessMemoryInfo, EnumProcessModules`
- **`SHELL32.dll`** (14 functions imported): `DragQueryPoint, ShellExecuteExW, SHGetFolderPathW, DragQueryFileW, SHEmptyRecycleBinW, SHBrowseForFolderW...`
- **`USER32.dll`** (160 functions imported): `GetCursorInfo, RegisterHotKey, ClientToScreen, GetKeyboardLayoutNameW, IsCharAlphaW, IsCharAlphaNumericW...`
- **`USERENV.dll`** (4 functions imported): `CreateEnvironmentBlock, DestroyEnvironmentBlock, UnloadUserProfile, LoadUserProfileW`
- **`VERSION.dll`** (3 functions imported): `VerQueryValueW, GetFileVersionInfoW, GetFileVersionInfoSizeW`
- **`WININET.dll`** (14 functions imported): `InternetReadFile, InternetCloseHandle, InternetOpenW, InternetSetOptionW, InternetCrackUrlW, HttpQueryInfoW...`
- **`WINMM.dll`** (3 functions imported): `timeGetTime, waveOutSetVolume, mciSendStringW`

---

## AliceGreenfingers.dll (Core Engine DLL)
- **File Size:** 496,974 bytes
- **Architecture:** x86 (32-bit)
- **Image Base:** `0x400000`
- **Address of Entry Point (RVA):** `0x30fd8`
- **TLS Directory Present:** `False`
- **Base Relocations Present:** `False`
- **Resource Directory Entry Count:** 12
- **Imported DLL Count:** 8
- **Exported Symbol Count:** 0

### Memory Sections & Characteristics
| Section Name | Virtual Address | Virtual Size | Raw Size | Executable | Readable | Writable | Characteristics |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `.text` | `0x1000` | `0x38a92` | `0x39000` | `True` | `True` | `False` | `0x60000020` |
| `.rdata` | `0x3a000` | `0x1d00` | `0x2000` | `False` | `True` | `False` | `0x40000040` |
| `.data` | `0x3c000` | `0x60d89c` | `0x5000` | `False` | `True` | `True` | `0xc0000040` |
| `.rsrc` | `0x64a000` | `0x36004` | `0x37000` | `False` | `True` | `False` | `0x40000040` |

### Imported Libraries & Functions (Summary)
- **`KERNEL32.dll`** (65 functions imported): `CompareStringW, CompareStringA, GetCPInfo, IsBadCodePtr, IsBadReadPtr, SetUnhandledExceptionFilter...`
- **`USER32.dll`** (37 functions imported): `SetCapture, ReleaseCapture, SetWindowPos, SetWindowLongA, AdjustWindowRect, ClientToScreen...`
- **`GDI32.dll`** (9 functions imported): `SelectObject, GetStockObject, GetTextExtentPoint32A, SetBkMode, SetTextColor, CreateFontA...`
- **`ADVAPI32.dll`** (14 functions imported): `AccessCheck, OpenThreadToken, OpenProcessToken, DuplicateToken, AllocateAndInitializeSid, InitializeSecurityDescriptor...`
- **`SHELL32.dll`** (1 functions imported): `ShellExecuteA`
- **`WINMM.dll`** (2 functions imported): `timeGetTime, joyGetPos`
- **`fmod.dll`** (20 functions imported): `_FSOUND_Sample_Load@20, _FSOUND_StopSound@4, _FSOUND_Sample_Free@4, _FMUSIC_SetOrder@8, _FMUSIC_PlaySong@4, _FMUSIC_SetLooping@8...`
- **`DDRAW.dll`** (1 functions imported): `DirectDrawCreate`

---

## fmod.dll (Audio Subsystem DLL)
- **File Size:** 162,816 bytes
- **Architecture:** x86 (32-bit)
- **Image Base:** `0x10000000`
- **Address of Entry Point (RVA):** `0x92d10`
- **TLS Directory Present:** `False`
- **Base Relocations Present:** `True`
- **Resource Directory Entry Count:** 1
- **Imported DLL Count:** 8
- **Exported Symbol Count:** 232

### Memory Sections & Characteristics
| Section Name | Virtual Address | Virtual Size | Raw Size | Executable | Readable | Writable | Characteristics |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `UPX0` | `0x1000` | `0x6d000` | `0x0` | `True` | `True` | `True` | `0xe0000080` |
| `UPX1` | `0x6e000` | `0x25000` | `0x25000` | `True` | `True` | `True` | `0xe0000040` |
| `.rsrc` | `0x93000` | `0x3000` | `0x2800` | `False` | `True` | `True` | `0xc0000040` |

### Imported Libraries & Functions (Summary)
- **`KERNEL32.DLL`** (2 functions imported): `LoadLibraryA, GetProcAddress`
- **`ADVAPI32.dll`** (1 functions imported): `RegCloseKey`
- **`MSACM32.dll`** (1 functions imported): `acmStreamOpen`
- **`MSVCRT.dll`** (1 functions imported): `abs`
- **`ole32.dll`** (1 functions imported): `CoInitialize`
- **`USER32.dll`** (1 functions imported): `ShowWindow`
- **`WINMM.dll`** (1 functions imported): `mixerOpen`
- **`WSOCK32.dll`** (1 functions imported): `inet_ntoa`

### Exported Functions
- `_FMUSIC_FreeSong@4` at `0x20626`
- `_FMUSIC_GetBPM@4` at `0x21813`
- `_FMUSIC_GetGlobalVolume@4` at `0x2174b`
- `_FMUSIC_GetMasterVolume@4` at `0x2170b`
- `_FMUSIC_GetName@4` at `0x2141d`
- `_FMUSIC_GetNumChannels@4` at `0x21628`
- `_FMUSIC_GetNumInstruments@4` at `0x215aa`
- `_FMUSIC_GetNumOrders@4` at `0x21536`
- `_FMUSIC_GetNumPatterns@4` at `0x21575`
- `_FMUSIC_GetNumSamples@4` at `0x215e9`
- `_FMUSIC_GetOpenState@4` at `0x21d11`
- `_FMUSIC_GetOrder@4` at `0x21853`
- `_FMUSIC_GetPattern@4` at `0x2178b`
- `_FMUSIC_GetPatternLength@8` at `0x216b9`
- `_FMUSIC_GetPaused@4` at `0x2197b`
- `_FMUSIC_GetRealChannel@8` at `0x219ba`
- `_FMUSIC_GetRow@4` at `0x218a9`
- `_FMUSIC_GetSample@8` at `0x21667`
- `_FMUSIC_GetSpeed@4` at `0x217d3`
- `_FMUSIC_GetTime@4` at `0x21900`

---

