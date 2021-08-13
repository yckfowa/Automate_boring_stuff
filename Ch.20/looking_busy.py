import pyautogui
import time

print("Lets look busy! ")

try:
    while True:
        pyautogui.moveRel(10, 0, duration=0.5)
        time.sleep(600)
        pyautogui.moveRel(-10, 0, duration=0.5)
except KeyboardInterrupt:
    print("Time to go home")

