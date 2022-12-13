#!/usr/bin/env python

from setuptools import setup, find_packages


python_requires = '>=3.6'


setup(
    name='soundinst',
    version='0.0.1',
    author='Telmo Menezes',
    author_email='telmo@telmomenezes.net',
    description='Sound installation',
    python_requires=python_requires,
    packages=find_packages(),
    install_requires=['pyserial'],
    entry_points='''
        [console_scripts]
        learner=soundinst.__main__:cli
    '''
)
