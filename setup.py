import os, subprocess
from pathlib import Path
from shutil import copyfile, rmtree
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

DeviceManagerCmake = Extension(
    'devicemanagerinterface',
    sources = [],
    #extra_objects = ['devicemanagerinterface']
)

class CustomBuild(build_ext):

    def build_extensions(self):

        for ext in self.extensions:

            try:
                out = subprocess.check_output(['cmake', '--version'])
            except Exception:
                raise RuntimeError('Cannot find CMake executable')

            libBuildPath = Path(self.build_temp, 'lib')

            if not os.path.exists(libBuildPath):
                os.makedirs(libBuildPath)

            
            cfg = 'Debug' if self.debug else 'Release'


            # Build Python module
            prePackageDir = Path(self.get_ext_fullpath(ext.name)).parent.absolute()


            subprocess.check_call(['cmake', '-B', self.build_temp,
                                    '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY:PATH=' + str(prePackageDir),
                                    '-DCMAKE_ARCHIVE_OUTPUT_DIRECTORY:PATH=' + str(prePackageDir),
                                    '-DCMAKE_RUNTIME_OUTPUT_DIRECTORY:PATH=' + str(prePackageDir),
                                    '-DCMAKE_BUILD_TYPE=' + str(cfg)
                                    ])


            # Build
            subprocess.check_call(['cmake', '--build', self.build_temp, '--config', cfg])

            precursor = ext.name
            if os.name == 'nt':
                precursor += '.dll'
            else:
                precursor = 'lib' + precursor + '.so'

            if os.name == 'nt':
                binPrePath = prePackageDir / cfg / precursor
            else:
                binPrePath = prePackageDir / precursor
            binFinalPath = prePackageDir / ext._file_name

            copyfile(binPrePath, binFinalPath)

            # Copy PDB file also
            if cfg == 'Debug' and os.name == 'nt':
                pbdPrePath = prePackageDir / cfg / (ext.name + '.pdb')
                pdbFinalPath = prePackageDir / (ext.name + '.pdb')
                copyfile(pbdPrePath, pdbFinalPath)

            if os.name == 'nt':
                rmtree(prePackageDir / cfg)
            else:
                os.remove(binPrePath)
                files = os.listdir(prePackageDir)

                for _file in files:
                    if _file.endswith(".a"):
                        os.remove(os.path.join(prePackageDir, _file))



setup   ( 
        ext_modules = [DeviceManagerCmake],
        package_dir={'': 'src'},
        cmdclass = {'build_ext': CustomBuild}
        )