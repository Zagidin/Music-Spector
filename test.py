import ctypes
from time import sleep

SCROLL_LOCK = 0x91
NUM_LOCK = 0x90
CAPS_LOCK = 0x14 


def press_key(code):
    ctypes.windll.user32.keybd_event(code, 0, 0, 0)
    ctypes.windll.user32.keybd_event(code, 0, 2, 0)

while True:
    for _ in range(5):
        press_key(SCROLL_LOCK)
        sleep(0.0999)
        press_key(NUM_LOCK)

    for _ in range(3):
        press_key(CAPS_LOCK)
        sleep(0.1)
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(CAPS_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)

    for _ in range(5):
        press_key(SCROLL_LOCK)
        sleep(0.0999)
        press_key(NUM_LOCK)
    
    for _ in range(4):
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)
        sleep(0.0999)
        press_key(CAPS_LOCK)

    for _ in range(5):
        press_key(SCROLL_LOCK)
        sleep(0.0999)
        press_key(NUM_LOCK)

    for _ in range(4):
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)
        sleep(0.0999)
        press_key(CAPS_LOCK)

    for _ in range(5):
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)
    
    for _ in range(3):
        press_key(CAPS_LOCK)
        sleep(0.1)
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(CAPS_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)

    for _ in range(4):
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)

    for _ in range(6):
        press_key(SCROLL_LOCK)
        sleep(0.0999)
        press_key(NUM_LOCK)

    for _ in range(4):
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)

    for _ in range(4):
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)
        sleep(0.0999)
        press_key(CAPS_LOCK)

    for _ in range(4):
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)

    for _ in range(4):
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(CAPS_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)

    for _ in range(5):
        press_key(SCROLL_LOCK)
        sleep(0.0999)
        press_key(NUM_LOCK)

    for _ in range(4):
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)

    for _ in range(3):
        press_key(CAPS_LOCK)
        sleep(0.1)
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(CAPS_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)

    for _ in range(4):
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)
    
    for _ in range(3):
        press_key(CAPS_LOCK)
        sleep(0.1)
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(CAPS_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)
    
    for _ in range(4):
        press_key(NUM_LOCK)
        sleep(0.0999)
        press_key(SCROLL_LOCK)