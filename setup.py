import os, subprocess, platform
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

arch = platform.architecture()
x86_64 = False
if arch[0] == '64bit':
    x86_64 = True






DeviceManagerInterface = Extension(
                    'devicemanagerinterface',
                    libraries = ['DeviceManager'],
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
                                   ]
                    )
# https://stackoverflow.com/questions/61260755/symbols-from-a-static-library-are-not-exported-while-linking-to-a-shared-library
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
                subprocess.check_call(['cmake', '-S', 'src/DeviceManager_ADS_Samples', '-B',  self.build_temp, 
                        '-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE',
                        '-DBUILD_SHARED_LIBS=OFF',
                        #'-DPOSITION_INDEPENDENT_CODE=ON'
                        '-DCMAKE_CXX_FLAGS=-fPIC'
                        ])

                # Build
                subprocess.check_call(['cmake', '--build', self.build_temp, '--target', 'DeviceManager', '--config', cfg])
                
                #set(CMAKE_POSITION_INDEPENDENT_CODE ON)
                build_path = os.path.relpath(self.build_temp)

                if os.name == 'nt':
                    ext.extra_compile_args.append('/std:c++17')
                    ext.extra_compile_args.append('/DUSE_TWINCAT_ROUTER')
                    ext.include_dirs.append('C:/TwinCAT/AdsApi/TcAdsDll/Include')

                    tcAdsDllLibDir = os.path.abspath('C:/TwinCAT/AdsApi/TcAdsDll/x64/lib') if x86_64 == True else os.path.abspath('C:/TwinCAT/AdsApi/TcAdsDll/lib')
                    ext.library_dirs.append(tcAdsDllLibDir)
                    ext.libraries.append('TcAdsDll')
                else: 
                    ext.extra_compile_args.append('-std=c++17') 
                    #ext.extra_compile_args.append('-Wl,--whole-archive') 


                    ext.extra_compile_args.append('-Wl,--whole-archive')
                    ads_libpath = os.path.join(build_path, '_deps', 'beckhoff_ads-build', 'libads.a')
                    ext.extra_compile_args.append(ads_libpath)


                    devman_libpath = os.path.join(build_path, 'libDeviceManager.a')
                    link_arg = '-Wl,--whole-archive {}'.format(os.path.join(build_path, 'libDeviceManager.a'))
                    #ext.extra_link_args.append('-Wl,--whole-archive {}'.format(os.path.join(build_path, 'libDeviceManager.a')))
                    ext.extra_compile_args.append('-Wl,--whole-archive')
                    ext.extra_compile_args.append(devman_libpath)




                    #ext.extra_compile_args.append('-fPIC') 
                    #ext.library_dirs.append(build_path)
                    #ext.extra_objects.append(os.path.join(build_path, 'libDeviceManager.a'))
                    ext.include_dirs.append(os.path.join(build_path, '_deps', 'beckhoff_ads-src', 'AdsLib'))


                lib_path = os.path.join(build_path, cfg)
                ext.library_dirs.append(build_path)
                ext.library_dirs.append(lib_path) # TODO: Same path on all configurations?
                
            super(CustomBuild, self).build_extension(ext)



setup   ( 
        ext_modules = [DeviceManagerInterface],
        package_dir={'': 'src'},
        cmdclass = {'build_ext': CustomBuild}
        )