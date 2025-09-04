from imui.sdl import (
    SDL_Init,

    SDL_INIT_VIDEO,
    SDL_INIT_GAMEPAD,
)

if not SDL_Init(SDL_INIT_VIDEO | SDL_INIT_GAMEPAD):
    print('Error: SDL_Init()')