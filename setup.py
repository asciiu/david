# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='david',
    version='0.1.0',
    description='Daily Journey',
    long_description=readme,
    author='Satori Wilde',
    author_email='swilde@kwondo.com',
    url='https://github.com/asciiu/david',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

