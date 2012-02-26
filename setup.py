#!/usr/bin/env python
import os

from distutils.core import setup

from setuptools import find_packages

django_base_dir = 'djangobase/project_template'

data_files = []
for dirpath, dirnames, filenames in os.walk(django_base_dir):
    file_list = [os.path.join(dirpath, f) for f in filenames]
    data_files.append([dirpath, file_list])

setup(
    name='Django-base',
    version='0.91',
    url="https://github.com/macmichael01/django-base",
    author='Chris McMichael',
    author_email='macmichael01@gmail.com',
    description='Django-base project setup',
    install_requires=('jinja2',),
    packages = ['djangobase/'],
    data_files = data_files,
    scripts = ['djangobase/scripts/mkdjango'],
    license="BSD",
    keywords="django python setup",
    long_description="Django base project setup",
)