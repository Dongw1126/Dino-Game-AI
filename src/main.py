import pyautogui
import time

def shortJump():
    start = time.time()
    pyautogui.keyDown('up')
    while True:
        if time.time() - start > 0.0001:
            pyautogui.keyUp('up')
            break;

def longJump():
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
