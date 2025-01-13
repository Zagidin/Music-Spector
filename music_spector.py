import ctypes
from time import sleep
from random import randint

SCROLL_LOCK = 0x91
NUM_LOCK = 0x90
CAPS_LOCK = 0x14 

my_list_key = [SCROLL_LOCK, NUM_LOCK, CAPS_LOCK]

def press_key(code):
    ctypes.windll.user32.keybd_event(code, 0, 0, 0)
    ctypes.windll.user32.keybd_event(code, 0, 2, 0)

print("\033[32mМузыкальный спектор\033[0m")
sleep(0.1)
print("\033[34mZagidin Magamedragimov\033[0m")
sleep(0.1)
print("\033[33mДата создания -> 12.01.2025 год\033[0m")
sleep(0.1)
print("\033[1;31m\t\tЧтобы отановить Ctrl + C\033[0m")

try:
    if input("\033[33mЧтобы начать пропишите -> go: \033[0m") == "go":
        for _ in range(35):
            for _ in range(5):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(3):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.1)
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(5):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])
            
            for _ in range(4):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(5):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(4):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(5):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])
            
            for _ in range(3):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.1)
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(4):
                press_key(my_list_key[randint(0, 2)])
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(6):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(4):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(4):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(4):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(4):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(NUM_LOCK)
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(5):
                press_key(SCROLL_LOCK)
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(4):
                press_key(NUM_LOCK)
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(3):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.1)
                press_key(NUM_LOCK)
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(CAPS_LOCK)
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

            for _ in range(4):
                press_key(NUM_LOCK)
                sleep(0.0999)
                press_key(SCROLL_LOCK)
            
            for _ in range(3):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.1)
                press_key(NUM_LOCK)
                sleep(0.0999)
                press_key(SCROLL_LOCK)
                sleep(0.0999)
                press_key(CAPS_LOCK)
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])
            
            for _ in range(4):
                press_key(my_list_key[randint(0, 2)])
                sleep(0.0999)
                press_key(my_list_key[randint(0, 2)])

except KeyboardInterrupt:
    print("\033[1;31m\t\tПрограмма Завершена\033[0m")