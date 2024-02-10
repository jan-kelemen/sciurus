add_subdirectory(libvterm)

add_library(sciurus_core)

if(MSVC)
    set(PLATFORM_SOURCES
            ${CMAKE_CURRENT_SOURCE_DIR}/os_mswin.c
            ${CMAKE_CURRENT_SOURCE_DIR}/os_win32.c
            ${CMAKE_CURRENT_SOURCE_DIR}/winclip.c
            ${CMAKE_CURRENT_SOURCE_DIR}/iscygpty.c
    )

    set(EXE_PLATFORM_SOURCES
            ${CMAKE_CURRENT_SOURCE_DIR}/os_w32exe.c
    )
elseif(CMAKE_C_COMPILER_ID STREQUAL "Clang" OR CMAKE_C_COMPILER_ID STREQUAL "GNU")
    set(PLATFORM_SOURCES
            ${CMAKE_CURRENT_SOURCE_DIR}/os_unix.c
            ${CMAKE_CURRENT_SOURCE_DIR}/if_xcmdsrv.c
            ${CMAKE_CURRENT_SOURCE_DIR}/pty.c
    )
elseif(CMAKE_C_COMPILER_ID STREQUAL "AppleClang")
    set(PLATFORM_SOURCES
            ${CMAKE_CURRENT_SOURCE_DIR}/os_unix.c
            ${CMAKE_CURRENT_SOURCE_DIR}/os_macosx.m
            ${CMAKE_CURRENT_SOURCE_DIR}/os_mac_conv.c
            ${CMAKE_CURRENT_SOURCE_DIR}/if_xcmdsrv.c
            ${CMAKE_CURRENT_SOURCE_DIR}/pty.c
    )
else()
    message(FATAL_ERROR "Unrecognized compiler: '${CMAKE_C_COMPILER_ID}'")
endif()

