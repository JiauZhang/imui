#include <nanobind/nanobind.h>
#include <imgui/imgui.h>

namespace nb = nanobind;

namespace imui {

void def_flags(nb::module_ & (m)) {
    nb::enum_<ImGuiConfigFlags_>(m, "ImGuiConfigFlags", nb::is_arithmetic())
        .value("None", ImGuiConfigFlags_::ImGuiConfigFlags_None)
        .value("NavEnableKeyboard", ImGuiConfigFlags_::ImGuiConfigFlags_NavEnableKeyboard)
        .value("NavEnableGamepad", ImGuiConfigFlags_::ImGuiConfigFlags_NavEnableGamepad)
        .value("NoMouse", ImGuiConfigFlags_::ImGuiConfigFlags_NoMouse)
        .value("NoMouseCursorChange", ImGuiConfigFlags_::ImGuiConfigFlags_NoMouseCursorChange)
        .value("NoKeyboard", ImGuiConfigFlags_::ImGuiConfigFlags_NoKeyboard)
        .value("IsSRGB", ImGuiConfigFlags_::ImGuiConfigFlags_IsSRGB)
        .value("IsTouchScreen", ImGuiConfigFlags_::ImGuiConfigFlags_IsTouchScreen);
    nb::enum_<ImGuiSliderFlags_>(m, "ImGuiSliderFlags", nb::is_arithmetic())
        .value("None", ImGuiSliderFlags_::ImGuiSliderFlags_None)
        .value("Logarithmic", ImGuiSliderFlags_::ImGuiSliderFlags_Logarithmic)
        .value("NoRoundToFormat", ImGuiSliderFlags_::ImGuiSliderFlags_NoRoundToFormat)
        .value("NoInput", ImGuiSliderFlags_::ImGuiSliderFlags_NoInput)
        .value("WrapAround", ImGuiSliderFlags_::ImGuiSliderFlags_WrapAround)
        .value("ClampOnInput", ImGuiSliderFlags_::ImGuiSliderFlags_ClampOnInput)
        .value("ClampZeroRange", ImGuiSliderFlags_::ImGuiSliderFlags_ClampZeroRange)
        .value("NoSpeedTweaks", ImGuiSliderFlags_::ImGuiSliderFlags_NoSpeedTweaks)
        .value("AlwaysClamp", ImGuiSliderFlags_::ImGuiSliderFlags_AlwaysClamp)
        .value("InvalidMask_", ImGuiSliderFlags_::ImGuiSliderFlags_InvalidMask_);
}

} // namespace imui