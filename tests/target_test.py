import logging
from asyncio import base_futures
from email import base64mime
import os, sys, glob, json
from shutil import rmtree
from pathlib import Path
from inspect import getmembers

# 'lib.win-amd64-3.9'
extBinDir = Path().resolve() / 'build' / 'lib.win-amd64-3.9-pydebug'

if os.name == 'nt': # Load TwinCAT DLL when on Windows
    sys.path.append(str(extBinDir))

#### OPTIONS ####
bRebuildCpp = False
bRebuildPy  = False
bTarget     = False
bCPU        = True
bMB         = False
bTC         = False
bGen        = False
bMisc       = False
bFSO        = True
logging.basicConfig(level=logging.DEBUG)

if bRebuildCpp:

    files = os.listdir(extBinDir)

    for _file in files:
        if _file.endswith(".pyd") or _file.endswith(".pdb"):
            os.remove(os.path.join(extBinDir, _file))

if bRebuildPy:
    try:
        rmtree(str(extBinDir / 'devicemanager'))
    except Exception:
        pass

if bRebuildCpp or bRebuildPy:
    os.system('python_d setup.py build --debug')


try:
    from devicemanager.targetdevice import Target
except Exception as e:
    print(e)
print('Current Process ID: ' + str(os.getpid()))

#target = Target('5.69.55.236.1.1', timeout = 2500) # Windows
#target = Target('5.69.55.236.1.1') # Windows
target = Target('5.80.201.232.1.1') # TC/BSD


##### Target #####
if bTarget:
    try:
        #print(target.all())
        print(json.dumps(target.all(),sort_keys=True, indent=4))
    except Exception as e:
        print(e)
        pass

try:

    ####### CPU ########

    if (cpu := target.CPU) and bCPU:
        print(cpu.frequency())
        #print(cpu.usage())
        #print(cpu.temperature())
        #print(cpu.all())
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

    ##### File System #####

    if(fso := target.FileSystem) and bFSO:
        #bytesRead = fso.read('C:/TwinCAT/3.1/Boot/AdsFileBrowser.zip', 'C:/Users/StephanA/Downloads/AdsFileBrowser.zip')
        #bytesRead = fso.read('C:/TwinCAT/3.1/Boot/AdsFileBrowser.zip', 'C:/Users/StephanA/Downloads/AdsFileBrowser.zip', silent = True)
        #bytesRead = fso.read('C:/TwinCAT/3.1/Boot/AdsFileBrowser.zip', 'C:/Users/StephanA/Downloads/AdsFileBrowser.zip')
        #print('Bytes read from target: {}'.format(bytesRead))
        #bytesWritten = fso.write('C:/TwinCAT/3.1/Boot/test.jpeg', 'C:/Users/StephanA/Downloads/test.jpeg')
        #print('Bytes written to target: {}'.format(bytesWritten))
        #bytesWritten = fso.write('C:/TwinCAT/3.1/Boot/test.jpeg', 'C:/Users/StephanA/Downloads/test.jpeg', silent = True)
        #print('Bytes written to target: {}'.format(bytesWritten))
        #bytesWritten = fso.write('C:/TwinCAT/3.1/Boot/test.jpeg', 'C:/Users/StephanA/Downloads/test.jpeg')
        #print('Bytes written to target: {}'.format(bytesWritten))
        folder, files = fso.dir('/usr/local/etc/TwinCAT/3.1/Boot/*')
    else:
        print('File System module not available on target')


    #### General ####

    if(gen := target.General) and bFSO:
        print(gen.name())
    else:
        print('General module not available on target')

    if bMisc:
        target.reboot()



except Exception as e:
    print(e)




input("Press Enter to exit...")