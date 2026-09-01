# Alice Greenfingers - Game State Machine Reference

| State ID | Enum Identifier | Primary Presentation | Valid Transitions |
| :---: | :--- | :--- | :--- |
| `0` | `STATE_STARTUP` | Dark splash / initialization | `STATE_MAIN_MENU` (1) |
| `1` | `STATE_MAIN_MENU` | Title screen, Start button | `STATE_NAME_DIALOG` (2), `STATE_GAMEPLAY` (3) |
| `2` | `STATE_NAME_DIALOG` | Player profile name entry modal | `STATE_GAMEPLAY` (3) |
| `3` | `STATE_GAMEPLAY` | Main 5x8 farm grid simulation | `STATE_PAUSE_OPTIONS` (4), `STATE_SHOP_MARKET` (5) |
| `4` | `STATE_PAUSE_OPTIONS` | Pause overlay and audio volume settings | `STATE_GAMEPLAY` (3) |
| `5` | `STATE_SHOP_MARKET` | Town market stall purchasing & selling | `STATE_GAMEPLAY` (3) |
