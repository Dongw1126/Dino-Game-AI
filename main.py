from selenium import webdriver
import pyautogui
import time

def Short_Jump():
    start = time.time()
    pyautogui.keyDown('up')
    while True:
        if time.time() - start > 0.0001:
            pyautogui.keyUp('up')
            break;

def Long_Jump():
    start = time.time()
    pyautogui.keyDown('up')
    while True:
        if time.time() - start > 0.1:
            pyautogui.keyUp('up')
            break;
            
def Duck():
    pyautogui.press('down')

def Restart():
    pyautogui.press('enter')


driver = webdriver.Chrome()
driver.get('chrome://dino')

time.sleep(2)
driver.close()
