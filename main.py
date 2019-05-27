from selenium import webdriver
import pyautogui
import time

def Jump():
    pyautogui.press('up')

def Duck():
    pyautogui.press('down')

def Restart():
    pyautogui.press('enter')

    

driver = webdriver.Chrome()
driver.get('chrome://dino')

time.sleep(2)
driver.close()
