# -*- encoding: utf-8 -*-
# Author: Komorebi
# Date: 2023/7/3 21:07
# Describe:
from distutils.core import setup
# from setuptools import setup

setup(
    name="packcode",
    version="0.1",
    description="This is my app.",
    author="K",
    # py_modules=["callback/call_def", "packcode/pack_code"],
    # 依赖包
    # requires=[],
    # install_requires=[],
    packages=["callback.back", "packcode"],
    # packages=find_packages(),
    include_package_data=True,
)

# command
# python setup.py sdist bdist_wheel
# 打包需要带非py文件时，需要创建MANIFEST.in文件。例：recursive-include(不需要递归，可以把recursive-include改成include) package *.tar.gz
