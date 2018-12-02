
SET(TRIVIAL_LEAK_SOURCES trivial_leak.c)

add_executable(trivial_leak ${TRIVIAL_LEAK_SOURCES})
#set_target_properties(trivial_leak PROPERTIES FOLDER "bin")
#install(TARGETS trivial_leak DESTINATION "bin")
set_target_properties(trivial_leak PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/bin")

