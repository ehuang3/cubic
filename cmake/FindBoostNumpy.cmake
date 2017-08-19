# Find Boost.NumPy
find_package(PkgConfig QUIET)

find_path(BoostNumpy_INCLUDE_DIRS
    NAMES numpy.hpp
    PATHS "${CMAKE_INSTALL_PREFIX}/include/boost" "/usr/local/include/boost")

find_library(BoostNumpy_LIBRARY
    NAMES libboost_numpy.so
    PATHS "${CMAKE_INSTALL_PREFIX}/lib64" "/usr/local/lib")
