from imui import (
    IMGUI_CHECKVERSION,
    CreateContext,
    GetIO,
    StyleColorsDark,
    GetStyle,
    NewFrame,
    Begin,
    End,

    ImGuiConfigFlags,
    ImVec4,
)
from imui.sdl import (
    SDL_Init,
    SDL_Delay,
    SDL_GetError,
    SDL_GetPrimaryDisplay,
    SDL_GetDisplayContentScale,
    SDL_CreateWindow,
    SDL_SetWindowPosition,
    SDL_ShowWindow,
    SDL_CreateGPUDevice,
    SDL_ClaimWindowForGPUDevice,
    SDL_SetGPUSwapchainParameters,
    SDL_GetGPUSwapchainTextureFormat,

    ImGui_ImplSDL3_InitForSDLGPU,
    ImGui_ImplSDLGPU3_InitInfo,
    SDL_GPUSampleCount,
    ImGui_ImplSDLGPU3_Init,

    SDL_Event,
    SDL_EventType,
    SDL_WindowEvent,
    SDL_PollEvent,
    SDL_GetWindowID,
    SDL_GetWindowFlags,
    ImGui_ImplSDL3_ProcessEvent,
    ImGui_ImplSDLGPU3_NewFrame,
    ImGui_ImplSDL3_NewFrame,

    SDL_INIT_VIDEO,
    SDL_INIT_GAMEPAD,

    SDL_WINDOW_RESIZABLE,
    SDL_WINDOW_MINIMIZED,
    SDL_WINDOW_HIDDEN,
    SDL_WINDOW_HIGH_PIXEL_DENSITY,

    SDL_WINDOWPOS_CENTERED,

    SDL_GPU_SHADERFORMAT_SPIRV,
    SDL_GPU_SHADERFORMAT_DXIL,
    SDL_GPU_SHADERFORMAT_METALLIB,
    SDL_GPU_SWAPCHAINCOMPOSITION_SDR,
    SDL_GPU_PRESENTMODE_VSYNC,
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

SDL_SetWindowPosition(window, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED)
SDL_ShowWindow(window)

gpu_device = SDL_CreateGPUDevice(SDL_GPU_SHADERFORMAT_SPIRV | SDL_GPU_SHADERFORMAT_DXIL | SDL_GPU_SHADERFORMAT_METALLIB, True)
if not gpu_device:
    print(f'Error: SDL_CreateGPUDevice(): {SDL_GetError()}')
    exit(-1)
if not SDL_ClaimWindowForGPUDevice(gpu_device, window):
    print(f'Error: SDL_ClaimWindowForGPUDevice(): {SDL_GetError()}')
    exit(-1)
SDL_SetGPUSwapchainParameters(gpu_device, window, SDL_GPU_SWAPCHAINCOMPOSITION_SDR, SDL_GPU_PRESENTMODE_VSYNC)

IMGUI_CHECKVERSION()
CreateContext()
io = GetIO()
io.ConfigFlags |= ImGuiConfigFlags.NavEnableKeyboard
io.ConfigFlags |= ImGuiConfigFlags.NavEnableGamepad

StyleColorsDark()

style = GetStyle()
style.ScaleAllSizes(main_scale)
style.FontScaleDpi = main_scale

ImGui_ImplSDL3_InitForSDLGPU(window)

init_info = ImGui_ImplSDLGPU3_InitInfo()
init_info.Device = gpu_device
init_info.ColorTargetFormat = SDL_GetGPUSwapchainTextureFormat(gpu_device, window)
init_info.MSAASamples = SDL_GPUSampleCount.SAMPLECOUNT_1
ImGui_ImplSDLGPU3_Init(init_info)

show_demo_window = True
show_another_window = False
clear_color = ImVec4(0.45, 0.55, 0.60, 1.00)

done = False
while not done:
    event = SDL_Event()
    while SDL_PollEvent(event):
        ImGui_ImplSDL3_ProcessEvent(event)
        if event.type == SDL_EventType.QUIT:
            done = True
        if event.type == SDL_EventType.WINDOW_CLOSE_REQUESTED and event.window.windowID == SDL_GetWindowID(window):
            done = True

    if SDL_GetWindowFlags(window) & SDL_WINDOW_MINIMIZED:
        SDL_Delay(10)
        continue

    ImGui_ImplSDLGPU3_NewFrame()
    ImGui_ImplSDL3_NewFrame()
    NewFrame()