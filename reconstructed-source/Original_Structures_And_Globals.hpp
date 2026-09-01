// ==========================================================================
// ALICE GREENFINGERS - RECONSTRUCTED NATIVE C++ STRUCTURES & GLOBALS
// Recovered from AliceGreenfingers.dll & SexyAppFramework
// ==========================================================================

#ifndef ORIGINAL_STRUCTURES_AND_GLOBALS_HPP_
#define ORIGINAL_STRUCTURES_AND_GLOBALS_HPP_

#include <windows.h>
#include <cstdint>

namespace original {

struct SexyAppBase {
    void* vtable;
    uint32_t mWidth;
    uint32_t mHeight;
    bool mIsWindowed;
};

struct AliceGameApp : public SexyAppBase {
    uint32_t mGold;
    uint32_t mDayNumber;
    float mDayTimer;
};

} // namespace original

#endif // ORIGINAL_STRUCTURES_AND_GLOBALS_HPP_
