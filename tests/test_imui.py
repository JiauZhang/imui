from imui import (
    __imgui_version__,
    __imgui_version_num__,
    ImVec2,
    ImVec4,

    ImFontAtlas,
    ImGuiContext,

    CreateContext,
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

    def test_create_context(self):
        font = ImFontAtlas()
        ctx = CreateContext(font)
        assert isinstance(ctx, ImGuiContext)