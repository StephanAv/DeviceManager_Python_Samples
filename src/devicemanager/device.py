import os
if os.name == 'nt': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

from devicemanagerinterface import Device as _device

class Device:

    _device = None

    def __init__(self, AmsNetId: str, ipAddr : str = '', timeout = 2000):
        print('Device::__init__() called')
        
        if os.name == 'nt':
            self._device = _device(AmsNetId, timeout)

    def serialNumber(self) -> str:
        return self._device.serialNumber()

    def all(self) -> dict:
        return {
                'Serial Number' : self.serialNumber()
            }