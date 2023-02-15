import os, sys
from inspect import getmembers

from DeviceManager import TargetDevice

for attr in getmembers(TargetDevice):
    print(attr)