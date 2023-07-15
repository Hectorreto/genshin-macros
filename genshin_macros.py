import pyautogui
import keyboard
from time import sleep
from threading import Thread
from pynput import mouse
from helpers import randomBetween, getDistance

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.005
stopClicking = False
cooldown = 0
isKeepingClick = False
ignoreNextClick = False
lastPosition = None

def listenBreakLoop():
    global cooldown, stopClicking
    sleep(0.5) 
    while (key := keyboard.read_key()) not in ['shift', 'mayusculas']:
        print(key)
        cooldown = 5
    stopClicking = True

def on_click(x, y, button, pressed):
    global cooldown, isKeepingClick, ignoreNextClick
    if ignoreNextClick:
        return

    if pressed:
        isKeepingClick = True
    else:
        isKeepingClick = False
        cooldown = 5
mouse.Listener(on_click=on_click).start()

def falseClickIn(position):
    global ignoreNextClick
    ignoreNextClick = True
    pyautogui.leftClick(position)
    ignoreNextClick = False

def autoclick(startPosition):
    global cooldown, isKeepingClick, lastPosition

    if cooldown > 0:
        print('cooldown', cooldown)
        cooldown -= 1
    elif isKeepingClick:
        print('isKeepingClick', isKeepingClick)
        pass
    else:
        position = pyautogui.position()
        falseClickIn(startPosition)

        if getDistance(position, startPosition) < getDistance(position, lastPosition):
            pyautogui.moveTo(lastPosition)
            return
        else:
            pyautogui.moveTo(position)
            lastPosition = position

while True:
    print('waiting')
    keyboard.wait('shift+w+s')

    print('clicking')
    stopClicking = False
    cooldown = 0
    isKeepingClick = False
    position = pyautogui.position()
    lastPosition = position
    Thread(target=listenBreakLoop).start()

    while not stopClicking: 
        autoclick(position)
        randomTime = randomBetween(0.050, 0.150)
        sleep(randomTime)
