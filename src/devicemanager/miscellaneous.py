import platform, os, logging
if os.name == 'nt': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

from devicemanagerinterface import Miscellaneous as _miscellaneous

class Miscellaneous:

    _miscellaneous = None

    def __init__(self, AmsNetId: str, ipAddr : str = '', timeout = 2000):

        logging.debug('Miscellaneous::__init__() called')
        
        _system = platform.system()
        if _system == 'Windows' or _system == 'FreeBSD':
            self._miscellaneous = _miscellaneous(AmsNetId, timeout)
        else:
            self._miscellaneous = _miscellaneous(AmsNetId, ipAddr, timeout)

    def reboot(self):
        self._miscellaneous.reboot()
