card1="10001"
pwd1="123456"
ban1=10000

card2="10002"
pwd2="123456"
ban2=100000

card3="10003"
pwd3="123456"
ban3=1000000

print("欢迎来到银行！")
times=0

while True:
    card=input("请输入银行卡号：")
    pwd=input("请输入银行卡密码：")
    ban = 0#余额

    if card == card1 and pwd == pwd1:
        ban = ban1
    elif card == card2 and pwd == pwd2:
        ban = ban2
    elif card == card3 and pwd == pwd3:
        ban = ban3
    else:
        times = times + 1
        if times>=3:
            print("您已经输错三次密码，卡已被锁，请联系柜台！")
            break
        else:
            print("卡号密码错误，请重新输入！")
            continue

    while True:
        num = input("请输入要办理的业务（1、存款 2、取款 3、退卡）:")
        if num == "1":
            inn = float(input("请输入存款金额："))
            if inn<0:
                print("存款金额需要大于0")
                continue
            else:
                ban = ban + inn
                print("存款成功！存入",inn,"元。余额",ban,"元！")
        elif num == "2":
            out = float(input("请输入取款金额："))
            if out>ban:
                print("余额不足！")
                continue
            else:
                ban = ban - out
                print("取款成功！取出",out,"余额为：",ban)
        elif num == "3":
            print("请收好卡片，欢迎下次再来！")
            break
        else:
            print("卡号密码错误，请重新输入！")
            continue