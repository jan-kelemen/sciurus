find_program(WHOAMI_PROG whoami)
find_program(HOSTNAME_PROG hostname)

if (EXISTS ${WHOAMI_PROG})
    execute_process(COMMAND ${WHOAMI_PROG}
        OUTPUT_STRIP_TRAILING_WHITESPACE
        OUTPUT_VARIABLE USERNAME)
endif()

if (EXISTS ${HOSTNAME_PROG})
    execute_process(COMMAND ${HOSTNAME_PROG}
        OUTPUT_STRIP_TRAILING_WHITESPACE
        OUTPUT_VARIABLE HOSTNAME)
endif()

configure_file(
  "${PROJECT_SOURCE_DIR}/config/pathdef.c.in"
  "${PROJECT_BINARY_DIR}/config/auto/pathdef.c"
  ESCAPE_QUOTES)
