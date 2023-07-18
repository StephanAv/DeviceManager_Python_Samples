import platform, os, logging
if os.name == 'nt': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

from devicemanagerinterface import Device as _device



class Device:

    _device = None

    def __init__(self, AmsNetId: str, ipAddr : str = '', timeout = 2000):
        
        logging.debug('Device::__init__() called')
        
        _system = platform.system()
        if _system == 'Windows' or _system == 'FreeBSD':
            self._device = _device(AmsNetId, timeout)
        else:
            self._device = _device(AmsNetId, ipAddr, timeout)

    def serialNumber(self) -> str:
        return self._device.serialNumber()

    def all(self) -> dict:
        return {
                'Serial Number' : self.serialNumber()
            }