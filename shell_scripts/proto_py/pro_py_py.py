#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Komorebi
# Date: 2023/7/26 21:52
# Describe:
from pro_py_pb2 import *

person = Person()
person.age = 20
person.name = "张三"
print("person")
print(person)
print(person.SerializeToString())

one = One()
one.id = 3
operson = one.person
operson.age = 30
operson.name = "李四"
print("one")
print(one)

two = Two()
two.x = 1920
tone = two.one
tone.id = 39
tone.person.age = 40
tone.person.name = "王二"
# two.one.MergeFrom(one)
print("two")
print(two)

three = Three()
three.y = 1080
ttwo = three.two
# ttwo.x = 49
# ttwo.one.person.age = 50
# ttwo.one.person.name = "王二"
three.two.MergeFrom(two)
print("three")
print(three)
