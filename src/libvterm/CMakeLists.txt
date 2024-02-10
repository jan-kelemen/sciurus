add_library(vterm)

target_sources(vterm
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src/encoding.c
        ${CMAKE_CURRENT_SOURCE_DIR}/src/keyboard.c
        ${CMAKE_CURRENT_SOURCE_DIR}/src/mouse.c
        ${CMAKE_CURRENT_SOURCE_DIR}/src/parser.c
        ${CMAKE_CURRENT_SOURCE_DIR}/src/pen.c
        ${CMAKE_CURRENT_SOURCE_DIR}/src/screen.c
        ${CMAKE_CURRENT_SOURCE_DIR}/src/state.c
        ${CMAKE_CURRENT_SOURCE_DIR}/src/unicode.c
        ${CMAKE_CURRENT_SOURCE_DIR}/src/vterm.c
)

target_include_directories(vterm
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/..
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        ${CMAKE_CURRENT_SOURCE_DIR}/proto)

target_compile_definitions(vterm
    PRIVATE
        VSNPRINTF=vim_vsnprintf
        SNPRINTF=vim_snprintf
        IS_COMBINING_FUNCTION=utf_iscomposing_uint
        WCWIDTH_FUNCTION=utf_uint2cells
)

if(MSVC)
    target_compile_definitions(vterm
        PRIVATE
            INLINE=
            GET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type
    )
elseif(CMAKE_C_COMPILER_ID MATCHES ".*Clang" OR CMAKE_C_COMPILER_ID STREQUAL "GNU")
    target_compile_definitions(vterm 
        PRIVATE
            HAVE_CONFIG_H
            _REENTRANT 
            _FORTIFY_SOURCE=1
            INLINE=inline
    )
else()
    message(FATAL_ERROR "Unrecognized compiler: '${CMAKE_C_COMPILER_ID}'")
endif()


