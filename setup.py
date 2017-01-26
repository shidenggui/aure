# coding:utf8
from setuptools import setup

import aure

long_desc = """
aure
===============

*  util for auto reload failed shell command Edit


Installation
--------------

pip install aure

Upgrade
---------------

    pip install aure --upgrade

Quick Start
--------------

::
    aure your shell command

"""

setup(
    name='aure',
    version=aure.__version__,
    description='util for auto reload failed shell command',
    long_description=long_desc,
    author='shidenggui',
    author_email='longlyshidenggui@gmail.com',
    license='BSD',
    url='https://github.com/shidenggui/aure',
    keywords='shell autoreload',
    install_requires=[
    ],
    entry_points={
        'console_scripts': ['aure=aure:main'],
    },
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'License :: OSI Approved :: BSD License'],
    py_modules=['aure'],
    package_data={},
)
