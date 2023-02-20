import os
from devicemanager.cpu import CPU
from devicemanager.mainboard import Mainboard
from devicemanager.twincat import TwinCAT

class Target:

    def __init__(self, AmsNetId: str, ipAddr : str = ''):
        print('Target::__init__() called')
        self.AmsNetId = AmsNetId
        self.ipAddr = ipAddr

        self.CPU = None
        self.CPU = CPU(self.AmsNetId, self.ipAddr)

        self.Mainboard = None
        self.Mainboard = Mainboard(self.AmsNetId, self.ipAddr)

        self.TwinCAT = None
        self.TwinCAT = TwinCAT(self.AmsNetId, self.ipAddr)