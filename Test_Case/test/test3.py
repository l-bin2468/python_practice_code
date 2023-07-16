# -*- encoding:utf-8 -*-

# f1 = open("./1.txt", "r", encoding="utf-8")
# x = input("用户名：")
# y = input("密码：")
# txt = f1.read().strip("\n")
# index = txt.find(x)
# if -1 != index:
#     lines = txt.split("\n")
#     for i in lines:
#         line = i.strip("\n")
#         xy = line.split(",")
#         x1 = xy[0]
#         y1 = xy[1]
#         if x1 == x:
#             if y1 == y:
#                 print("zhengque")
#             else:
#                 print("cuowu")
# else:
#     print("cuowu")
#
#
#
# # 账号对，密码对 预期正确 实际错误 王五  88888
# # 账号错，密码对 预期错误 实际错误
# # 账号
import math

# a = eval(input("边长一："))
# b = eval(input("边长二："))
# c = eval(input("边长三："))
# d = eval(input("边长四："))
# m = eval(input("对角之和："))
# z = a + b + c + d
# x = z / 2
# print("z", z)
# print("x", x)
# s1 = (x - a) * (x - b) * (x - c) * (x - d)
# s2 = a * b * c * d
s3 = abs((math.modf(math.cos(112.5)))[1])
# s4 = s2 * s3
# s = math.sqrt(s1 - s4)
# print(s1)
# print(s2)
print("s3", s3)
# print(s4)
# print(s)

# 256.0
# 256
# 0.2007699654710709
# 51.39711116059415
# 16.0