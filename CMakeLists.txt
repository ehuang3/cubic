cmake_minimum_required(VERSION 2.4.4 FATAL_ERROR)
project(cubic)

############################################################
## Libraries.
############################################################

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake;${CMAKE_MODULE_PATH}")

find_package(Eigen REQUIRED)

############################################################
## Definitions.
############################################################

set(TARGET_H
    Path.h
    Trajectory.h
    )

set(TARGET_SRC
    Path.cpp
    Trajectory.cpp
    )

include_directories(
    ${Eigen_INCLUDE_DIR}
    )

set(LIB_NAME
    cubic
    )

############################################################
## Build and Installation.
############################################################

SET(TARGET_NAME ${LIB_NAME} )
SET(TARGET_TARGETNAME ${LIB_NAME} )
ADD_LIBRARY(${LIB_NAME}
    SHARED
    ${TARGET_H}
    ${TARGET_H_NO_MODULE_INSTALL}
    ${TARGET_SRC}
    )

SET(INSTALL_INCDIR include)
SET(INSTALL_BINDIR bin)
SET(INSTALL_LIBDIR lib${LIB_POSTFIX})
SET(INSTALL_ARCHIVEDIR lib${LIB_POSTFIX})

SET(HEADERS_GROUP "Header Files")

SOURCE_GROUP(
    ${HEADERS_GROUP}
    FILES ${TARGET_H}
    )

INSTALL(
    TARGETS ${LIB_NAME}
    RUNTIME DESTINATION ${INSTALL_BINDIR} 
    LIBRARY DESTINATION ${INSTALL_LIBDIR} 
    ARCHIVE DESTINATION ${INSTALL_ARCHIVEDIR} 
    )

INSTALL (
    FILES       ${TARGET_H}
    DESTINATION ${INSTALL_INCDIR}/${LIB_NAME}
    )

CONFIGURE_FILE(cmake/${LIB_NAME}Config.cmake.in "${CMAKE_BINARY_DIR}/cmake/${LIB_NAME}Config.cmake" @ONLY)
INSTALL(FILES ${CMAKE_BINARY_DIR}/cmake/${LIB_NAME}Config.cmake DESTINATION share/${LIB_NAME})

############################################################
## Pymodule Build and Installation.
############################################################

find_package(PythonLibs 2.7 REQUIRED)
find_package(Boost COMPONENTS python REQUIRED)
find_package(BoostNumpy REQUIRED)
find_package(GLOG REQUIRED)

set(PYMODULE_H
    )

set(PYMODULE_SRC
    export_EigenNumpy.cpp
    pycubic_module.cpp
    )

include_directories(
    ${Eigen_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${Boost_INCLUDE_DIRS}
    ${BoostNumpy_INCLUDE_DIRS}
    ${GLOG_INCLUDE_DIRS}
    )

set(PYMODULE_NAME
    _cubic
    )

ADD_COMPILE_OPTIONS(-std=c++11)

ADD_LIBRARY(${PYMODULE_NAME}
    SHARED
    ${PYMODULE_H}
    ${PYMODULE_H_NO_MODULE_INSTALL}
    ${PYMODULE_SRC}
    )

TARGET_LINK_LIBRARIES(${PYMODULE_NAME}
    ${LIB_NAME}
    ${PYTHON_LIBRARIES}
    ${Boost_LIBRARIES}
    ${BoostNumpy_LIBRARY}
    ${GLOG_LIBRARIES}
    )

SET_TARGET_PROPERTIES(${PYMODULE_NAME}
    PROPERTIES
    PREFIX ""
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/cubic"
    )
