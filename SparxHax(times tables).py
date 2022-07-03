from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#4 seconds before start to get ready
time.sleep(4)

#repeats the process using a while loop
while 1:
    if pyautogui.locateOnScreen('4x3.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('1')
        time.sleep(0.1)
        pyautogui.press('2')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('5x8.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('4')
        time.sleep(0.1)
        pyautogui.press('0')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('4x5.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('2')
        time.sleep(0.1)
        pyautogui.press('0')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('7x4.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('2')
        time.sleep(0.1)
        pyautogui.press('8')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('3x8.png', grayscale=True, region=(520,200,480,110)) or pyautogui.locateOnScreen('8x3.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('2')
        time.sleep(0.1)
        pyautogui.press('4')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('6x4.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('2')
        time.sleep(0.1)
        pyautogui.press('4')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('8x4.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('3')
        time.sleep(0.1)
        pyautogui.press('2')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('6x9.png', grayscale=True, region=(520,200,480,110)) or pyautogui.locateOnScreen('9x6.png', grayscale=True, region=(520,200,480,110))!= None:
        pyautogui.press('5')
        time.sleep(0.1)
        pyautogui.press('4')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('7x8.png', grayscale=True, region=(520,200,480,110)) or pyautogui.locateOnScreen('8x7.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('5')
        time.sleep(0.1)
        pyautogui.press('6')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('49-7.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('7')
        time.sleep(0.1)
        pyautogui.press('enter')
    elif pyautogui.locateOnScreen('8x6.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('4')
        time.sleep(0.1)
        pyautogui.press('8')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('12x3.png', grayscale=True, region=(520,200,480,110)) or pyautogui.locateOnScreen('9x4.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('3')
        time.sleep(0.1)
        pyautogui.press('6')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('4x12.png', grayscale=True, region=(520,200,480,110)) or pyautogui.locateOnScreen('6x8.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('4')
        time.sleep(0.1)
        pyautogui.press('8')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    elif pyautogui.locateOnScreen('5x12.png', grayscale=True, region=(520,200,480,110)) != None:
        pyautogui.press('6')
        time.sleep(0.1)
        pyautogui.press('0')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
    else:
        print("Undefined")
        time.sleep(1)
