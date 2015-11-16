#!/usr/bin/env python
"""
    Pip module setup
"""
from setuptools import setup

INSTALL_REQUIRES = [
    'click >= 0.5.0'
]

setup(name='elasticsearch-import',
      version='0.0.0',
      description='Elasticsearch data import',
      url='http://github.com/riguy724/elasticsearch-import',
      author='Christopher Riley',
      author_email='riguy724@gmail.com',
      license='MIT',
      install_requires=INSTALL_REQUIRES,
      packages=["import", "import/cli"],
      entry_points={
        'console_scripts': [
            'elastic-import=import.cli.main:hello',
        ],
      })
