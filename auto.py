import pyautogui as pg
import time
import pyperclip

time.sleep(2)
pg.PAUSE = 1

i = 93
for _ in range(7):
    pg.click(319, 78)
    pg.write('ex0{}.py'.format(i))
    pg.press('enter')
    i += 1
