import pyautogui
import keyboard
from time import sleep
from threading import Thread
from pynput import mouse
from helpers import random_between, get_distance

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.001
stop_clicking = False
cooldown = 0
is_keeping_click = False
ignore_next_click = False
last_position = None

def listen_break_loop():
    global cooldown, stop_clicking
    sleep(0.5) 
    while (key := keyboard.read_key()) not in ['shift', 'mayusculas']:
        print(key)
        cooldown = 5
    stop_clicking = True

def on_click(x, y, button, pressed):
    global cooldown, is_keeping_click, ignore_next_click
    if ignore_next_click:
        return

    if pressed:
        is_keeping_click = True
    else:
        is_keeping_click = False
        cooldown = 5
mouse.Listener(on_click=on_click).start()

def false_click_in(position):
    global ignore_next_click
    ignore_next_click = True
    pyautogui.leftClick(position)
    ignore_next_click = False

def update_start_position():
    global start_position, stop_clicking
    while not stop_clicking:
        image_location = pyautogui.locateCenterOnScreen('button.png', confidence=0.8)
        if image_location:
            print("Button found at:", image_location)
            start_position = image_location
        sleep(0.5)

def autoclick():
    global cooldown, is_keeping_click, last_position, start_position

    if cooldown > 0:
        print('cooldown:', cooldown)
        cooldown -= 1
    elif is_keeping_click:
        print('is keeping click:', is_keeping_click)
        pass
    else:
        position = pyautogui.position()
        false_click_in(start_position)

        if get_distance(position, start_position) < get_distance(position, last_position):
            pyautogui.moveTo(last_position)
            return
        else:
            pyautogui.moveTo(position)
            last_position = position

while True:
    print('waiting')
    keyboard.wait('shift+w+s')

    print('clicking')
    stop_clicking = False
    cooldown = 0
    is_keeping_click = False
    start_position = pyautogui.position()
    last_position = start_position
    Thread(target=listen_break_loop).start()
    Thread(target=update_start_position).start()

    while not stop_clicking: 
        autoclick()
        random_time = random_between(0.050, 0.150)
        sleep(random_time)
