# -*- encoding:utf-8 -*-

# import datetime
# import time
# import itchat
#
# # 登录微信
# itchat.auto_login(hotReload=False)
# # 获取朋有列表
# friends_list = itchat.get_friends(update=True)
# name = itchat.search_friends(name=u'bin')
# Aying = name[0]["UserName"]
# #获取时间
# while True:
#     now= datetime.datetime.now()
#     if now.hour == 6 and now.minute == 00:
#         itchat.send('早安',Aying)
#     elif now.hour == 22 and now.minute == 00:
#         itchat.send('晚安',Aying)
#     time.sleep(30)


import autoit
import win32gui
import win32con
import win32clipboard as w
import time


def send(name, msg):
    # 打开剪贴板
    w.OpenClipboard()
    # 清空剪贴板
    w.EmptyClipboard()
    # 设置剪贴板内容
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    # 获取剪贴板内容
    date = w.GetClipboardData()
    # 关闭剪贴板
    w.CloseClipboard()
    # 获取qq窗口句柄
    handle = win32gui.FindWindow(None, name)
    if handle == 0:
        print('未找到窗口！')
    # 显示窗口
    win32gui.ShowWindow(handle, win32con.SW_SHOW)
    # 把剪切板内容粘贴到qq窗口
    win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)
    # 按下后松开回车键，发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    time.sleep(2)  # 延缓进程


def main():
    name = 'bin'
    print('开始')
    for i in range(1, 5):
        #         send(name, '第'+str(i)+'次测试')
        send(name, '你你你')
    print('结束')


main()

