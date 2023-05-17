# DeviceManager_Python_Samples

Build with Python 3.9

## Build & Debug

General Requirements

- C/C++ toolchain
- Python development package
- CMake


#### Build platform wheel

Build platform wheel in virtual environment:
`python -m build --wheel`

Build platform wheel in native environment:
`python -m build --wheel --no-isolation`


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


### Tests

- [main.py](/tests/main.py) - Test scenario with remote target for debugging purpose
- [on_target_test.py](/tests/on_target_test.py) - For a direct test on a Beckhoff PC

##### Procedure for target test (cmd.exe)
 
Copy the **.whl* and [on_target_test.py](/tests/on_target_test.py) to *C:\Users\Administrator* on the target system.
Open the command prompt:

1. `cd %USERPROFILE%`
2. `python -m venv %USERPROFILE%\venv_devicemanager`
3. `venv_devicemanager\Scripts\activate`
4. `python -m pip install -I %USERPROFILE%\devicemanager-0.0.1-cp39-cp39-win_amd64.whl`
5. `python %USERPROFILE%\on_target_test.py`