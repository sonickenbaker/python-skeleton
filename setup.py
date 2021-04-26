#!/usr/bin/env python

from os.path import dirname
import os
import sys

from setuptools import setup
from setuptools import find_packages

base_dir = os.path.join(dirname(__file__), "src")
sys.path.append(base_dir)

import python_skeleton  # noqa


with open("requirements.txt") as f:
    required_list = f.read().splitlines()

packages = find_packages(where=os.path.join(dirname(__file__), "src"))
print(required_list)
print(packages)
setup(
    name=python_skeleton.PROJECT_NAME,
    version=python_skeleton.__version__,
    author="Sonickenbaker",
    author_email="sonickenbaker@gmail.com",
    description="Example Package",
    url="https://github.com/sonickenbaker/python-skeleton",
    install_requires=required_list,
    scripts=["bin/example.py"],
    packages=packages,
    package_dir={"python_skeleton": "src/python_skeleton"},
    #    data_files=[
    #        ("data", ["data/data.yaml"]),
    #        ("templates", ["templates/{}".format(x) for x in os.listdir("templates")]),
    #    ],
    python_requires=">=3.7",
)
