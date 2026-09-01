cmake_minimum_required(VERSION 3.15)
project(alice_greenfingers_reconstructed VERSION 1.0.0 LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

include_directories(include .)
include_directories(unresolved)

# Source File Groups
set(CORE_SOURCES
    src/state/game_state.cpp
    src/engine/game_loop.cpp
    src/events/event_dispatcher.cpp
    src/resources/resource_loader.cpp
    src/rendering/renderer.cpp
    src/rendering/animation.cpp
    src/rendering/directdraw_boundary.cpp
    src/audio/fmod_system.cpp
    src/platform/input.cpp
    src/platform/win32_boundary.cpp
    src/platform/window.cpp
    src/platform/sdl2_window.cpp
    src/globals/recovered_globals.cpp
    src/objects/engine_context.cpp
    src/recovered/recovered_group_a.cpp
    unresolved/unresolved_calls.cpp
)

add_library(alice_reconstructed STATIC ${CORE_SOURCES})

# Target Executable
add_executable(alice_greenfingers_reconstructed src/main.cpp)
target_link_libraries(alice_greenfingers_reconstructed PRIVATE alice_reconstructed)

if (WIN32)
    target_link_libraries(alice_greenfingers_reconstructed PRIVATE gdi32 user32)
endif()
