#pip install pyautogui
#this package need to be installed

import pyautogui
import webbrowser as w
import time

w.open("web.whatsappp.com")
time.sleep(50)

for i in range(5):
 pyautogui.press("hi")
 pyautogui.press("enter")
