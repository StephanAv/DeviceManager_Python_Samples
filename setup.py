import os, subprocess
from pathlib import Path
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

DeviceManagerCmake = Extension(
    'devicemanagerinterface',
    sources = []
)

class CustomBuild(build_ext):

    def build_extensions(self):

        for ext in self.extensions:

            if ext.name == 'devicemanagerinterface':
                try:
                    out = subprocess.check_output(['cmake', '--version'])
                except Exception:
                    raise RuntimeError('Cannot find CMake executable')

                libBuildPath = Path(self.build_temp, 'lib')

                if not os.path.exists(libBuildPath):
                    os.makedirs(libBuildPath)


                cfg = 'Debug' if self.debug else 'Release'
                
                # Build DeviceManager library

                # Config
                subprocess.check_call(['cmake', '-S', 'src/DeviceManager_ADS_Samples', '-B',  libBuildPath, 
                        '-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE',
                        '-DBUILD_SHARED_LIBS=OFF',
                        #'-DPOSITION_INDEPENDENT_CODE=ON'
                        '-DCMAKE_CXX_FLAGS=-fPIC'
                        ])

                # Build
                subprocess.check_call(['cmake', '--build', libBuildPath, '--target', 'DeviceManager', '--config', cfg])
                

                # Build Python module

                # Config
                subprocess.check_call(['cmake', '-B', self.build_temp])


                # Build
                subprocess.check_call(['cmake', '--build', self.build_temp, '--config', cfg])

                
            super(CustomBuild, self).build_extension(ext)


setup   ( 
        ext_modules = [DeviceManagerCmake],
        package_dir={'': 'src'},
        cmdclass = {'build_ext': CustomBuild}
        )