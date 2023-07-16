#个人所得税计算器

before=float(input("请输入税前工资："))
m1=float(input("请输入社保扣除金额："))

ss=0#纳税金额
ys=before-m1-5000#应纳税所得额

if ys<=3000 and ys>0:
    ss = ys * 0.03 - 0
elif ys<=12000:
    ss = ys * 0.10 - 210
elif ys <= 12000:
    ss = ys * 0.20 - 1410
elif ys <= 25000:
    ss = ys * 0.25 - 2660
elif ys <= 35000:
    ss = ys * 0.30 - 4410
elif ys <= 80000:
    ss = ys * 0.35 - 7160
elif ys > 80000:
    ss = ys * 0.40 - 15160

print("您应纳税金额为：", ss, "元！到手工资为：", before-m1-ss, "元！")
