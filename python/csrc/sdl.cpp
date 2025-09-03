#include <nanobind/nanobind.h>
#include <SDL3/SDL.h>

namespace nb = nanobind;
using namespace nanobind::literals;

namespace imui {

void def_sdl(nb::module_ & (m)) {
    m.attr("SDL_INIT_AUDIO") = SDL_INIT_AUDIO;
    m.attr("SDL_INIT_VIDEO") = SDL_INIT_VIDEO;
    m.attr("SDL_INIT_JOYSTICK") = SDL_INIT_JOYSTICK;
    m.attr("SDL_INIT_HAPTIC") = SDL_INIT_HAPTIC;
    m.attr("SDL_INIT_GAMEPAD") = SDL_INIT_GAMEPAD;
    m.attr("SDL_INIT_EVENTS") = SDL_INIT_EVENTS;
    m.attr("SDL_INIT_SENSOR") = SDL_INIT_SENSOR;
    m.attr("SDL_INIT_CAMERA") = SDL_INIT_CAMERA;

    m.def("SDL_Init", &SDL_Init);
}

} // namespace imui