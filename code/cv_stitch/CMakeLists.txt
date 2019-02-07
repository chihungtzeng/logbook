cmake_minimum_required(VERSION 3.1)
project(cvfun)

find_package(OpenCV REQUIRED)

include_directories(
    ${OPENCV_INCLUDE_DIRS}
)

add_executable(imshow imshow_main.cpp)

target_link_libraries(
    imshow
    ${OpenCV_LIBRARIES})
