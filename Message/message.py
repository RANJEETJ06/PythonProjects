import pyautogui
import time
time.sleep(5)
for _ in range(10):
    pyautogui.typewrite("Hello World")
    pyautogui.press("enter")