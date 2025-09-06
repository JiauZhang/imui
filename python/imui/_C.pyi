import enum
from typing import overload


class ImGuiConfigFlags(enum.IntEnum):
    None = 0

    NavEnableKeyboard = 1

    NavEnableGamepad = 2

    NoMouse = 16

    NoMouseCursorChange = 32

    NoKeyboard = 64

    IsSRGB = 1048576

    IsTouchScreen = 2097152

class ImGuiSliderFlags(enum.IntEnum):
    None = 0

    Logarithmic = 32

    NoRoundToFormat = 64

    NoInput = 128

    WrapAround = 256

    ClampOnInput = 512

    ClampZeroRange = 1024

    NoSpeedTweaks = 2048

    AlwaysClamp = 1536

def Text(arg: str, /) -> None: ...

def Checkbox(label: str, v: bool) -> bool: ...

def SliderFloat(label: str, v: float, v_min: float, v_max: float, format: str = '%.3f', flags: int = 0) -> bool: ...

SDL_INIT_AUDIO: int = 16

SDL_INIT_VIDEO: int = 32

SDL_INIT_JOYSTICK: int = 512

SDL_INIT_HAPTIC: int = 4096

SDL_INIT_GAMEPAD: int = 8192

SDL_INIT_EVENTS: int = 16384

SDL_INIT_SENSOR: int = 32768

SDL_INIT_CAMERA: int = 65536

SDL_WINDOW_FULLSCREEN: int = 1

SDL_WINDOW_OPENGL: int = 2

SDL_WINDOW_OCCLUDED: int = 4

SDL_WINDOW_HIDDEN: int = 8

SDL_WINDOW_BORDERLESS: int = 16

SDL_WINDOW_RESIZABLE: int = 32

SDL_WINDOW_MINIMIZED: int = 64

SDL_WINDOW_MAXIMIZED: int = 128

SDL_WINDOW_MOUSE_GRABBED: int = 256

SDL_WINDOW_INPUT_FOCUS: int = 512

SDL_WINDOW_MOUSE_FOCUS: int = 1024

SDL_WINDOW_EXTERNAL: int = 2048

SDL_WINDOW_MODAL: int = 4096

SDL_WINDOW_HIGH_PIXEL_DENSITY: int = 8192

SDL_WINDOW_MOUSE_CAPTURE: int = 16384

SDL_WINDOW_MOUSE_RELATIVE_MODE: int = 32768

SDL_WINDOW_ALWAYS_ON_TOP: int = 65536

SDL_WINDOW_UTILITY: int = 131072

SDL_WINDOW_TOOLTIP: int = 262144

SDL_WINDOW_POPUP_MENU: int = 524288

SDL_WINDOW_KEYBOARD_GRABBED: int = 1048576

SDL_WINDOW_VULKAN: int = 268435456

SDL_WINDOW_METAL: int = 536870912

SDL_WINDOW_TRANSPARENT: int = 1073741824

SDL_WINDOW_NOT_FOCUSABLE: int = 2147483648

SDL_WINDOWPOS_CENTERED: int = 805240832

SDL_GPU_SHADERFORMAT_INVALID: int = 0

SDL_GPU_SHADERFORMAT_PRIVATE: int = 1

SDL_GPU_SHADERFORMAT_SPIRV: int = 2

SDL_GPU_SHADERFORMAT_DXBC: int = 4

SDL_GPU_SHADERFORMAT_DXIL: int = 8

SDL_GPU_SHADERFORMAT_MSL: int = 16

SDL_GPU_SHADERFORMAT_METALLIB: int = 32

SDL_GPU_SWAPCHAINCOMPOSITION_SDR: int = 0

SDL_GPU_SWAPCHAINCOMPOSITION_SDR_LINEAR: int = 1

SDL_GPU_SWAPCHAINCOMPOSITION_HDR_EXTENDED_LINEAR: int = 2

