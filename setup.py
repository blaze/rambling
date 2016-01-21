#!/usr/bin/env python

import os
from setuptools import setup

setup(name='knit',
      version='0.0.1',
      description='Python wrapper for YARN Application: distributed shell',
      url='http://github.com/blaze/knit/',
      maintainer='Benjamin Zaitlen',
      maintainer_email='bzaitlen@continuum.io',
      license='MIT',
      keywords='yarn',
      packages=['knit'],
      package_data={'knit': ['java_libs/knit-1.0-SNAPSHOT.jar']},
      install_requires=[],
      long_description=(open('README.rst').read() if os.path.exists('README.rst')
                        else ''),
      zip_safe=False)