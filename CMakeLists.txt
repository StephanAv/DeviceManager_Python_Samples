cmake_minimum_required(VERSION 3.14)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)


find_package(PythonInterp REQUIRED)
find_package(PythonLibs REQUIRED)

add_library(DeviceManagerWrapper
    SHARED 
        src/devicemanager_interface.cpp
        src/types/py_cpu.cpp
        src/types/py_twincat.cpp
        src/types/py_fso.cpp
        src/types/py_mainboard.cpp
        src/types/py_miscellaneous.cpp
        src/types/py_general.cpp
        src/types/py_device.cpp
)

if (WIN32)
    add_compile_definitions(USE_TWINCAT_ROUTER)

    target_include_directories(DeviceManagerWrapper PUBLIC "C:\\TwinCAT\\AdsApi\\TcAdsDll\\Include")
    target_link_libraries(DeviceManagerWrapper PUBLIC TcAdsDll.lib)

    if(CMAKE_SIZEOF_VOID_P EQUAL 8)
        target_link_directories(DeviceManagerWrapper PRIVATE "C:\\TwinCAT\\AdsApi\\TcAdsDll\\x64\\lib")
    elseif(CMAKE_SIZEOF_VOID_P EQUAL 4)
        target_link_directories(DeviceManagerWrapper PRIVATE "C:\\TwinCAT\\AdsApi\\TcAdsDll\\lib")
    endif()
endif()

add_subdirectory(src/DeviceManager_ADS_Samples)

target_link_libraries(DeviceManagerWrapper PRIVATE DeviceManager ${PYTHON_LIBRARIES})
target_include_directories(DeviceManagerWrapper PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/src/types
        ${PYTHON_INCLUDE_DIRS} 
)