
SET(TRIVIAL_LEAK_CPP_SOURCES trivial_leak.cpp)

add_executable(trivial_leak_cpp ${TRIVIAL_LEAK_CPP_SOURCES})
#set_target_properties(trivial_leak PROPERTIES FOLDER "bin")
#install(TARGETS trivial_leak DESTINATION "bin")
set_target_properties(trivial_leak_cpp PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/bin")

