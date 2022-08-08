import pyautogui as pg
import time

print("program will rn in 5 sec")
time.sleep(5)

for i in range(100):
    pg.write("Check your account...")
    time.sleep(0.5)
    pg.press("Enter")