import os, logging
from tqdm import tqdm

if os.name == 'nt': # Load TwinCAT DLL when on Windows
    os.add_dll_directory('C:/TwinCAT/Common64')

from devicemanagerinterface import FileSystem as _fso



class FSO:

    _fso = None

    def __init__(self, AmsNetId: str, ipAddr : str = '', timeout = 2000):

        logging.debug('FSO::__init__() called')

        if os.name == 'nt':
            self._fso = _fso(AmsNetId, timeout)

    def read(self, targetFile : str, localFile: str, silent : bool = False) -> int:

        bytesRead = 0

        if silent:
            bytesRead = self._fso.readFile(targetFile, localFile)
        else:
            pBar = tqdm(total=100)
            fBar = lambda n: pBar.update((n+1) - pBar.n) 
            bytesRead = self._fso.readFile(targetFile, localFile, fBar)
            pBar.close()

        return bytesRead

    def write(self, targetFile : str, localFile: str, silent : bool = False) -> int:
        
        bytesWritten = 0
        
        if silent:
            bytesWritten = self._fso.writeFile(targetFile, localFile)
        else:
            pBar = tqdm(total=100)
            fBar = lambda n: pBar.update((n+1) - pBar.n) 
            bytesWritten = self._fso.writeFile(targetFile, localFile, fBar)

        return bytesWritten;
