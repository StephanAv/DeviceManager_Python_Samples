import os
if os.name == 'nt': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

from devicemanagerinterface import General as _general

class General:

    _general = None

    def __init__(self, AmsNetId: str, ipAddr : str = ''):
        print('Mainboard::__init__() called')
        if os.name == 'nt':
            self._general = _general(AmsNetId)

    def name(self):
        return self._general.deviceName()