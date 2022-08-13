
with open('info.txt','r') as f:
    info=f.read().split('\n\n')

dict={}
while info:dict[info.pop()]=info.pop()

import pyautogui
import time
time.sleep(3)

pyautogui.PAUSE=0

text="YOUR TEXT in any case"

text=text.replace('\n','  ').replace(' ','|').upper()

for character in text:
    commands=dict[character].split('\n')
    for line_of_commands in commands:
        for command in line_of_commands:
            if command=='1':
                pyautogui.typewrite('1')
            # press "right"
            pyautogui.press('right')
        # press down, left *7
        pyautogui.press('down')
        for _ in range(7): pyautogui.press('left')
    # press up *7, right *8
    for _ in range(7): pyautogui.press('up')
    for _ in range(8): pyautogui.press('right')

