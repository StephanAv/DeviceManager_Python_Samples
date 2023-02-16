import os
from DeviceManager.cpu import CPU
from DeviceManager.mainboard import Mainboard
#import DeviceManager.cpu as _cpu



class Target:

    def __init__(self, AmsNetId: str, ipAddr : str = ''):
        print('Target::__init__() called')
        self.AmsNetId = AmsNetId
        self.ipAddr = ipAddr

        self.CPU = None
        self.CPU = CPU(self.AmsNetId, self.ipAddr)

        self.Mainboard = None
        self.Mainboard = Mainboard(self.AmsNetId, self.ipAddr)

#x = {}


def add_two(number):
    return number + 2