from typing import overload


ImGuiConfigFlags_None: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_None

ImGuiConfigFlags_NavEnableKeyboard: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_NavEnableKeyboard

ImGuiConfigFlags_NavEnableGamepad: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_NavEnableGamepad

ImGuiConfigFlags_NoMouse: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_NoMouse

ImGuiConfigFlags_NoMouseCursorChange: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_NoMouseCursorChange

ImGuiConfigFlags_NoKeyboard: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_NoKeyboard

ImGuiConfigFlags_IsSRGB: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_IsSRGB

ImGuiConfigFlags_IsTouchScreen: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_IsTouchScreen

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

def CreateContext(shared_font_atlas: ImFontAtlas | None = None) -> ImGuiContext: ...

def GetCurrentContext() -> ImGuiContext: ...

def GetIO() -> ImGuiIO: ...
