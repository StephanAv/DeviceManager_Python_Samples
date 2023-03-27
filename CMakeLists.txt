cmake_minimum_required(VERSION 3.14)
project(pythonextension)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package (Python3 COMPONENTS Development)

add_library(devicemanagerinterface
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

OPTION(BUILD_SHARED_LIBS "" OFF)

add_subdirectory(src/DeviceManager_ADS_Samples)



if (WIN32)
    add_compile_definitions(USE_TWINCAT_ROUTER)

    target_include_directories(devicemanagerinterface PUBLIC "C:\\TwinCAT\\AdsApi\\TcAdsDll\\Include")
    target_link_libraries(devicemanagerinterface PUBLIC TcAdsDll.lib)

    if(CMAKE_SIZEOF_VOID_P EQUAL 8)
        target_link_directories(devicemanagerinterface PRIVATE "C:\\TwinCAT\\AdsApi\\TcAdsDll\\x64\\lib")
    elseif(CMAKE_SIZEOF_VOID_P EQUAL 4)
        target_link_directories(devicemanagerinterface PRIVATE "C:\\TwinCAT\\AdsApi\\TcAdsDll\\lib")
    endif()

elseif(UNIX) # Linux, FreeBSD or TwinCAT/BSD

    execute_process(
        COMMAND sh -c "kenv loader_brand"
        OUTPUT_VARIABLE manufacturer
    )
    set_property(TARGET DeviceManager PROPERTY POSITION_INDEPENDENT_CODE ON)
    
    if(${manufacturer} MATCHES beckhoff) # Use the TC1000 ADS Router on TwinCAT/BSD
        target_include_directories(devicemanagerinterface PUBLIC "/usr/local/include")
        target_link_directories(devicemanagerinterface PRIVATE "/usr/local/lib")
        target_link_libraries(devicemanagerinterface PUBLIC TcAdsDll)
        target_compile_definitions(devicemanagerinterface PUBLIC POSIX)
    else() # Linux build: Use Github ADS Router
        set_property(TARGET ads PROPERTY POSITION_INDEPENDENT_CODE ON)
    endif()
endif()



target_link_libraries(devicemanagerinterface PRIVATE DeviceManager ${Python3_LIBRARIES})

target_include_directories(devicemanagerinterface PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/src/types
        ${Python3_INCLUDE_DIRS}
)