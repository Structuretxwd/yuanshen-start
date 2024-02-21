'''

from pynput import mouse

control = mouse.Controller()

print(control.position)

from ctypes import windll

import win32api

import win32con

import time

import os

width = windll.user32.GetSystemMetrics(0)

height = windll.user32.GetSystemMetrics(1)

print(width, height)

windll.user32.SetCursorPos(900,300)



import os

#os.startfile(r'D:\新建.png')

#os.startfile(r'D:\新建文本文档.txt')

os.startfile('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"')

'''

import pyautogui

import os

import time

os.startfile('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"')
time.sleep(5)
pyautogui.click(1049, 69)

time.sleep(5)

pyautogui.click(172, 50)

pyautogui.keyDown('h')

pyautogui.keyUp('h')

pyautogui.keyDown('t')

pyautogui.keyUp('t')

pyautogui.keyDown('t')

pyautogui.keyUp('t')

pyautogui.keyDown('p')

pyautogui.keyUp('p')

pyautogui.keyDown('s')

pyautogui.keyUp('s')

pyautogui.keyDown(':')

pyautogui.keyUp(':')

pyautogui.keyDown('/')

pyautogui.keyUp('/')

pyautogui.keyDown('/')

pyautogui.keyUp('/')

pyautogui.keyDown('w')

pyautogui.keyUp('w')

pyautogui.keyDown('w')

pyautogui.keyUp('w')

pyautogui.keyDown('w')

pyautogui.keyUp('w')

pyautogui.keyDown('.')

pyautogui.keyUp('.')

pyautogui.keyDown('b')

pyautogui.keyUp('b')

pyautogui.keyDown('i')

pyautogui.keyUp('i')

pyautogui.keyDown('l')

pyautogui.keyUp('l')

pyautogui.keyDown('i')

pyautogui.keyUp('i')

pyautogui.keyDown('b')

pyautogui.keyUp('b')

pyautogui.keyDown('i')

pyautogui.keyUp('i')

pyautogui.keyDown('l')

pyautogui.keyUp('l')

pyautogui.keyDown('i')

pyautogui.keyUp('i')
#bilibili

pyautogui.keyDown('.')

pyautogui.keyUp('.')

pyautogui.keyDown('c')

pyautogui.keyUp('c')

pyautogui.keyDown('o')

pyautogui.keyUp('o')

pyautogui.keyDown('m')

pyautogui.keyUp('m')

pyautogui.keyDown('/')

pyautogui.keyUp('/')

pyautogui.keyDown('v')

pyautogui.keyUp('v')

pyautogui.keyDown('i')

pyautogui.keyUp('i')

pyautogui.keyDown('d')

pyautogui.keyUp('d')

pyautogui.keyDown('e')

pyautogui.keyUp('e')

pyautogui.keyDown('o')

pyautogui.keyUp('o')

pyautogui.keyDown('/')

pyautogui.keyUp('/')

pyautogui.keyDown('B')

pyautogui.keyUp('B')

pyautogui.keyDown('V')

pyautogui.keyUp('V')

pyautogui.keyDown('1')

pyautogui.keyUp('1')

pyautogui.keyDown('q')

pyautogui.keyUp('q')

pyautogui.keyDown('6')

pyautogui.keyUp('6')

pyautogui.keyDown('4')

pyautogui.keyUp('4')

pyautogui.keyDown('y')

pyautogui.keyUp('y')

pyautogui.keyDown('1')

pyautogui.keyUp('1')

pyautogui.keyDown('N')

pyautogui.keyUp('N')

pyautogui.keyDown('7')

pyautogui.keyUp('7')

pyautogui.keyDown('w')

pyautogui.keyUp('w')

pyautogui.keyDown('g')

pyautogui.keyUp('g')


'''
#pyautogui.hotkey('ctrl', 'v')
'''
pyautogui.keyDown('enter')

pyautogui.keyUp('enter')
time.sleep(3)

pyautogui.click(1075,865)
time.sleep(3)

pyautogui.click(1079,777)
time.sleep(5)

os.startfile('D:\yyds\Genshin Impact\launcher.exe')
time.sleep(5)

pyautogui.click(1328, 765)
time.sleep(35)

pyautogui.click(944, 526)