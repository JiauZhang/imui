from imui.sdl import (
    SDL_Init,
    SDL_GetError,
    SDL_GetPrimaryDisplay,
    SDL_GetDisplayContentScale,

    SDL_INIT_VIDEO,
    SDL_INIT_GAMEPAD,

    SDL_WINDOW_RESIZABLE,
    SDL_WINDOW_HIDDEN,
    SDL_WINDOW_HIGH_PIXEL_DENSITY,
)

if not SDL_Init(SDL_INIT_VIDEO | SDL_INIT_GAMEPAD):
    print(f'Error: SDL_Init(): {SDL_GetError()}')

display_id = SDL_GetPrimaryDisplay()
main_scale = SDL_GetDisplayContentScale(display_id)
window_flags = SDL_WINDOW_RESIZABLE | SDL_WINDOW_HIDDEN | SDL_WINDOW_HIGH_PIXEL_DENSITY