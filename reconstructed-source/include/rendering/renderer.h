// ==========================================================================
// ALICE GREENFINGERS - SOFTWARE BACKBUFFER RENDERER
// ==========================================================================

#pragma once
#ifndef RENDERER_H
#define RENDERER_H

#include <stdint.h>
#include "rendering/render_state.h"

#ifdef __cplusplus
extern "C" {
#endif

#define RENDER_WIDTH  800
#define RENDER_HEIGHT 600

void Renderer_Initialize(void);
void Renderer_Shutdown(void);
void Renderer_RenderFrame(const RenderState* state);
const uint32_t* Renderer_GetBackbuffer(void);
uint32_t Renderer_GetTotalFramesRendered(void);

#ifdef __cplusplus
}
#endif

#endif // RENDERER_H
