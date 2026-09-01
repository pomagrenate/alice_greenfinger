// ==========================================================================
// ALICE GREENFINGERS - RENDERING BOUNDARY
// Evidence: notes/RENDERING_ARCHITECTURE.md
// ==========================================================================

#pragma once
#ifndef DIRECTDRAW_BOUNDARY_H
#define DIRECTDRAW_BOUNDARY_H

#include "generated/recovered_types.h"

#ifdef __cplusplus
extern "C" {
#endif

void Render_InitSurfaces(void);
void Render_BlitTerrainLayer(void);
void Render_BlitSpriteLayer(void);
void Render_BlitGuiOverlay(void);
void Render_FlipSurface(void);
void Render_ShutdownSurfaces(void);

#ifdef __cplusplus
}
#endif

#endif // DIRECTDRAW_BOUNDARY_H