target_sources(sciurus_core
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/alloc.c
        ${CMAKE_CURRENT_SOURCE_DIR}/arabic.c
        ${CMAKE_CURRENT_SOURCE_DIR}/arglist.c
        ${CMAKE_CURRENT_SOURCE_DIR}/autocmd.c
        ${CMAKE_CURRENT_SOURCE_DIR}/blob.c
        ${CMAKE_CURRENT_SOURCE_DIR}/beval.c
        ${CMAKE_CURRENT_SOURCE_DIR}/blowfish.c
        ${CMAKE_CURRENT_SOURCE_DIR}/buffer.c
        ${CMAKE_CURRENT_SOURCE_DIR}/bufwrite.c
        ${CMAKE_CURRENT_SOURCE_DIR}/change.c
        ${CMAKE_CURRENT_SOURCE_DIR}/charset.c
        ${CMAKE_CURRENT_SOURCE_DIR}/cindent.c
        ${CMAKE_CURRENT_SOURCE_DIR}/clientserver.c
        ${CMAKE_CURRENT_SOURCE_DIR}/clipboard.c
        ${CMAKE_CURRENT_SOURCE_DIR}/cmdexpand.c
        ${CMAKE_CURRENT_SOURCE_DIR}/cmdhist.c
        ${CMAKE_CURRENT_SOURCE_DIR}/crypt.c
        ${CMAKE_CURRENT_SOURCE_DIR}/crypt_zip.c
        ${CMAKE_CURRENT_SOURCE_DIR}/debugger.c
        ${CMAKE_CURRENT_SOURCE_DIR}/dict.c
        ${CMAKE_CURRENT_SOURCE_DIR}/diff.c
        ${CMAKE_CURRENT_SOURCE_DIR}/digraph.c
        ${CMAKE_CURRENT_SOURCE_DIR}/drawline.c
        ${CMAKE_CURRENT_SOURCE_DIR}/drawscreen.c
        ${CMAKE_CURRENT_SOURCE_DIR}/edit.c
        ${CMAKE_CURRENT_SOURCE_DIR}/eval.c
        ${CMAKE_CURRENT_SOURCE_DIR}/evalbuffer.c
        ${CMAKE_CURRENT_SOURCE_DIR}/evalfunc.c
        ${CMAKE_CURRENT_SOURCE_DIR}/evalvars.c
        ${CMAKE_CURRENT_SOURCE_DIR}/evalwindow.c
        ${CMAKE_CURRENT_SOURCE_DIR}/ex_cmds.c
        ${CMAKE_CURRENT_SOURCE_DIR}/ex_cmds2.c
        ${CMAKE_CURRENT_SOURCE_DIR}/ex_docmd.c
        ${CMAKE_CURRENT_SOURCE_DIR}/ex_eval.c
        ${CMAKE_CURRENT_SOURCE_DIR}/ex_getln.c
        ${CMAKE_CURRENT_SOURCE_DIR}/fileio.c
        ${CMAKE_CURRENT_SOURCE_DIR}/filepath.c
        ${CMAKE_CURRENT_SOURCE_DIR}/findfile.c
        ${CMAKE_CURRENT_SOURCE_DIR}/float.c
        ${CMAKE_CURRENT_SOURCE_DIR}/fold.c
        ${CMAKE_CURRENT_SOURCE_DIR}/getchar.c
        ${CMAKE_CURRENT_SOURCE_DIR}/gui_xim.c
        ${CMAKE_CURRENT_SOURCE_DIR}/hardcopy.c
        ${CMAKE_CURRENT_SOURCE_DIR}/hashtab.c
        ${CMAKE_CURRENT_SOURCE_DIR}/help.c
        ${CMAKE_CURRENT_SOURCE_DIR}/highlight.c
        ${CMAKE_CURRENT_SOURCE_DIR}/if_cscope.c
        ${CMAKE_CURRENT_SOURCE_DIR}/indent.c
        ${CMAKE_CURRENT_SOURCE_DIR}/insexpand.c
        ${CMAKE_CURRENT_SOURCE_DIR}/json.c
        ${CMAKE_CURRENT_SOURCE_DIR}/list.c
        ${CMAKE_CURRENT_SOURCE_DIR}/locale.c
        ${CMAKE_CURRENT_SOURCE_DIR}/logfile.c
        ${CMAKE_CURRENT_SOURCE_DIR}/map.c
        ${CMAKE_CURRENT_SOURCE_DIR}/mark.c
        ${CMAKE_CURRENT_SOURCE_DIR}/match.c
        ${CMAKE_CURRENT_SOURCE_DIR}/mbyte.c
        ${CMAKE_CURRENT_SOURCE_DIR}/memfile.c
        ${CMAKE_CURRENT_SOURCE_DIR}/memline.c
        ${CMAKE_CURRENT_SOURCE_DIR}/menu.c
        ${CMAKE_CURRENT_SOURCE_DIR}/message.c
        ${CMAKE_CURRENT_SOURCE_DIR}/misc1.c
        ${CMAKE_CURRENT_SOURCE_DIR}/misc2.c
        ${CMAKE_CURRENT_SOURCE_DIR}/mouse.c
        ${CMAKE_CURRENT_SOURCE_DIR}/move.c
        ${CMAKE_CURRENT_SOURCE_DIR}/normal.c
        ${CMAKE_CURRENT_SOURCE_DIR}/ops.c
        ${CMAKE_CURRENT_SOURCE_DIR}/option.c
        ${CMAKE_CURRENT_SOURCE_DIR}/optionstr.c
        ${CMAKE_CURRENT_SOURCE_DIR}/popupmenu.c
        ${CMAKE_CURRENT_SOURCE_DIR}/popupwin.c
        ${CMAKE_CURRENT_SOURCE_DIR}/profiler.c
        ${CMAKE_CURRENT_SOURCE_DIR}/quickfix.c
        ${CMAKE_CURRENT_SOURCE_DIR}/regexp.c
        ${CMAKE_CURRENT_SOURCE_DIR}/register.c
        ${CMAKE_CURRENT_SOURCE_DIR}/scriptfile.c
        ${CMAKE_CURRENT_SOURCE_DIR}/screen.c
        ${CMAKE_CURRENT_SOURCE_DIR}/search.c
        ${CMAKE_CURRENT_SOURCE_DIR}/session.c
        ${CMAKE_CURRENT_SOURCE_DIR}/sha256.c
        ${CMAKE_CURRENT_SOURCE_DIR}/sign.c
        ${CMAKE_CURRENT_SOURCE_DIR}/spell.c        
        ${CMAKE_CURRENT_SOURCE_DIR}/spellfile.c
        ${CMAKE_CURRENT_SOURCE_DIR}/spellsuggest.c
        ${CMAKE_CURRENT_SOURCE_DIR}/strings.c
        ${CMAKE_CURRENT_SOURCE_DIR}/syntax.c
        ${CMAKE_CURRENT_SOURCE_DIR}/tag.c
        ${CMAKE_CURRENT_SOURCE_DIR}/term.c
        ${CMAKE_CURRENT_SOURCE_DIR}/testing.c
        ${CMAKE_CURRENT_SOURCE_DIR}/textformat.c
        ${CMAKE_CURRENT_SOURCE_DIR}/textobject.c
        ${CMAKE_CURRENT_SOURCE_DIR}/textprop.c
        ${CMAKE_CURRENT_SOURCE_DIR}/time.c
        ${CMAKE_CURRENT_SOURCE_DIR}/typval.c
        ${CMAKE_CURRENT_SOURCE_DIR}/ui.c
        ${CMAKE_CURRENT_SOURCE_DIR}/undo.c
        ${CMAKE_CURRENT_SOURCE_DIR}/usercmd.c
        ${CMAKE_CURRENT_SOURCE_DIR}/userfunc.c
        ${CMAKE_CURRENT_SOURCE_DIR}/vim9class.c
        ${CMAKE_CURRENT_SOURCE_DIR}/vim9cmds.c
        ${CMAKE_CURRENT_SOURCE_DIR}/vim9compile.c
        ${CMAKE_CURRENT_SOURCE_DIR}/vim9execute.c
        ${CMAKE_CURRENT_SOURCE_DIR}/vim9expr.c
        ${CMAKE_CURRENT_SOURCE_DIR}/vim9instr.c
        ${CMAKE_CURRENT_SOURCE_DIR}/vim9script.c
        ${CMAKE_CURRENT_SOURCE_DIR}/vim9type.c
        ${CMAKE_CURRENT_SOURCE_DIR}/viminfo.c
        ${CMAKE_CURRENT_SOURCE_DIR}/window.c

        ${CMAKE_BINARY_DIR}/config/auto/pathdef.c
        
        ${CMAKE_CURRENT_SOURCE_DIR}/sound.c
        ${CMAKE_CURRENT_SOURCE_DIR}/terminal.c
        
        ${CMAKE_CURRENT_SOURCE_DIR}/version.c
        
        ${CMAKE_CURRENT_SOURCE_DIR}/job.c
        ${CMAKE_CURRENT_SOURCE_DIR}/channel.c
        
        ${CMAKE_CURRENT_SOURCE_DIR}/xdiff/xdiffi.c
        ${CMAKE_CURRENT_SOURCE_DIR}/xdiff/xemit.c
        ${CMAKE_CURRENT_SOURCE_DIR}/xdiff/xprepare.c
        ${CMAKE_CURRENT_SOURCE_DIR}/xdiff/xutils.c
        ${CMAKE_CURRENT_SOURCE_DIR}/xdiff/xhistogram.c
        ${CMAKE_CURRENT_SOURCE_DIR}/xdiff/xpatience.c
        
        ${PLATFORM_SOURCES}
)

