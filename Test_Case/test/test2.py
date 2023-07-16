# -*- encoding:utf-8 -*-
from time import sleep

import autoit
import pyautogui

exe = r"F:\WeChat\WeChat.exe"
# f = os.popen(exe)
# data = f.readlines()
# f.close()
# print(data)

autoit.run(exe)
sleep(3)
# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
pyautogui.click()
print(autoit.__class__)
