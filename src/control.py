import pyautogui

def shortJump():
    start = time.time()
    pyautogui.keyDown('up')
    while True:
        if time.time() - start > 0.0001:
            pyautogui.keyUp('space')
            break;

def longJump():
    start = time.time()
    pyautogui.keyDown('up')
    while True:
        if time.time() - start > 0.1:
            pyautogui.keyUp('space')
            break;
            
def Duck():
    pyautogui.press('down')

def Restart():
    pyautogui.press('enter')