target_include_directories(sciurus_core
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${CMAKE_CURRENT_SOURCE_DIR}/proto
)

target_link_libraries(sciurus_core
    PUBLIC
        vterm
)

if(MSVC)
    target_link_libraries(sciurus_core
        PUBLIC
            imm32.lib
            winmm.lib
            Ws2_32.lib
            netapi32.lib 
    )
    
    target_compile_definitions(sciurus_core
        PUBLIC
            HAVE_PATHDEF
            WIN32 
            HAVE_STDINT_H
            WINVER=0x0601
            _WIN32_WINNT=0x0601
            /source-charset:utf-8
            FEAT_CSCOPE
            FEAT_TERMINAL
            FEAT_MBYTE_IME
            DYNAMIC_IME
            DYNAMIC_ICONV
            DYNAMIC_GETTEXT
            FEAT_huge
            MODIFIED_BY="Jan Kelemen"
            FEAT_SOUND
            FEAT_JOB_CHANNEL
            FEAT_IPV6
            FEAT_INET_NTOP
    )
elseif(CMAKE_C_COMPILER_ID STREQUAL "Clang" OR CMAKE_C_COMPILER_ID STREQUAL "GNU")
    target_compile_options(sciurus_core
        PUBLIC
            --std=c2x
            -Wall -Wextra
    )

    target_compile_definitions(sciurus_core
        PUBLIC
            HAVE_CONFIG_H
            _REENTRANT 
            _FORTIFY_SOURCE=1
    )

    target_link_libraries(sciurus_core
        PUBLIC
            X11::Xt
            m
            selinux
            tinfo
            sodium
            canberra
    )
