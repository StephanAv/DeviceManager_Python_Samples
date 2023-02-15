import os, sys
from inspect import getmembers

if os.name == 'nt': # Check Python version 
    os.add_dll_directory('C:/TwinCAT/Common64')
    #sys.path.append('C:/Users/StephanA/source/repos/DeviceManager_ADS_Samples/out/build/x64-Release/PyModule')

#print("sys.path:")
#print('\n'.join(sys.path))
#print('os.name: {}'.format(os.name))

import DeviceManagerInterface
from DeviceManagerInterface import *
#print('Loaded DeviceManager binary: {}'.format(DeviceManager.__file__))

for attr in getmembers(DeviceManagerInterface):
    print(attr)


# Windows 10

amsNetId = "5.69.55.236.1.1"  
ipAddr   = "192.168.1.102"

# TwinCAT/BSD

#amsNetId = "5.80.201.232.1.1" 
#ipAddr   = "192.168.1.98"

#if os.name == 'nt': 
    #cpu = CPU(amsNetId)
    #tc  = TwinCAT(amsNetId)
    #fs   = FileSystem(amsNetId)
    #mb = Mainboard(amsNetId)
    #misc  = Miscellaneous(amsNetId)
    #general = General(amsNetId)
    #device = Device(amsNetId)