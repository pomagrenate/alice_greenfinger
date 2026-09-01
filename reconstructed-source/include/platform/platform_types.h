// ==========================================================================
// ALICE GREENFINGERS - PLATFORM PRIMITIVE TYPES
// ==========================================================================

#pragma once
#ifndef PLATFORM_TYPES_H
#define PLATFORM_TYPES_H

#include "generated/recovered_types.h"

#ifdef _WIN32
#include <windows.h>
#else
typedef void* HWND;
typedef void* HINSTANCE;
typedef void* HMODULE;
typedef char* LPSTR;
#define WINAPI
#endif

#endif // PLATFORM_TYPES_H
