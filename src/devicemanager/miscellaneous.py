import os
if os.name == 'nt': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

from devicemanagerinterface import Miscellaneous as _miscellaneous

class Miscellaneous:

    _miscellaneous = None

    def __init__(self, AmsNetId: str, ipAddr : str = '', timeout = 2000):
        print('Miscellaneous::__init__() called')
        
        if os.name == 'nt':
            self._miscellaneous = _miscellaneous(AmsNetId, timeout)


    def reboot(self):
        self._miscellaneous.reboot()
