import os, subprocess, platform
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

arch = platform.architecture() # TODO: Specify TcAdsDll library
x86_64 = False
if arch[0] == '64bit':
    x86_64 = True

tcAdsDllLibDir = os.path.abspath('C:/TwinCAT/AdsApi/TcAdsDll/x64/lib') if x86_64 == True else os.path.abspath('C:/TwinCAT/AdsApi/TcAdsDll/lib')


DeviceManagerInterface = Extension(
                    'devicemanagerinterface',
                    libraries = ['DeviceManager', 'TcAdsDll'],
                    sources =   [       'src/devicemanager_interface.cpp',
                                        'src/types/py_cpu.cpp',
                                        'src/types/py_device.cpp',
                                        'src/types/py_fso.cpp',
                                        'src/types/py_general.cpp',
                                        'src/types/py_mainboard.cpp',
                                        'src/types/py_miscellaneous.cpp',
                                        'src/types/py_twincat.cpp',
                                ],
                    include_dirs = [    'src/types',
                                        'src/DeviceManager_ADS_Samples/ADS',
                                        'src/DeviceManager_ADS_Samples/Areas',
                                        'C:/TwinCAT/AdsApi/TcAdsDll/Include'
                                   ],
                    library_dirs=[tcAdsDllLibDir],
                    extra_compile_args=['/std:c++17',  '/DUSE_TWINCAT_ROUTER' ]
                    )

class CustomBuild(build_ext):

    def build_extensions(self):

        for ext in self.extensions:

            if ext.name == 'devicemanagerinterface':
                try:
                    out = subprocess.check_output(['cmake', '--version'])
                except Exception:
                    raise RuntimeError('Cannot find CMake executable')

                if not os.path.exists(self.build_temp):
                    os.makedirs(self.build_temp)

                cfg = 'Debug' if self.debug else 'Release'
                
                # Config
                subprocess.check_call(['cmake', '-S', 'src/DeviceManager_ADS_Samples', '-B',  self.build_temp, '-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE'])

                # Build
                subprocess.check_call(['cmake', '--build', self.build_temp, '--target', 'DeviceManager', '--config', cfg])
                
                build_path = os.path.relpath(self.build_temp)
                lib_path = os.path.join(build_path, cfg)
                ext.library_dirs.append(build_path)
                ext.library_dirs.append(lib_path) # TODO: Same path on all configurations?
                
            super(CustomBuild, self).build_extension(ext)



setup   ( 
        ext_modules = [DeviceManagerInterface],
        package_dir={'': 'src'},
        cmdclass = {'build_ext': CustomBuild}
        )