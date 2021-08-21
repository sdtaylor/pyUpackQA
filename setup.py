from setuptools import setup, find_packages

# Package meta-data.
NAME = 'pyUnpackQA'
DESCRIPTION = 'QA bit unpacking for Landsat, MODIS, Sentinal, VIIRS, and more.'
URL = 'https://github.com/sdtaylor/pyUnpackQA'
AUTHOR = 'Shawn Taylor'
LICENSE = 'MIT'
REQUIRES_PYTHON = '>=3.6.0'

# What packages are required for this module to be executed?
REQUIRED = [
    'numpy',
]

version = {}
with open('pyUnpackQA/version.py') as fp:
    exec(fp.read(), version)
VERSION = version['__version__']

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      url=URL,
      author=AUTHOR,
      license=LICENSE,
      packages=[NAME],
      python_requires=REQUIRES_PYTHON,
      zip_safe=False)