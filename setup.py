#!/usr/bin/env python
# -*- coding: utf-8 -*-

# disable python setup.py register error
import sys
reload(sys).setdefaultencoding("UTF-8")
from setuptools import setup, find_packages
import os
import codecs

version = '1.2'

setup(name='Products.ChinaPak',
      version=version,
      description="Chinese new translation and a normalizer for Plone 4",
      long_description=open("README.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        ],
      keywords='plone i18n chinese normalizer translation chinapak',
      author='andelf',
      author_email='andelf@gmail.com',
      url='http://github.com/andelf/Products.ChinaPak',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
