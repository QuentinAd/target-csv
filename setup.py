#!/usr/bin/env python

from setuptools import setup

setup(name='target-csv',
      version='0.0.1',
      description='Singer-modified target for writing CSV files',
      author='Lokals Technologies, Ltd.',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['target_csv'],
      install_requires=[
          'jsonschema==2.6.0',
          'singer-python>=2.1.4',
      ],
      entry_points='''
          [console_scripts]
          target-csv=target_csv:main
      ''',
)
