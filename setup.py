# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        return ''

setup(
    name='{{ project_name }}',
    version='0.0',
    packages=find_packages(),
    author='{{ project_name }} author',
    author_email='me@example.com',
    license='BSD',
    description='{{ project_name }} description',
    long_description = read('README.rst'),
    scripts=['manage.py'],
    # see here for complete list of classifiers
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ),
)
