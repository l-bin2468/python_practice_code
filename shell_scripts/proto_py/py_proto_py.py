#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Komorebi
# Date: 2023/7/26 21:52
# Describe:
from proto_pb2 import *

proto = Proto()
proto.p_age = 20
proto.p_name = "张三"
print("person")
print(proto)
print(proto.SerializeToString())

one = One()
one.id = 3
operson = one.proto
operson.p_age = 30
operson.p_name = "李四"
print("one")
print(one)

two = Two()
two.x = 1920
tone = two.one
tone.id = 39
tone.proto.p_age = 40
tone.proto.p_name = "王二"
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
