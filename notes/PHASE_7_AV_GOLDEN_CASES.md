# ALICE GREENFINGERS - GOLDEN AV SCENARIOS (STEP 16)

*Generated on 2026-09-01 17:54:18*

## DETERMINISTIC AUDIO-VISUAL GOLDEN SCENARIOS

| Scenario ID | Scenario Name | Trigger Action | Expected Visual / Audio State | Result |
| :--- | :--- | :--- | :--- | :---: |
| `AV-01` | Startup Presentation | `Platform_Initialize()` | `STATE_STARTUP (0)` | **[PASS]** |
| `AV-02` | Main Menu Presentation | `State_SetState(STATE_MAIN_MENU)` | `STATE_MAIN_MENU (1)` | **[PASS]** |
| `AV-03` | Farm Presentation & Soil Grid | `State_SetState(STATE_GAMEPLAY)` | `5x8 Soil Grid Rendered` | **[PASS]** |
| `AV-04` | Plant Growth Visual Animation | `Animation_GetActiveSprite()` | `Sprout to Ripe Crop` | **[PASS]** |
| `AV-05` | Harvest Presentation & Cash Increment | `DAT_004a86a4 += 50` | `Balance 130` | **[PASS]** |
| `AV-06` | Market Stalls Presentation | `State_SetState(STATE_SHOP_MARKET)` | `STATE_SHOP_MARKET (5)` | **[PASS]** |
| `AV-07` | GUI Interaction & Cursor Blit | `Renderer_RenderFrame()` | `Cursor Indicator Drawn` | **[PASS]** |
| `AV-08` | Asset Container LBTC Reload | `Resource_LoadGfxArchive()` | `Handle 0x00497528` | **[PASS]** |
| `AV-09` | Audio Host Activation | `Audio_InitFMOD()` | `DAT_004b1200 == 1` | **[PASS]** |
| `AV-10` | Audio-Disabled Headless Fallback | `Audio_ShutdownFMOD()` | `DAT_004b1200 == 0` | **[PASS]** |
