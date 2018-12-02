
SET(GTEST_SOURCES src/gtest-all.cc)
SET(GTEST_MAIN_SOURCES src/gtest_main.cc)
SET(GTEST_INCLUDE_DIRECTORIES include)
SET(GTEST_LINK_DIRECTORIES ${PROJECT_BINARY_DIR}/lib)

FIND_PACKAGE(Threads REQUIRED)
SET(GTEST_LINK_LIBRARIES 
    ${CMAKE_THREAD_LIBS_INIT}
)

# Define helper functions and macros used by Google Test.
#include(cmake/internal_utils.cmake)

#config_compiler_and_linker()  # Defined in internal_utils.cmake.

# Where Google Test's .h files can be found.
include_directories(
    ${GTEST_INCLUDE_DIRECTORIES}
    .
)

link_directories(${GTEST_LINK_DIRECTORIES})
add_library(gtest SHARED ${GTEST_SOURCES})
target_link_libraries(gtest ${GTEST_LINK_LIBRARIES})

