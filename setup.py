#!/usr/bin/env python
"""
    Pip module setup
"""
from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'Click'
]

setup(
    name='elastic-import',
    version='0.0.3',
    description='Elasticsearch data import',
    url='http://github.com/riguy724/elasticsearch-import',
    author='Christopher Riley',
    author_email='riguy724@gmail.com',
    license='MIT',
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    packages=find_packages(),
    entry_points={
      'console_scripts': [
          'elastic-import = esimport.cli.main:hello',
      ],
    },
)