SDL_GPU_SWAPCHAINCOMPOSITION_HDR10_ST2084: int = 3

SDL_GPU_PRESENTMODE_VSYNC: int = 0

SDL_GPU_PRESENTMODE_IMMEDIATE: int = 1

SDL_GPU_PRESENTMODE_MAILBOX: int = 2

def SDL_Init(arg: int, /) -> bool: ...

def SDL_GetError() -> str: ...

def SDL_GetPrimaryDisplay() -> int: ...

def SDL_GetDisplayContentScale(arg: int, /) -> float: ...

class SDL_Window:
    def __bool__(self) -> bool: ...

def SDL_CreateWindow(arg0: str, arg1: int, arg2: int, arg3: int, /) -> SDL_Window: ...

def SDL_DestroyWindow(arg: SDL_Window, /) -> None: ...

def SDL_SetWindowPosition(arg0: SDL_Window, arg1: int, arg2: int, /) -> bool: ...

def SDL_ShowWindow(arg: SDL_Window, /) -> bool: ...

class SDL_GPUDevice:
    def __bool__(self) -> bool: ...

def SDL_CreateGPUDevice(format_flags: int, debug_mode: bool, name: str = '') -> SDL_GPUDevice: ...

def SDL_ClaimWindowForGPUDevice(arg0: SDL_GPUDevice, arg1: SDL_Window, /) -> bool: ...

def SDL_SetGPUSwapchainParameters(device: SDL_GPUDevice, window: SDL_Window, swapchain_composition: int, present_mode: int) -> bool: ...

__imgui_version__: str = '1.92.2 WIP'

__imgui_version_num__: int = 19214

class ImVec2:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, arg0: float, arg1: float, /) -> None: ...

    @property
    def x(self) -> float: ...

    @x.setter
    def x(self, arg: float, /) -> None: ...

    @property
    def y(self) -> float: ...

    @y.setter
    def y(self, arg: float, /) -> None: ...

    def __str__(self) -> str: ...

    def __repr__(self) -> str: ...

class ImVec4:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, /) -> None: ...

    @property
    def x(self) -> float: ...

    @x.setter
    def x(self, arg: float, /) -> None: ...

    @property
    def y(self) -> float: ...

    @y.setter
    def y(self, arg: float, /) -> None: ...

    @property
    def z(self) -> float: ...

    @z.setter
    def z(self, arg: float, /) -> None: ...

    @property
    def w(self) -> float: ...

    @w.setter
    def w(self, arg: float, /) -> None: ...

    def __str__(self) -> str: ...

    def __repr__(self) -> str: ...

class ImFontAtlas:
    def __init__(self) -> None: ...

class ImGuiContext:
    def __init__(self, arg: ImFontAtlas, /) -> None: ...

    @property
    def Initialized(self) -> bool: ...

    @Initialized.setter
    def Initialized(self, arg: bool, /) -> None: ...

class ImGuiIO:
    def __init__(self) -> None: ...

    @property
    def ConfigFlags(self) -> int: ...

    @ConfigFlags.setter
    def ConfigFlags(self, arg: int, /) -> None: ...

class ImGuiStyle:
    def __init__(self) -> None: ...

    def ScaleAllSizes(self, arg: float, /) -> None: ...

    @property
    def FontScaleDpi(self) -> float: ...

    @FontScaleDpi.setter
    def FontScaleDpi(self, arg: float, /) -> None: ...

def IMGUI_CHECKVERSION() -> bool: ...

def CreateContext(shared_font_atlas: ImFontAtlas | None = None) -> ImGuiContext: ...

def GetCurrentContext() -> ImGuiContext: ...

def GetIO() -> ImGuiIO: ...

def StyleColorsDark(dst: ImGuiStyle | None = None) -> None: ...

def GetStyle() -> ImGuiStyle: ...

def NewFrame() -> None: ...

def Begin(name: str, p_open: bool | None = None, flags: int = 0) -> bool: ...

def End() -> None: ...
