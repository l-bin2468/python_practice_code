#!/usr/bin/env python
from google.protobuf import json_format
import addr_pb2

person = addr_pb2.Person()
person.name = "付登龙"
person.id = 1
person.email = "1185694@qq.com"
person.phone.add(number="13386851858", type=addr_pb2.Person.MOBILE)  # 序列化成二进制
print("person")
print(person.SerializeToString())  # 从二进制反序列化

person1 = addr_pb2.Person()
person1.ParseFromString(person.SerializeToString())  # 转换成字典
print("json_format")
print(json_format.MessageToDict(person1, True))  # 从json数据反序列化

person2 = addr_pb2.Person()
json_format.Parse(json_format.MessageToJson(person1, True), person2)
print("person2")
print(person2)

addr = addr_pb2.AddressBook()
per = addr.person.add()
per.name = "3"
per.id = 3
per.email = "q@qq.com"
per.phone.add(number="123", type=addr_pb2.Person.PhoneType.Name(1))
print("addr")
print(addr)
