# -*- encoding:utf-8 -*-

import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
print(rootPath)
sys.path.append(os.path.split(rootPath)[0])
print(os.path.split(rootPath)[0])
