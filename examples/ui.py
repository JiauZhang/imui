from imui.sdl import (
    SDL_Init,
    SDL_GetError,
    SDL_GetPrimaryDisplay,
    SDL_GetDisplayContentScale,
    SDL_CreateWindow,

    SDL_INIT_VIDEO,
    SDL_INIT_GAMEPAD,

    SDL_WINDOW_RESIZABLE,
    SDL_WINDOW_HIDDEN,
    SDL_WINDOW_HIGH_PIXEL_DENSITY,
)

if not SDL_Init(SDL_INIT_VIDEO | SDL_INIT_GAMEPAD):
    print(f'Error: SDL_Init(): {SDL_GetError()}')
    exit(-1)

display_id = SDL_GetPrimaryDisplay()
main_scale = SDL_GetDisplayContentScale(display_id)
window_flags = SDL_WINDOW_RESIZABLE | SDL_WINDOW_HIDDEN | SDL_WINDOW_HIGH_PIXEL_DENSITY
window = SDL_CreateWindow("Dear ImGui SDL3+SDL_GPU example", (int)(1280 * main_scale), (int)(720 * main_scale), window_flags)
if not window:
    print(f'Error: SDL_CreateWindow(): {SDL_GetError()}')
    exit(-1)