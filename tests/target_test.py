import os, sys, glob
from pathlib import Path
from inspect import getmembers

# 'lib.win-amd64-3.9'
extBinDir = Path().resolve() / 'build' / 'lib.win-amd64-3.9-pydebug'

if os.name == 'nt': # Load TwinCAT DLL when on Windows
    sys.path.append(str(extBinDir))

#### OPTIONS ####
bRebuild = True

if bRebuild:
    for f in glob.glob(str(extBinDir / '*.pyd')):
        os.remove(f)
    os.system('python_d setup.py build --debug')





import DeviceManager
#from DeviceManager.TargetDevice import Target
#from DeviceManager import TargetDevice
from DeviceManager.TargetDevice import Target
#for attr in getmembers(Target):
#    print(attr)



print('Process ID: ' + str(os.getpid()))

#target = Target('5.69.55.236.1.1') # Windows
target = Target('5.80.201.232.1.1') # TC/BSD

bCPU    = False
bMB     = True
try:
    ###### CPU #######

    if (cpu := target.CPU) and bCPU:
        print(cpu.all())
    else:
        print('CPU Module not available')

    #### Mainboard ####

    if(mb := target.Mainboard) and bMB:
        print(mb.serialNumber())
        print(mb.all())
    else:
        print('Mainboard Module not available')

except Exception as e:
    print(e)




input("Press Enter to exit...")