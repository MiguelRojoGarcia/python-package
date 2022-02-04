from setuptools import setup

setup(
   name='MyCLIPackages',
   version='0.1.0',
   author='Miguel Rojo',
   author_email='miguel_rggame@hotmail.com',
   packages=['my_cli_package'],
   scripts=['scripts/test.sh'],
   description='This package contains modules of general purpose.',
   long_description=open('README.md').read(),
   install_requires=[
       "mysql-connector-python",
       "pytest",
   ],
)