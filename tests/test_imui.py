import imui
from imui import (
    __imgui_version__,
    __imgui_version_num__,
    ImVec2,
    ImVec4,

    ImFontAtlas,
    ImGuiContext,

    CreateContext,
    GetCurrentContext,
    GetIO,
)

class TestClass:
    def test_imvec2(self):
        imvec2 = ImVec2(2, 3)
        assert imvec2.x == 2 and imvec2.y == 3
        imvec2.x = 4
        imvec2.y = 5
        assert imvec2.x == 4 and imvec2.y == 5

    def test_imvec4(self):
        imvec4 = ImVec4(6, 7, 8, 9)
        assert imvec4.x == 6 and imvec4.y == 7 and imvec4.z == 8 and imvec4.w == 9
        imvec4.x = 0
        imvec4.y = 1
        imvec4.z = 2
        imvec4.w = 3
        assert imvec4.x == 0 and imvec4.y == 1 and imvec4.z == 2 and imvec4.w == 3

    def test_context(self):
        font = ImFontAtlas()
        ctx_1 = CreateContext(font)
        assert isinstance(ctx_1, ImGuiContext)
        assert ctx_1.Initialized == True

        ctx_2 = GetCurrentContext()
        assert ctx_1 is ctx_2

        ctx_1.Initialized = False
        assert ctx_2.Initialized == False

    def test_ImGuiIO(self):
        ctx = CreateContext()
        io_1 = GetIO()
        value = imui.ImGuiConfigFlags.NavEnableGamepad.value
        io_1.ConfigFlags = imui.ImGuiConfigFlags.NavEnableGamepad
        io_1.ConfigFlags |= imui.ImGuiConfigFlags.NoMouseCursorChange
        value |= imui.ImGuiConfigFlags.NoMouseCursorChange.value
        io_1.ConfigFlags |= imui.ImGuiConfigFlags.IsTouchScreen
        value |= imui.ImGuiConfigFlags.IsTouchScreen.value
        assert io_1.ConfigFlags == value

        io_2 = GetIO()
        assert io_2 is io_1