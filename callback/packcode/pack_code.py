# -*- encoding: utf-8 -*-
# Author: Komorebi
# Date: 2023/7/3 22:24
# Describe:
class PackPyCode(object):
    def first_step(self):
        print("touch setup.py")
        print("python setup.py build")
        print("python setup.py sdist")
        print("python install name-version.tar.gz")
