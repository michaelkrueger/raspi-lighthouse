from setuptools import setup

setup(
    name='lighthouse-web',
    packages=['lighthouse'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)