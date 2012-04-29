# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='{{ project_name }}',
    version='0.0',
    packages=find_packages(),
    author='{{ project_name }} author',
    author_email='me@example.com',
    license='BSD',
    description='{{ project_name }} description',
    scripts=['manage.py',],
)
