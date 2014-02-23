#! /usr/bin/env python

import os
import shutil
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def create_config():
    print 'Installing config file to %s' % os.path.expanduser('~/.cinephile.yaml')
    shutil.copyfile('cinephile.yaml', os.path.expanduser('~/.cinephile.yaml'))


setup(
    name='cinephile',
    version='1.0',
    description='Python CLI tool to scan movie directory \
        recursively, normalize the filename and retrieve useful \
        information from imdb.',
    long_description=read('README.md'),
    license='MIT License',
    keywords='IMDB Movies Rating List',
    author='Navin Sylvester',
    author_email='navinsylvester@gmail.com',
    url='https://github.com/navinsylvester/cinephile',
    download_url='https://github.com/navinsylvester/cinephile/tarball/master',
    install_requires=[
        'PyYAML >= 3.10',
    ],
    py_modules=['cinephile'],
    # FIXME: Packaging scripts doesn't work this way for single file packages.
    # They should be moved to a directory for packaging data files.
    data_files=['cinephile.yaml'],
    include_package_data = True,
    entry_points={
        'console_scripts': ['cinephile = cinephile:main']
    },
    platforms=['any'],
    classifiers=[
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Environment :: Console',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'TTopic :: Utilities'
    ],
    zip_safe=True
)

# Save the config file in ~/.cinephile.yaml
create_config()