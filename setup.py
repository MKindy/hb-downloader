#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
from setuptools import setup, find_packages

def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name="hb_downloader",  # your package name (i.e. for import)
    version="0.7.0",
    maintainer="Mark Kindy",
    maintainer_email="MKindy@gmail.com",
    author="Brian Schkerke, Mayeul Cantan, Claudius Coenen, Katrin Leinweber, Tobi Grimm, Mark Kindy",
    author_email="N/A, mayeul.cantan@live.fr, N/A, N/A, N/A, MKindy@gmail.com",
    description="An automated utility to download your Humble Bundle purchases.",
    license="MIT",
    keywords="humble bundle download games",
    url="https://github.com/MKindy/hb-downloader",
    packages=find_packages(exclude=["*test*", "*TEST*"]),
    install_requires=[
        'requests',
        'pyyaml',
        'lxml'
    ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT",
        "Natural Language :: English"
    ],
    zip_safe=True,
)
