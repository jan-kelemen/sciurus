cmake_minimum_required(VERSION 3.27)

cmake_policy(SET CMP0025 NEW)

project(sciurus VERSION 0.1 LANGUAGES C)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(CMAKE_C_COMPILER_ID STREQUAL "Clang" OR CMAKE_C_COMPILER_ID STREQUAL "GNU")
	find_package(Curses)
	find_package(X11 COMPONENTS Xt)
elseif (CMAKE_C_COMPILER_ID STREQUAL "AppleClang")
    find_package(Curses)
	find_package(Intl)
	find_package(Iconv)
elseif(MSVC)
else()
	message(FATAL_ERROR "Unrecognized compiler: '${CMAKE_C_COMPILER_ID}'")
endif()

include(CTest)

add_subdirectory(config)
add_subdirectory(src)
