import os
if os.name == 'nt': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

from devicemanagerinterface import FileSystem as _fso

def progress(x):
    print(str(x))

class FSO:

    _fso = None

    def __init__(self, AmsNetId: str, ipAddr : str = '', timeout = 2000):
        print('FSO::__init__() called')
        if os.name == 'nt':
            self._fso = _fso(AmsNetId, timeout)

    def read(self, targetFile : str, localFile: str, silent : bool = False) -> int:
        bytesRead = self._fso.readFile(targetFile, localFile, progress)
        bytesRead = 5
        return bytesRead

