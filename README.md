# DeviceManager Python Samples

Build with Python 3.9

## Build & Debug

General Requirements

- C/C++ toolchain
- Python development package
- CMake

### Build platform wheel

Build platform wheel in virtual environment:
`python -m build --wheel`

Build platform wheel in native environment:
`python -m build --wheel --no-isolation`


### Debug instructions for Linux

#### Build CPython with Pydebug support

1. `cd ~`
2. `git clone https://github.com/python/cpython.git`
3. `git checkout 3.9`
4. `mkdir debug`
5. `cd debug`
6. `../configure --with-pydebug --enable-shared`
7. `make`
8. `sudo make install`

#### Build and Debug Devicemanager module

Make sure that `python` refers to the previously installed debug version of CPython.

1. `cd ~`
2. `git clone --recursive https://github.com/StephanAv/DeviceManager_Python_Samples.git && cd DeviceManager_Python_Samples/`
3. `python -m setup build --debug`
4. `gdb -x gdbinit`

### Debug instructions for Windows

Requirements:
- Visual Studio 2022 with MSVC C++ toolchain
- Python development libraries 
- Python debug installation: `python_d.exe` must be present in *Path* environment variables

#### Instructions

1. Build the module specifying debug interpreter: `python_d setup.py build --debug`
2. Open **python_dgb.sln** with Visual Studio 2022
3. Search path for debug build module must be explicit specified (see [tests/main.py](/tests/main.py))
4. No other **devicemanager** module may be present
5. Native code debugging must be set active in order to debug C/C++ sources
6. `python_d` must be selected as interpreter

#### Procedure for on target test (Windows)
 
Copy the **.whl* and [on_target_test.py](/tests/on_target_test.py) to *C:\Users\Administrator* on the target system.
Open the command prompt:

1. `cd %USERPROFILE%`
2. `python -m venv %USERPROFILE%\venv_devicemanager`
3. `venv_devicemanager\Scripts\activate`
4. `python -m pip install -I %USERPROFILE%\devicemanager-0.0.1-cp39-cp39-win_amd64.whl`
5. `python %USERPROFILE%\on_target_test.py`

### Build instructions for TwinCAT/BSD

1. Use pkg to install the following packages: `python39`, `py39-pip`, `py39-build`, `py39-wheel`, `git`, `cmake`, `os-generic-userland-devtools`
2. `cd ~`
3. `git clone --recursive https://github.com/StephanAv/DeviceManager_Python_Samples.git && cd DeviceManager_Python_Samples/`
4. `python3.9 -m build --wheel --no-isolation`
5. `python3.9 -m pip install -I dist/devicemanager-*`

### Tests

- [main.py](/tests/main.py) - Test scenario with remote target for debugging purpose
- [on_target_test.py](/tests/on_target_test.py) - For a direct test on a Beckhoff PC