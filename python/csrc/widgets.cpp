#include <nanobind/nanobind.h>
#include <imgui/imgui.h>

namespace nb = nanobind;
using namespace nanobind::literals;

namespace imui {

void def_widgets(nb::module_ & (m)) {
    m.def("Text", [](const char *text) { ImGui::Text(text); });
    m.def("Checkbox", &ImGui::Checkbox, "label"_a, "v"_a);
    m.def("SliderFloat", &ImGui::SliderFloat, "label"_a, "v"_a, "v_min"_a, "v_max"_a, "format"_a = "%.3f", "flags"_a = 0);
}

} // namespace imui