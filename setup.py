
import glob
import sys
import os
from setuptools import setup, find_packages
from iosbackups import __version__

setup(
    name = 'iosbackups',
    keywords = 'osx ios backup data',
    description = 'Module to get data from iOS device backups',
    author = 'Ilkka Tuohela',
    author_email = 'hile@iki.fi',
    url = 'https://github.com/hile/iosbackups/',
    version = __version__,
    license = 'PSF',
    packages = find_packages(),
    scripts = glob.glob('bin/*'),
    install_requires = (
        'systematic',
    ),
)