elseif(CMAKE_C_COMPILER_ID STREQUAL "AppleClang")
    target_compile_options(sciurus_core
        PUBLIC
            --std=c2x
            -Wall -Wextra
    )

    target_compile_definitions(sciurus_core
        PUBLIC
            HAVE_CONFIG_H
            _REENTRANT 
            _FORTIFY_SOURCE=1
            MACOS_X
            MACOS_X_DARWIN
    )

    target_link_libraries(sciurus_core
        PUBLIC
            m
            Intl::Intl
            Iconv::Iconv
            ncurses
            "-framework AppKit"
    )
else()
    message(FATAL_ERROR "Unrecognized compiler: '${CMAKE_C_COMPILER_ID}'")
endif()

add_executable(sciurus)

target_sources(sciurus
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/main.c
        ${EXE_PLATFORM_SOURCES}
)

target_link_libraries(sciurus PRIVATE sciurus_core)
if(MSVC)
    target_link_options(sciurus
        PUBLIC
            /SUBSYSTEM:console
    )
endif()

if(CMAKE_C_COMPILER_ID STREQUAL "GNU")
    add_executable(json_test)
    target_sources(json_test
        PRIVATE
            ${CMAKE_CURRENT_SOURCE_DIR}/json_test.c
    )
    target_link_libraries(json_test PRIVATE sciurus_core)
    add_test(NAME json_test COMMAND json_test)
    
    add_executable(kword_test)
    target_sources(kword_test
        PRIVATE
            ${CMAKE_CURRENT_SOURCE_DIR}/kword_test.c
    )
    target_link_libraries(kword_test PRIVATE sciurus_core)
    add_test(NAME kword_test COMMAND kword_test)
    
    add_executable(memfile_test)
    target_sources(memfile_test
        PRIVATE
            ${CMAKE_CURRENT_SOURCE_DIR}/memfile_test.c
    )
    target_link_libraries(memfile_test PRIVATE sciurus_core)
    add_test(NAME memfile_test COMMAND memfile_test)
    
    add_executable(message_test)
    target_sources(message_test
        PRIVATE
            ${CMAKE_CURRENT_SOURCE_DIR}/message_test.c
    )
    target_link_libraries(message_test PRIVATE sciurus_core)
    add_test(NAME message_test COMMAND message_test)
endif()
