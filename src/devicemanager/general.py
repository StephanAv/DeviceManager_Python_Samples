import platform, os, logging
if os.name == 'nt': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

from devicemanagerinterface import General as _general

#_dbg = hasattr(sys, 'gettotalrefcount')

class General:

    _general = None

    def __init__(self, AmsNetId: str, ipAddr : str = '', timeout = 2000):

        logging.debug('General::__init__() called')
        _system = platform.system()
        if _system == 'Windows' or _system == 'FreeBSD':
            self._general = _general(AmsNetId, timeout)
        else:
            self._general = _general(AmsNetId, ipAddr, timeout)

    def name(self) -> str:
        return self._general.deviceName()

    def all(self) -> dict:
        return {
            'Name' : self.name()
        }