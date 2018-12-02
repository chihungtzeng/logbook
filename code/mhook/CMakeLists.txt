cmake_minimum_required(VERSION 2.8.3)
project(mhook)


set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake")

set(GTEST_DIR ${CMAKE_SOURCE_DIR}/gtest)

add_subdirectory(src)
add_subdirectory(${GTEST_DIR})
add_subdirectory(tests)
add_subdirectory(unit_tests)


