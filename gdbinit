dir $cwd/src/devicemanager:$cwd/src/types:$cwd/src/DeviceManager_ADS_Samples/ADS
file python
set args -X dev tests/main.py

layout src
focus cmd

set breakpoint pending on
break src/types/py_slot_templates.h:96
#break getargs.c:1032