import pyautogui
import keyboard
from random import random, choice
from time import sleep
from math import sqrt
from threading import Thread
from pynput import mouse

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.001
exit = False
wait = 0
stop = False
frame = 0
ignoreNextClick = False
lastPosition = None

def waitExit():
    global wait, exit
    sleep(0.5) 
    while (key := keyboard.read_key()) not in ['shift', 'mayusculas']:
        print(key)
        wait = 5
    exit = True

def on_click(x, y, button, pressed):
    global wait, stop, ignoreNextClick
    if ignoreNextClick:
        return

    if pressed:
        stop = True
    else:
        stop = False
        wait = 5
mouse.Listener(on_click=on_click).start()

def getDistance(a, b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def falseClickIn(position):
    global ignoreNextClick
    ignoreNextClick = True
    pyautogui.leftClick(position)
    ignoreNextClick = False

def autoclick(startPosition):
    global wait, stop, frame, lastPosition

    if wait > 0:
        print(1, wait)
        wait -= 1
    elif stop:
        print(2, stop)
        pass
    else:
        position = pyautogui.position()
        falseClickIn(startPosition)

        if frame % 2 == 0:
            key = choice(['f', 'space'])
            print(key)
            keyboard.send(key) 

        if getDistance(position, startPosition) < getDistance(position, lastPosition):
            pyautogui.moveTo(lastPosition)
            return
        else:
            pyautogui.moveTo(position)
            lastPosition = position

    frame += 1

def randomBetween(min, max):
    return random() * (max - min) + min

while True:
    print('waiting')
    keyboard.wait('shift+w+s')

    print('clicking')
    exit = False
    wait = 0
    stop = False
    position = pyautogui.position()
    lastPosition = position
    Thread(target=waitExit).start()

    while not exit: 
        autoclick(position)
        randomTime = randomBetween(0.050, 0.150)
        sleep(randomTime)