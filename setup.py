import os, subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

DeviceManagerInterface = Extension(
                    'DeviceManagerInterface',
                    libraries = ['DeviceManagerInterface'],
                    sources = ['python_devicemanager.cpp'],
                    extra_compile_args=['-std=c++17']
                    )

class CustomBuild(build_ext):

    def build_extensions(self):

        for ext in self.extensions:
            print("Test")
            if ext.name == 'DeviceManager':
                try:
                    out = subprocess.check_output(['cmake', '--version'])
                except Exception:
                    raise RuntimeError('Cannot find CMake executable')

                if not os.path.exists(self.build_temp):
                    os.makedirs(self.build_temp)

                cfg = 'Debug' if self.debug else 'Release'
                
                # Config
                subprocess.check_call(['cmake', '-S', 'DeviceManager_ADS_Samples', '-B',  self.build_temp])

                # Build
                subprocess.check_call(['cmake', '--build', self.build_temp, '--target', 'DeviceManager', '--config', cfg])

                ext.library_dirs.append(self.build_temp)

            super(CustomBuild, self).build_extension(ext)



setup   ( 
        #name='DeviceManager', 
        ext_modules = [DeviceManagerInterface],
        cmdclass = {'build_ext': CustomBuild}
        )