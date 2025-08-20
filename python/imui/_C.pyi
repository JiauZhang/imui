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

    def ImGuiStyle(self, arg: float, /) -> None: ...

    @property
    def FontScaleDpi(self) -> float: ...

    @FontScaleDpi.setter
    def FontScaleDpi(self, arg: float, /) -> None: ...

def CreateContext(shared_font_atlas: ImFontAtlas | None = None) -> ImGuiContext: ...

def GetCurrentContext() -> ImGuiContext: ...

def GetIO() -> ImGuiIO: ...

def StyleColorsDark(dst: ImGuiStyle | None = None) -> None: ...

def GetStyle() -> ImGuiStyle: ...

def NewFrame() -> None: ...

def Begin(name: str, p_open: bool | None = None, flags: int = 0) -> bool: ...

def End() -> None: ...

def Text(arg: str, /) -> None: ...

def Checkbox(label: str, v: bool) -> bool: ...

def SliderFloat(label: str, v: float, v_min: float, v_max: float, format: str = '%.3f', flags: int = 0) -> bool: ...
