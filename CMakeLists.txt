cmake_minimum_required(VERSION 3.0.0)
project(lmsfilter VERSION 0.1.0)

add_subdirectory(clBP)

add_executable(lmsfilter lmsfilter.cpp)
target_link_libraries(lmsfilter fir) 
find_package(iir)
target_link_libraries(lmsfilter iir::iir)
target_link_libraries(lmsfilter iir::iir_static)
target_link_libraries(lmsfilter fir clBP) 

add_executable(LMS LMS.cpp)
target_link_libraries(LMS fir) 
find_package(iir)
target_link_libraries(LMS iir::iir)
target_link_libraries(LMS iir::iir_static)
target_link_libraries(LMS fir clBP) 

add_executable(butterworth butterworth.cpp parameters.h)
find_package(iir)
target_link_libraries(butterworth iir::iir)
target_link_libraries(butterworth iir::iir_static)
target_link_libraries(butterworth fir clBP) 

add_executable(DNF DNF.cpp parameters2.h)
find_package(iir)
target_link_libraries(DNF iir::iir)
target_link_libraries(DNF iir::iir_static)
target_link_libraries(DNF fir clBP) 

add_executable(prefilter prefilter.cpp)
target_link_libraries(prefilter fir)
find_package(iir)
target_link_libraries(prefilter iir::iir)
target_link_libraries(prefilter iir::iir_static)


set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
