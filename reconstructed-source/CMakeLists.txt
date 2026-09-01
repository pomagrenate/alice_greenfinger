cmake_minimum_required(VERSION 3.15)
project(alice_greenfingers_reconstructed C CXX)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${CMAKE_CURRENT_SOURCE_DIR}/generated
    ${CMAKE_CURRENT_SOURCE_DIR}
)

set(RECONSTRUCTED_SOURCES
    src/objects/engine_context.cpp
    src/globals/recovered_globals.cpp
    src/state/game_state.cpp
    src/events/event_dispatcher.cpp
    src/engine/game_loop.cpp
    src/resources/resource_loader.cpp
    src/rendering/directdraw_boundary.cpp
    src/rendering/renderer.cpp
    src/rendering/animation.cpp
    src/audio/fmod_system.cpp
    src/platform/win32_boundary.cpp
    src/platform/window.cpp
    src/platform/input.cpp
    src/recovered/recovered_group_a.cpp
    unresolved/unresolved_calls.cpp
)

# Reconstructed Core Static Library
add_library(alice_reconstructed STATIC ${RECONSTRUCTED_SOURCES})

# Reconstructed Executable Target
add_executable(alice_greenfingers_reconstructed
    src/main.cpp
)
target_link_libraries(alice_greenfingers_reconstructed PRIVATE alice_reconstructed gdi32 user32)
