#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

PACKAGE_NAME = 'electronics_lab'

requirements = ['pyvisa', 'numpy', 'python-vxi11', 'pyvisa-py',
'bumpversion==0.5.3',
'wheel==0.32.1',
'watchdog==0.9.0',
'flake8==3.5.0',
'tox==3.5.2',
'coverage==4.5.1',
'Sphinx==1.8.1',
'twine==1.12.1']

setup_requirements = []

test_requirements = []

# _entry_points = {
#     'console_scripts': [
#         f'cli={PACKAGE_NAME}.cli:main'
#     ],
# }

_scripts = [f'{PACKAGE_NAME}/cli.py']

setup(
    author="Derick Hess",
    author_email='derick.hess@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Drivers and tools for my personal eldectronics lab equipment",
    # entry_points=_entry_points,
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='electronics_lab',
    name='electronics_lab',
    packages=find_packages(include=['electronics_lab', 'drivers']),
    setup_requires=setup_requirements,
    scripts=_scripts,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/derick-hess/electronics_lab',
    version='0.1.0',
    zip_safe=False,
)
