# Alice Greenfingers - Linux & POSIX Build Guide (Phase 12)

## 1. Prerequisites
- **Compiler:** GCC 9+ or Clang 10+ (supporting C++17)
- **Build Generator:** CMake 3.15+ and Ninja or Make
- **Libraries:** SDL2 development packages (`libsdl2-dev`)

## 2. Build Instructions
```bash
# Clone or navigate to the repository
cd AliceGreenfingers_RE

# Configure CMake with SDL2 backend
cmake -S reconstructed-source -B build-linux -G Ninja -DCMAKE_BUILD_TYPE=Release

# Compile standalone Linux binary
cmake --build build-linux
```

## 3. Running the Portable Linux Executable
```bash
./build-linux/alice_greenfingers_reconstructed
```
