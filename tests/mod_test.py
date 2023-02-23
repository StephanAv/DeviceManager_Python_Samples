import json

try:
    from devicemanager.targetdevice import Target
    
except Exception as e:
    print(e)

target = Target('5.69.55.236.1.1') # Windows

bTarget     = True
bCPU        = True
bMB         = True
bTC         = True

cpu     = target.CPU
mb      = target.Mainboard
tc      = target.TwinCAT

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

    if cpu and bCPU:
        print(cpu.all())
    else:
        print('CPU module not available on target')

    #### Mainboard ####

    if mb and bMB:
        print(mb.all())
    else:
        print('Mainboard module not available on target')

    ##### TwinCAT #####

    if tc and bTC:
        print(tc.all())
        tc.deleteAdsRoute('StephanA01.beckhoff.com')
    else:
        print('TwinCAT module not available on target')

except Exception as e:
    print(e)= Device(amsNetId)