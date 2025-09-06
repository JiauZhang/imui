#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <SDL3/SDL.h>
#include <SDL3/SDL_gpu.h>

namespace nb = nanobind;
using namespace nanobind::literals;

namespace imui {

#define UnWrapper(var, T) (*((T **)(&var)))

struct SDL_Window_Wrapper {
    SDL_Window_Wrapper(SDL_Window *w) : window(w) {};
    struct SDL_Window *window;
    bool __bool__() { return window != nullptr; }
};
struct SDL_GPUDevice_Wrapper {
    SDL_GPUDevice_Wrapper(SDL_GPUDevice *g) : gpu_device(g) {};
    SDL_GPUDevice *gpu_device;
    bool __bool__() { return gpu_device != nullptr; }
};

void def_sdl(nb::module_ & (m)) {
    m.attr("SDL_INIT_AUDIO") = SDL_INIT_AUDIO;
    m.attr("SDL_INIT_VIDEO") = SDL_INIT_VIDEO;
    m.attr("SDL_INIT_JOYSTICK") = SDL_INIT_JOYSTICK;
    m.attr("SDL_INIT_HAPTIC") = SDL_INIT_HAPTIC;
    m.attr("SDL_INIT_GAMEPAD") = SDL_INIT_GAMEPAD;
    m.attr("SDL_INIT_EVENTS") = SDL_INIT_EVENTS;
    m.attr("SDL_INIT_SENSOR") = SDL_INIT_SENSOR;
    m.attr("SDL_INIT_CAMERA") = SDL_INIT_CAMERA;

    m.attr("SDL_WINDOW_FULLSCREEN") = SDL_WINDOW_FULLSCREEN;
    m.attr("SDL_WINDOW_OPENGL") = SDL_WINDOW_OPENGL;
    m.attr("SDL_WINDOW_OCCLUDED") = SDL_WINDOW_OCCLUDED;
    m.attr("SDL_WINDOW_HIDDEN") = SDL_WINDOW_HIDDEN;
    m.attr("SDL_WINDOW_BORDERLESS") = SDL_WINDOW_BORDERLESS;
    m.attr("SDL_WINDOW_RESIZABLE") = SDL_WINDOW_RESIZABLE;
    m.attr("SDL_WINDOW_MINIMIZED") = SDL_WINDOW_MINIMIZED;
    m.attr("SDL_WINDOW_MAXIMIZED") = SDL_WINDOW_MAXIMIZED;
    m.attr("SDL_WINDOW_MOUSE_GRABBED") = SDL_WINDOW_MOUSE_GRABBED;
    m.attr("SDL_WINDOW_INPUT_FOCUS") = SDL_WINDOW_INPUT_FOCUS;
    m.attr("SDL_WINDOW_MOUSE_FOCUS") = SDL_WINDOW_MOUSE_FOCUS;
    m.attr("SDL_WINDOW_EXTERNAL") = SDL_WINDOW_EXTERNAL;
    m.attr("SDL_WINDOW_MODAL") = SDL_WINDOW_MODAL;
    m.attr("SDL_WINDOW_HIGH_PIXEL_DENSITY") = SDL_WINDOW_HIGH_PIXEL_DENSITY;
    m.attr("SDL_WINDOW_MOUSE_CAPTURE") = SDL_WINDOW_MOUSE_CAPTURE;
    m.attr("SDL_WINDOW_MOUSE_RELATIVE_MODE") = SDL_WINDOW_MOUSE_RELATIVE_MODE;
    m.attr("SDL_WINDOW_ALWAYS_ON_TOP") = SDL_WINDOW_ALWAYS_ON_TOP;
    m.attr("SDL_WINDOW_UTILITY") = SDL_WINDOW_UTILITY;
    m.attr("SDL_WINDOW_TOOLTIP") = SDL_WINDOW_TOOLTIP;
    m.attr("SDL_WINDOW_POPUP_MENU") = SDL_WINDOW_POPUP_MENU;
    m.attr("SDL_WINDOW_KEYBOARD_GRABBED") = SDL_WINDOW_KEYBOARD_GRABBED;
    m.attr("SDL_WINDOW_VULKAN") = SDL_WINDOW_VULKAN;
    m.attr("SDL_WINDOW_METAL") = SDL_WINDOW_METAL;
    m.attr("SDL_WINDOW_TRANSPARENT") = SDL_WINDOW_TRANSPARENT;
    m.attr("SDL_WINDOW_NOT_FOCUSABLE") = SDL_WINDOW_NOT_FOCUSABLE;

    m.attr("SDL_WINDOWPOS_CENTERED") = SDL_WINDOWPOS_CENTERED;

    m.attr("SDL_GPU_SHADERFORMAT_INVALID") = SDL_GPU_SHADERFORMAT_INVALID;
    m.attr("SDL_GPU_SHADERFORMAT_PRIVATE") = SDL_GPU_SHADERFORMAT_PRIVATE;
    m.attr("SDL_GPU_SHADERFORMAT_SPIRV") = SDL_GPU_SHADERFORMAT_SPIRV;
    m.attr("SDL_GPU_SHADERFORMAT_DXBC") = SDL_GPU_SHADERFORMAT_DXBC;
    m.attr("SDL_GPU_SHADERFORMAT_DXIL") = SDL_GPU_SHADERFORMAT_DXIL;
    m.attr("SDL_GPU_SHADERFORMAT_MSL") = SDL_GPU_SHADERFORMAT_MSL;
    m.attr("SDL_GPU_SHADERFORMAT_METALLIB") = SDL_GPU_SHADERFORMAT_METALLIB;

    m.def("SDL_Init", &SDL_Init);
    m.def("SDL_GetError", []() { return std::string(SDL_GetError()); });
    m.def("SDL_GetPrimaryDisplay", &SDL_GetPrimaryDisplay);
    m.def("SDL_GetDisplayContentScale", &SDL_GetDisplayContentScale);

    nb::class_<SDL_Window_Wrapper>(m, "SDL_Window")
        .def("__bool__", &SDL_Window_Wrapper::__bool__);
    m.def("SDL_CreateWindow", [](const char *title, int w, int h, SDL_WindowFlags flags) {
        SDL_Window *window = SDL_CreateWindow(title, w, h, flags);
        return SDL_Window_Wrapper(window);
    });
    m.def("SDL_DestroyWindow", [](const SDL_Window_Wrapper &w) { SDL_DestroyWindow(UnWrapper(w, SDL_Window)); });
    m.def("SDL_SetWindowPosition", [](const SDL_Window_Wrapper &w, int x, int y) { return SDL_SetWindowPosition(w.window, x, y); });
    m.def("SDL_ShowWindow", [](const SDL_Window_Wrapper &w) { return SDL_ShowWindow(UnWrapper(w, SDL_Window)); });

    nb::class_<SDL_GPUDevice_Wrapper>(m, "SDL_GPUDevice")
        .def("__bool__", &SDL_GPUDevice_Wrapper::__bool__);
    m.def("SDL_CreateGPUDevice", [](SDL_GPUShaderFormat format_flags, bool debug_mode, const char *name) {
        if (*name == '\0') name = nullptr;
        return SDL_GPUDevice_Wrapper(SDL_CreateGPUDevice(format_flags, debug_mode, name));
    }, "format_flags"_a, "debug_mode"_a, "name"_a = "");
    m.def("SDL_ClaimWindowForGPUDevice", [](const SDL_GPUDevice_Wrapper &g, const SDL_Window_Wrapper &w) {
        return SDL_ClaimWindowForGPUDevice(UnWrapper(g, SDL_GPUDevice), UnWrapper(w, SDL_Window));
    });
}

} // namespace imui