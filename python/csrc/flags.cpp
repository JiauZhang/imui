#include <nanobind/nanobind.h>
#include <imgui/imgui.h>

namespace nb = nanobind;

namespace imui {

void def_flags(nb::module_ & (m)) {
    nb::enum_<ImGuiConfigFlags_>(m, "ImGuiConfigFlags_", nb::is_arithmetic())
        .value("ImGuiConfigFlags_None", ImGuiConfigFlags_::ImGuiConfigFlags_None)
        .value("ImGuiConfigFlags_NavEnableKeyboard", ImGuiConfigFlags_::ImGuiConfigFlags_NavEnableKeyboard)
        .value("ImGuiConfigFlags_NavEnableGamepad", ImGuiConfigFlags_::ImGuiConfigFlags_NavEnableGamepad)
        .value("ImGuiConfigFlags_NoMouse", ImGuiConfigFlags_::ImGuiConfigFlags_NoMouse)
        .value("ImGuiConfigFlags_NoMouseCursorChange", ImGuiConfigFlags_::ImGuiConfigFlags_NoMouseCursorChange)
        .value("ImGuiConfigFlags_NoKeyboard", ImGuiConfigFlags_::ImGuiConfigFlags_NoKeyboard)
        .value("ImGuiConfigFlags_IsSRGB", ImGuiConfigFlags_::ImGuiConfigFlags_IsSRGB)
        .value("ImGuiConfigFlags_IsTouchScreen", ImGuiConfigFlags_::ImGuiConfigFlags_IsTouchScreen)
        .export_values();
}

} // namespace imui