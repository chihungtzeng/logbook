find_package(LibDL REQUIRED)

set(MHOOK_SOURCES 
    chook.c 
    cpphook.cpp 
    mbook.cpp
    util_cpp.cpp
)

set(MHOOK_INCLUDE_DIRECTORIES ${CMAKE_CURRENT_SOURCE_DIR})
set(MHOOK_LINK_LIBRARIES ${LIBDL_LIBRARIES})

include_directories(${MHOOK_INCLUDE_DIRECTORIES})
add_library(mhook SHARED ${MHOOK_SOURCES})
target_link_libraries(mhook ${MHOOK_LINK_LIBRARIES})

