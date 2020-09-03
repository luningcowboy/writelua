cmake_minimum_require(VERSION 2.8)
project(leptjson_test C)
if (CMAKE_COMPILER_ID MATCHES "GUN|Clang")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -ansi -pedantic -Wall")
endif()

add_library(leptjson leptjson.c)
add_executable(leptjson_test test.c)
target_link_libraries(leptjson_test leptjson)
