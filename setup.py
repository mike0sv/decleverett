# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup_args = dict(
    name='decleverett',
    version='0.0.2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/mike0sv/decleverett',
    license='Apache-2.0',
    author='mike0sv',
    author_email='mike0sv@gmail.com',
    description='Little wrapper for everett config library',
    install_requires=['everett'],
    extras_require={'yaml': 'everett[yaml]'})

if __name__ == '__main__':
    setup(**setup_args)
