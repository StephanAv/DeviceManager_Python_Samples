#fro    m gettext import bind_textdomain_codeset
from email.generator import BytesGenerator
import os, sys, glob
from shutil import rmtree
from pathlib import Path
from inspect import getmembers

# 'lib.win-amd64-3.9'
extBinDir = Path().resolve() / 'build' / 'lib.win-amd64-3.9-pydebug'

if os.name == 'nt': # Load TwinCAT DLL when on Windows
    sys.path.append(str(extBinDir))

#### OPTIONS ####
bBuild      = True
bRebuild    = True
bCPU        = False
bMB         = False
bTC         = False
bGen        = True


if bBuild:
    if bRebuild:
        for f in glob.glob(str(extBinDir / '*.pyd')):
            os.remove(f)
    try:
        rmtree(str(extBinDir / 'devicemanager'))
    except Exception:
        pass
    os.system('python_d setup.py build --debug')


try:
    from devicemanager.targetdevice import Target
except Exception as e:
    print(e)
print('Current Process ID: ' + str(os.getpid()))

target = Target('5.69.55.236.1.1') # Windows
#target = Target('5.80.201.232.1.1') # TC/BSD


try:
    ####### CPU ########

    if (cpu := target.CPU) and bCPU:
        print(cpu.all())
    else:
        print('CPU module not available on target')

    #### Mainboard ####

    if(mb := target.Mainboard) and bMB:
        print(mb.all())
    else:
        print('Mainboard module not available on target')

    ##### TwinCAT #####

    if(tc := target.TwinCAT) and bTC:
        print(tc.all())
        tc.deleteAdsRoute('StephanA01.beckhoff.com')
    else:
        print('TwinCAT module not available on target')

    #### General ####

    if(gen := target.General) and bGen:
        print(gen.name())
    else:
        print('General module not available on target')

except Exception as e:
    print(e)




input("Press Enter to exit...")