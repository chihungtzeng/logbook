
SET(UNIT_TEST_MBOOK_SOURCES 
    mbook_unittest.cpp
    ${GTEST_DIR}/src/gtest_main.cc
)
SET(UNIT_TEST_MBOOK_INCLUDE_DIRECTORIES 
    ${CMAKE_SOURCE_DIR}/src
    ${GTEST_DIR}/include
)
SET(UNIT_TEST_MBOOK_LIBRARIES
    gtest
    mhook
    ${LIBDL_LIBRARIES}
)



include_directories(${UNIT_TEST_MBOOK_INCLUDE_DIRECTORIES})
add_executable(unit_test_mbook ${UNIT_TEST_MBOOK_SOURCES})
target_link_libraries(unit_test_mbook ${UNIT_TEST_MBOOK_LIBRARIES})

