#!/usr/bin/env python

from setuptools import setup
import os
import sys
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)



setup(
    name='pysample',
    license='License :: OSI Approved :: Python Software Foundation License',
    #py_modules=['foobar', ],
    packages=['pysample', ],
    version='0.1',
    install_requires=['requests'],
    tests_require=['pytest','pytest-xdist'],
    cmdclass= {'test':PyTest},

    description='A python package than can be used as a model/template for writing, testing and deploying python packages.',
    long_description=open('README.txt').read(),

    author='Sorin Sbarnea',
    author_email='sorin.sbarnea@gmail.com',
    url='https://github.com/pycontribs/pysample.git',

    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration :: Authentication/Directory",
    ]
)
