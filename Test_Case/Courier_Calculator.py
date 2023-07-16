# #快递价格计算器
# print("欢迎来到快递价格系统！")
#
# dict1={"01":12,"02":20,"03":"None","04":10}
# dict2={"01":10,"02":20,"03":"Call Company","04":5}
#
# count=0
#
# while True:
#     weight=input("请输入重量（千克）：")#input默认接收字符串
#     num=input("请输入地点编号（01.东三省/宁夏/青海/海南 02.新疆/西藏 03.港澳台/国外 04.其他）：")
#     p = 0
#     if weight!="" and num!="":
#         weight=float(weight)
#         if weight>=3:
#             if num=="01" or num=="02" or num=="04":
#                 # p = 12 + 10 * (weight - 3)
#                 p = dict1[num] + dict2[num] * (weight - 3)
#             # elif num == "02":
#             #     # p = 20 + 20 * (weight - 3)
#             #     p = dict1[num] + dict2[num] * (weight - 3)
#             elif num == "03":
#                 # print("该地区不接受寄件！")
#                 print(dict1[num])
#             # elif num == "04":
#             #     # p = 10 + 5 * (weight - 3)
#             #     p = dict1[num] + dict2[num] * (weight - 3)
#             else:
#                 print("输入错误！")
#         elif weight<3 and weight>0:
#             if num=="01" or num=="02" or num=="04":
#                 # p = 12
#                 p = dict1[num]
#             # elif num == "02":
#             #     # p = 20
#             #     p = dict1[num]
#             elif num == "03":
#                 # print("该地区不接受寄件，请联系总公司！")
#                 print(dict2[num])
#             # elif num == "04":
#             #     # p = 10
#             #     p = dict1[num]
#             else:
#                 print("输入错误！")
#         else:
#             print("输入错误！")
#         print("您好，您的包裹价格为：", p, "元！")
#     else:
#         print("输入错误！")
#     print("您好，您的包裹价格为：",p,"元！")
#
#     count+=1
#
#     if count==3:
#         break



#快递价格计算器

print("欢迎来到快递价格系统！")

num=input("请输入地点编号（01.东三省/宁夏/青海/海南 02.新疆/西藏 03.港澳台/国外 04.其他）：")
weight=int(input("请输入重量（千克）："))

dict1={"01":12,"02":20,"03":"None","04":10}
dict2={"01":10,"02":20,"03":"Call Company","04":5}
p=0

if num == "01":
    if weight>=3:
        # p = 12 + 10 * (weight - 3)
        p = dict1[num] + dict2[num] * (weight - 3)
    else:
        # p = 12
        p = dict1[num]
elif num == "02":
    if weight >= 3:
        # p = 20 + 20 * (weight - 3)
        p = dict1[num] + dict2[num] * (weight - 3)
    else:
        # p = 12
        p = dict1[num]
elif num == "03":
    # print("该地区不接受寄件！")
    print(dict1[num])
elif num == "04":
    if weight>=3:
        # p = 10 + 5 * (weight - 3)
        p = dict1[num] + dict2[num] * (weight - 3)
    else:
        # p = 10
        p = dict1[num]
else:
    print("输入错误！")

print("您好，您的包裹价格为：", p, "元！")