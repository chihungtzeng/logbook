cmake_minimum_required(VERSION 3.1)
project(cvfun)

find_package(OpenCV REQUIRED)

include_directories(
    ${OPENCV_INCLUDE_DIRS}
)

set(PROJ "imshow")
add_executable(${PROJ} ${PROJ}_main.cpp)
target_link_libraries(${PROJ} ${OpenCV_LIBRARIES})

set(PROJ "stitch")
add_executable(${PROJ} ${PROJ}_main.cpp)
target_link_libraries(${PROJ} ${OpenCV_LIBRARIES})
