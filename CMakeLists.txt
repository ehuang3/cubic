cmake_minimum_required(VERSION 2.4.4 FATAL_ERROR)
project(trajectories)

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
    trajectories
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
