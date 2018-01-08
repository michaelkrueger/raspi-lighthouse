from setuptools import setup

setup(
    name='lighthouse_web',
    packages=['lighthouse_web'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
	ext_modules  = [Extension('_rpi_ws281x', 
                                     sources=['rpi_ws281x.i'],
                                     library_dirs=['../../rpi_ws281x'],
                                     libraries=['ws2811', 'rt'])]
)