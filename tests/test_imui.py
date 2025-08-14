import imui
from imui import version

class TestClass:
    def test_version(self):
        assert imui.__version__ == version.__version__

    def test_import_extension(self):
        success = True
        try:
            from imui import _C
        except:
            success = False
        assert success

    def test_imvec2(self):
        imvec2 = imui.ImVec2(2, 3)
        assert imvec2.x == 2 and imvec2.y == 3
        imvec2.x = 4
        imvec2.y = 5
        assert imvec2.x == 4 and imvec2.y == 5

    def test_imvec4(self):
        imvec4 = imui.ImVec4(6, 7, 8, 9)
        assert imvec4.x == 6 and imvec4.y == 7 and imvec4.z == 8 and imvec4.w == 9
        imvec4.x = 0
        imvec4.y = 1
        imvec4.z = 2
        imvec4.w = 3
        assert imvec4.x == 0 and imvec4.y == 1 and imvec4.z == 2 and imvec4.w == 3