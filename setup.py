"""A google image search scraper to automatically search and download images from the web
See
https://github.com/AlexNilsson/python-image-scraper
"""

# Developers:
# Install with:
#   pip install -e .
# Distribute with:
# python setup.py bdist_wheel
# twine upload dist/*

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='gscraper',
    version='0.1.2',
    packages=find_packages(),

    install_requires=['setuptools>=28.8.0'],

    author='Alexander Nilsson',
    author_email='contact@alexnilsson.io',
    description='Automatically download images from google image search',
    license="MIT",
    keywords='web scraper google image images search automatic download',
    url='https://github.com/AlexNilsson/python-image-scraper',


    long_description=long_description,
    long_description_content_type='text/markdown',

)
