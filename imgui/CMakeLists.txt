include(FetchContent)
FetchContent_Declare(
    SDL3
    GIT_REPOSITORY https://github.com/libsdl-org/SDL.git
    GIT_TAG release-3.2.20
    GIT_SHALLOW TRUE
)
set(BUILD_SHARED_LIBS ON CACHE BOOL "" FORCE)
set(BUILD_STATIC_LIBS OFF CACHE BOOL "" FORCE)
set(SDL_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)
set(SDL_BUILD_TESTS OFF CACHE BOOL "" FORCE)
set(SDL_INSTALL OFF CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(SDL3)

include_directories(
    ${CMAKE_SOURCE_DIR}/imgui
    ${CMAKE_SOURCE_DIR}/imgui/backends
)

add_library(
    imgui SHARED
    backends/imgui_impl_sdl3.cpp
    backends/imgui_impl_sdlrenderer3.cpp
    imgui_draw.cpp
    imgui_tables.cpp
    imgui_widgets.cpp
    imgui.cpp
)
target_link_libraries(imgui PRIVATE SDL3::SDL3)

install(TARGETS SDL3-shared imgui DESTINATION .)