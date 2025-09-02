import keyboard
import pyautogui
import time
import random
import threading
import os
import signal
import tkinter as tk

import pystray
from PIL import Image, ImageDraw

check = False
running = True


#Icon for tray
def create_image():
    img = Image.new("RGB", (64, 64), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    d.ellipse((16, 16, 48, 48), fill=(0, 0, 0))
    return img

#Function for popup notification
def popup_message(text):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)

    width, height = 300, 50
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    y, x = 10, screen_width

    root.geometry(f"{width}x{height}+{x}+{y}")

    label = tk.Label(root, text=text, bg="black", fg="white", font=("Arial", 12))
    label.pack(fill="both", expand=True)

    for pos in range(x, screen_width - width - 10, -10):
        root.geometry(f"{width}x{height}+{pos}+{y}")
        root.update()
        time.sleep(0.01)

    time.sleep(2)

    for pos in range(screen_width - width - 10, screen_width + 1, 10):
        root.geometry(f"{width}x{height}+{pos}+{y}")
        root.update()
        time.sleep(0.01)

    root.destroy()

def on_exit(icon, item):
    global running
    running = False
    icon.stop()

def stop_script():
    global check
    check = False
    print("stopping script")
    threading.Thread(target=popup_message, args=("⛔ Skrypt zatrzymany",), daemon=True).start()

def running_script():
    global check
    check = True
    print("running script")
    threading.Thread(target=popup_message, args=("▶️ Skrypt uruchomiony",), daemon=True).start()

def exit_script():
    global running
    running = False
    os.kill(os.getpid(), signal.SIGTERM)

keyboard.add_hotkey("-", stop_script, suppress=True)
keyboard.add_hotkey("+", running_script, suppress=True)
keyboard.add_hotkey("esc", exit_script, suppress=True)

def random_delay():
    if random.randint(1,5) == 5:
        return random.uniform(1.27,2.13)
    return random.uniform(0.57,1.29)

def press_key(x):
    pyautogui.keyDown(x)
    time.sleep(random.uniform(0.0523, 0.217))
    pyautogui.keyUp(x)

def press_keys():
    if random.random() < 0.2:
        #First F then SPACE
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

def worker():
    global running
    print("The script is running. Use '-' to stop, '+' to resume, ESC to quit.")
    try:
        while running:
            if check:
                press_keys()
            time.sleep(random_delay())
    except KeyboardInterrupt:
        print("Zatrzymano program")

def main():
    threading.Thread(target=worker, daemon=True).start()

    icon = pystray.Icon("GenSkipDial")
    icon.icon = create_image()
    icon.title = "GenSkipDial"
    icon.menu = pystray.Menu(
        pystray.MenuItem("Exit", on_exit)
    )
    icon.run()

if __name__ == "__main__":
    main()
