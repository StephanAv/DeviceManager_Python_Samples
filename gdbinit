dir $cwd/src/devicemanager:$cwd/src/types:$cwd/src/DeviceManager_ADS_Samples/ADS
file python
set args -X dev tests/main.py

layout src

set breakpoint pending on
#break $cwd/src/types/py_slot_templates.h:69
break src/types/py_slot_templates.h:69