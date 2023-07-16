# -*- encoding: utf-8 -*-
# Author: Komorebi
# Date: 2023/6/25 19:44
# Describe:
# str = "xyzzzz12344512zzzzzzzzzyxx"
# print(str.strip("xy"))
#
# print("-----------")
# print("\n")
# print("-----------")
#
# print(100 and 200)
# print(100 or 200)
# print(True and True)
# print(True and False)
# print(False and False)
# print(True or True)
# print(False or True)
# print(False or False)

# t = ["a", "b", "c"]
# print(",".join(t))
import copy

from callback.call_back import CallBackFunc
from packcode.pack_code import PackPyCode

l1 = {"x": [1, 2, 3, 4], "u": 123}
l2 = copy.deepcopy(l1)
l2["x"][0] = 3
print(l2)

# main()

CallBackFunc().double(2)
PackPyCode().first_step()
