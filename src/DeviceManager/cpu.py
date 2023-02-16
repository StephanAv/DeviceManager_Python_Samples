import os
if os.name == 'nt': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

from DeviceManagerInterface import CPU as _cpu

class CPU:

    _cpu = None

    def __init__(self, AmsNetId: str, ipAddr : str = ''):
        print('CPU::__init__() called')
        
        if os.name == 'nt':
            self._cpu = _cpu(AmsNetId)


    def frequency(self) -> int:
        return self._cpu.getFreq()

    def usage(self) -> int:
        return self._cpu.getUsage()

    def temperature(self) -> int:
        return self._cpu.getTemp()

    def all(self) -> dict:
        return {
            'Frequency [MHz]' : self.frequency(),
            'Temperature [°C]' : self.temperature(),
            'Usage [%]' : self.usage()
        }