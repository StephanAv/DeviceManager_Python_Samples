import logging
#from tkinter import Misc
from devicemanager.cpu import CPU
from devicemanager.mainboard import Mainboard
from devicemanager.twincat import TwinCAT
from devicemanager.general import General
from devicemanager.device import Device
from devicemanager.miscellaneous import Miscellaneous
from devicemanager.file_system import FSO

class Target:

    def __init__(self, AmsNetId: str = '', ipAddr : str = '', timeout = 2000):

        logging.debug('Target::__init__() called')

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

        self.Device = None
        self.Device = Device(self.AmsNetId, self.ipAddr, timeout)

        self.Miscellaneous = None
        self.Miscellaneous = Miscellaneous(self.AmsNetId, timeout)

        self.FileSystem = None 
        self.FileSystem = FSO(self.AmsNetId, timeout)

    def reboot(self):
        self.Miscellaneous.reboot()

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

        if self.Device:
            try:
                targetInfo['Device'] = self.Device.all()
            except Exception as e:
                print('Exception reading Device: ' + str(e))
                pass

        return targetInfo
