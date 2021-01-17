cmake_minimum_required(VERSION 3.0.0)
project(datarecordings VERSION 0.1.0)


add_executable(datarecordings lmsfilter.cpp)
target_link_libraries(datarecordings fir) 

find_package(iir)
target_link_libraries(datarecordings iir::iir)
target_link_libraries(datarecordings iir::iir_static)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
