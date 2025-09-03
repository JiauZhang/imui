#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <imgui/imgui_internal.h>
#include <imgui/imgui.h>
#include <string>
#include <cstdio>
#include <memory>
#include <cstdarg>

namespace nb = nanobind;
using namespace nanobind::literals;

namespace imui {

extern void def_flags(nb::module_ & (m));
extern void def_widgets(nb::module_ & (m));
extern void def_sdl(nb::module_ & (m));

std::string format(const char *fmt, ...) {
    va_list args;
    va_start(args, fmt);
    int size = std::vsnprintf(nullptr, 0, fmt, args);
    va_end(args);

    if (size < 0)
        return "";

    std::string result(size, '\0');
    va_start(args, fmt);
    std::vsnprintf(&result[0], size + 1, fmt, args);
    va_end(args);

    return result;
}

NB_MODULE(_C, m) {
    def_flags(m);
    def_widgets(m);
    def_sdl(m);

    m.attr("__imgui_version__") = IMGUI_VERSION;
    m.attr("__imgui_version_num__") = IMGUI_VERSION_NUM;

    nb::class_<ImVec2>(m, "ImVec2")
        .def(nb::new_([]() { return ImVec2(); }))
        .def(nb::new_([](float x, float y) { return ImVec2(x, y); }))
        .def_rw("x", &ImVec2::x)
        .def_rw("y", &ImVec2::y)
        .def("__str__", [](ImVec2 &self) { return format("(%f, %f)", self.x, self.y); })
        .def("__repr__", [](ImVec2 &self) { return format("ImVec2(x=%f, y=%f)", self.x, self.y); });
    nb::class_<ImVec4>(m, "ImVec4")
        .def(nb::new_([]() { return ImVec4(); }))
        .def(nb::new_([](float x, float y, float z, float w) { return ImVec4(x, y, z, w); }))
        .def_rw("x", &ImVec4::x)
        .def_rw("y", &ImVec4::y)
        .def_rw("z", &ImVec4::z)
        .def_rw("w", &ImVec4::w)
        .def("__str__", [](ImVec4 &self) { return format("(%f, %f, %f, %f)", self.x, self.y, self.z, self.w); })
        .def("__repr__", [](ImVec4 &self) { return format("ImVec4(x=%f, y=%f, z=%f, w=%f)", self.x, self.y, self.z, self.w); });

    nb::class_<ImFontAtlas>(m, "ImFontAtlas")
        .def(nb::init<>());
    nb::class_<ImGuiContext>(m, "ImGuiContext")
        .def(nb::init<ImFontAtlas *>())
        .def_rw("Initialized", &ImGuiContext::Initialized);
    nb::class_<ImGuiIO>(m, "ImGuiIO")
        .def(nb::init<>())
        .def_rw("ConfigFlags", &ImGuiIO::ConfigFlags);
    nb::class_<ImGuiStyle>(m, "ImGuiStyle")
        .def(nb::init<>())
        .def("ImGuiStyle", &ImGuiStyle::ScaleAllSizes)
        .def_rw("FontScaleDpi", &ImGuiStyle::FontScaleDpi);

    m.def("CreateContext", &ImGui::CreateContext, "shared_font_atlas"_a = nullptr);
    m.def("GetCurrentContext", &ImGui::GetCurrentContext);
    m.def("GetIO", nb::overload_cast<>(&ImGui::GetIO), nb::rv_policy::reference);
    m.def("StyleColorsDark", &ImGui::StyleColorsDark, "dst"_a = nullptr);
    m.def("GetStyle", &ImGui::GetStyle, nb::rv_policy::reference);
    m.def("NewFrame", &ImGui::NewFrame);
    m.def("Begin", &ImGui::Begin, "name"_a, "p_open"_a = nullptr, "flags"_a = 0);
    m.def("End", &ImGui::End);
}

} // namespace imui