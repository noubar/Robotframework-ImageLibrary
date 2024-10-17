# -*- coding: utf-8 -*-
from os.path import abspath, dirname, join as path_join
from setuptools import setup, find_packages
from src.ImageHorizonLibrary.version import VERSION

SETUPDIR = abspath(dirname(__file__))

KEYWORDS = ('imagerecognition gui robotframework testing testautomation '
            'acceptancetesting atdd bdd')

SHORT_DESC = ('Cross-platform Robot Framework library for GUI automation '
              'based on image recognition')

with open(path_join(SETUPDIR, 'README.rst'), 'r') as readme:
    LONG_DESCRIPTION = readme.read()

with open(path_join(SETUPDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

CLASSIFIERS = '''
Development Status :: 5 - Production/Stable
Programming Language :: Python :: 3 :: Only
Operating System :: OS Independent
Framework :: Robot Framework
Framework :: Robot Framework :: Library
Topic :: Software Development :: Testing
License :: OSI Approved :: MIT License
'''.strip().splitlines()

setup(name='robotframework-imagehorizonlibrary',
      author='Eficode Oy',
      author_email='info@eficode.com',
      url='https://github.com/Eficode/robotframework-imagehorizonlibrary',
      license='MIT',
      platforms='any',
      packages=find_packages('src'),
      package_dir={'ImageHorizonLibrary': 'src/ImageHorizonLibrary'},
      install_requires = REQUIREMENTS,
      keywords=KEYWORDS,
      classifiers=CLASSIFIERS,
      version=VERSION,
      description=SHORT_DESC,
      long_description_content_type="text/markdown",
      long_description=LONG_DESCRIPTION)
