import os, sys
from inspect import getmembers

if os.name == 'nt': # Check Python version 
    os.add_dll_directory('C:/TwinCAT/Common64')
    sys.path.append('C:/Users/StephanA/source/repos/DeviceManager_ADS_Samples/out/build/x64-Release/PyModule')

print("sys.path:")
print('\n'.join(sys.path))
print('os.name: {}'.format(os.name))

import DeviceManager
from DeviceManager import *
print('Loaded DeviceManager binary: {}'.format(DeviceManager.__file__))

for attr in getmembers(DeviceManager):
    print(attr)