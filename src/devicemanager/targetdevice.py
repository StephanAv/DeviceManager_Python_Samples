import os
from devicemanager.cpu import CPU
from devicemanager.mainboard import Mainboard
from devicemanager.twincat import TwinCAT
from devicemanager.general import General

class Target:

    def __init__(self, AmsNetId: str, ipAddr : str = '', timeout = 2000):
        print('Target::__init__() called')
        self.AmsNetId = AmsNetId
        self.ipAddr = ipAddr

        self.CPU = None
        self.CPU = CPU(self.AmsNetId, self.ipAddr, timeout)

        self.Mainboard = None
        self.Mainboard = Mainboard(self.AmsNetId, self.ipAddr, timeout)

        self.TwinCAT = None
        self.TwinCAT = TwinCAT(self.AmsNetId, self.ipAddr, timeout)

        self.General = None
        self.General = General(self.AmsNetId, self.ipAddr, timeout)

    def all(self) -> dict:
        targetInfo = {}
        if self.CPU:
            try:
                targetInfo['CPU'] = self.CPU.all()
            except Exception as e:
                print('Exception reading CPU: ' + str(e))
                pass

        if self.Mainboard:
            try:
                targetInfo['Mainboard'] = self.Mainboard.all()
            except Exception as e:
                print('Exception reading Mainboard: ' + str(e))
                pass
            
        if self.TwinCAT:
            try:
                targetInfo['TwinCAT'] = self.TwinCAT.all()
            except Exception as e:
                print('Exception reading TwinCAT: ' + str(e))
                pass

        if self.General:
            try:
                targetInfo['General'] = self.General.all()
            except Exception as e:
                print('Exception reading TwinCAT: ' + str(e))
                pass

        return targetInfo
