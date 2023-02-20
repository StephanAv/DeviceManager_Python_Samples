import os
if os.name == 'nt': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

from devicemanagerinterface import Mainboard as _mb

class Mainboard:

    _mb = None

    def __init__(self, AmsNetId: str, ipAddr : str = ''):
        print('Mainboard::__init__() called')
        if os.name == 'nt':
            self._mb = _mb(AmsNetId)

    def serialNumber(self) -> str:
        return self._mb.serialNumber()

    def minTemp(self) -> int:
        return self._mb.getMinTemp()

    def maxTemp(self) -> int:
        return self._mb.getMaxTemp()

    def temperature(self) -> int:
        return self._mb.getTemp()

    def all(self) -> dict:
        return {
            'Serial Number' : self.serialNumber(),
            'Min. Temperature [°C]' : self.minTemp(),
            'Max. Temperature [°C]' : self.maxTemp(),
            'Current Temperature [°C]' : self.temperature(),
        }
