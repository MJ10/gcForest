from __future__ import absolute_import, print_function

import io
import re
from os.path import dirname
from os.path import join

from setuptools import setup, find_packages


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()


setup(
    name='gcforest',
    url="https://github.com/MJ10/gcForest",
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Data scientists',
        'Topic :: Deep Learning :: Deep Forests',

        'Programming Language :: Python 2.7 :: Python 3.3+',
    ],
    keywords='random forest :: deep learning',
    version='1.1.1',
    license='MIT',
    description='This is the official implementation of the deep forest method',
    long_description=re.compile('^.. start-badges.*^.. end-badges',
                                re.M | re.S).sub('', read('README.md')),
    packages=["gcforest"],
    include_package_data=True,
    zip_safe=False,
)