import os
if os.name == 'nt': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

from devicemanagerinterface import TwinCAT as _twincat

class TwinCAT:

    _twincat = None

    def __init__(self, AmsNetId: str, ipAddr : str = ''):
        print('TwinCAT::__init__() called')
        
        if os.name == 'nt':
            self._twincat = _twincat(AmsNetId)

    def majorVersion(self) -> int:
        return self._twincat.getTcMajor()

    def minorVersion(self) -> int:
        return self._twincat.getTcMinor()

    def buildVersion(self) -> int:
        return self._twincat.getTcBuild()

    def all(self) -> dict:
        return {
            'TwinCAT Version' : str(self.majorVersion())
                              + '.' 
                              + str(self.minorVersion())
                              + '.' 
                              + str(self.buildVersion())
        }