import pyautogui
import keyboard
import time
import threading

def spawn_click():
    while not exit:
        if active:
            pyautogui.click()
        time.sleep(0.1)

def move_to_button():
    while not exit:
        if active:
            button_location = pyautogui.locateCenterOnScreen('button.png', confidence=0.8)
            if button_location:
                pyautogui.moveTo(button_location)
        time.sleep(0.1)

active = False
exit = False
threading.Thread(target=spawn_click).start()
threading.Thread(target=move_to_button).start()
print("Program started")

try:
    while True:
        keyboard.wait("shift+w+s")
        active = True
        print("Active: True")

        keyboard.wait("shift")
        active = False
        print("Active: False")

except KeyboardInterrupt:
    print('Exiting')

finally:
    exit = True
