#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import setup, find_packages


def get_version():
    ROOT = os.path.dirname(__file__)
    VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')
    init = open(os.path.join(ROOT, 'jcs_sbs_sdk', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)

requires = [
        'lxml>=3.5.0',
        'setuptools>=20.7.0',
        'six>=1.10.0'
    ]

setup(
    name='jcs-python-sdk-sbs',
    version=get_version(),
    description='The JCS SBS SDK for Python',
    long_description=open('README.md').read(),
    author='Jio Cloud Services - Simple Block Storage',
    url='https://github.com/utsav-deep-rjil/jcs-python-sdk-sbs',
    scripts=[],
    install_requires=requires,
    packages=find_packages(exclude=['main']),
    classifiers=[
        'Development Status :: In Dev',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ],
)
