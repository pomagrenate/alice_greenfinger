// ==========================================================================
// ALICE GREENFINGERS - RECONSTRUCTED C++ SOURCE CODE (EXE WRAPPER)
// Reconstructed from AliceGreenfingers.exe PE Executable Entry Point
// ==========================================================================

#include "Original_Structures_And_Globals.hpp"

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    // 1. Initialize PopCap SexyAppFramework Engine
    // 2. Load AliceGreenfingers.dll dynamically
    HMODULE hDll = LoadLibraryA("AliceGreenfingers.dll");
    if (!hDll) return -1;

    typedef void(__stdcall *StartGameFunc)();
    StartGameFunc pStart = (StartGameFunc)GetProcAddress(hDll, "StartGame");
    if (pStart) pStart();

    FreeLibrary(hDll);
    return 0;
}
