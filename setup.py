#!/usr/local/bin/python3

from distutils.core import setup

setup(
    name='woodcoinrpc',
    version='0.1',
    description='Woodcoin RPC',
    long_description=open('README.rst').read(),
    author='phm',
    author_email='<phm@woodcoin.org>',
    maintainer='phm',
    maintainer_email='<phm@woodcoin.org>',
    url='http://www.github.com/paulmadore/woodcoinrpc.py',
    packages=['woodcoinrpc'],
    classifiers=[
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'
    ]
)
