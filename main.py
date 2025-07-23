import keyboard
import pyautogui
import time
import random

check = False

def stop_script():
    global check
    check = False
    print("stopping script")

def running_script():
    global check
    check = True
    print("running script")

def random_delay():
    if random.randint(1,5) == 5:
        return random.uniform(1.27,2.13)
    return random.uniform(0.57,1.29)

def press_key(x):
    pyautogui.keyDown(x)
    time.sleep(random.uniform(0.0523, 0.217))
    pyautogui.keyUp(x)

def press_keys():
    if random.random() < 0.2: #First F then SPACE
        pyautogui.scroll(10)
        if random.random() < 0.93:
            press_key('f')
        time.sleep(random.uniform(0.0484, 0.283))
        if random.random() < 0.94:
            press_key('space')
    else:
        #First SPACE then F
        if random.random() < 0.92:
            press_key('space')
        time.sleep(random.uniform(0.0516, 0.2183))
        pyautogui.scroll(10)
        if random.random() < 0.91:
            press_key('f')

keyboard.add_hotkey("q", stop_script, suppress=True)
keyboard.add_hotkey("r", running_script, suppress=True)

def main():
    global check

    print("The script is running press 'q' to stop and 'r' to resume")

    try:
        while True:
            if check:
                press_keys()
            time.sleep(random_delay())
    except KeyboardInterrupt:
        print("Zatrzymano program")

if __name__ == "__main__":
    main()