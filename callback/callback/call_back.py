# -*- encoding: utf-8 -*-
# Author: Komorebi
# Date: 2023/6/30 18:38
# Describe:
class CallBackFunc(object):
    def __init__(self):
        self.event = {}

    # 定义回调函数double()
    def double(self, x):
        print(f"double()被调用")
        return x * 2

    # 定义回调函数quadruple()
    def quadruple(self, x):
        print("quadruple()被调用")
        return  x * 4

    # 定义中间函数getOddNumber(k, getEvenNumber)
    def getOddNumber(self, k, callback_name):
        k = k + 1
        print(f"k: {k}")
        # print(f"将k传递给{callback_name.__name__}")
        self.event[k] = callback_name
        return 1 + callback_name(k)

    # def describe(self, k, callFunc):


"""
调用main()函数
k: 2
将k传递给double
double()被调用
i: 5
k: 2
将k传递给quadruple
quadruple()被调用
i: 9
k: 2
将k传递给<lambda>
i: 17
"""
