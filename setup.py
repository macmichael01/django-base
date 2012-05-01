#!/usr/bin/env python
import os

from setuptools import setup, find_packages

from djangobase.generator import __version__


data_files = []
django_base_dir = 'djangobase/templates'
for dirpath, dirnames, filenames in os.walk(django_base_dir):
    file_list = [os.path.join(dirpath, f) for f in filenames]
    data_files.append([dirpath, file_list])

setup(
    name='Django-base',
    version=__version__,
    url="https://github.com/macmichael01/django-base",
    author='Chris McMichael',
    author_email='macmichael01@gmail.com',
    description='Django-base project setup',
    install_requires=('jinja2',),
    packages=('djangobase',),
    data_files=data_files,
    scripts=('djangobase/bin/mkdjango',),
    license="BSD",
    keywords="django python setup",
    long_description="Django base project setup",
    zip_safe=False,
)
