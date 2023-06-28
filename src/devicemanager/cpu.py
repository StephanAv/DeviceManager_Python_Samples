import platform, os, logging

if platform.system() == 'Windows': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

#isTcPlatform = platform.system() == 'Windows' or platform.system() == 'FreeBSD'

from devicemanagerinterface import CPU as _cpu


class CPU:

    _cpu = None

    def __init__(self, AmsNetId: str, ipAddr : str = '', timeout = 2000):
        
        logging.debug('CPU::__init__() called')
        
        if platform.system() == 'Windows':
            self._cpu = _cpu(AmsNetId, timeout)
        else:
            self_cpu = _cpu(AmsNetId, ipAddr, timeout)
            x = 3


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
