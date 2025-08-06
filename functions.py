import os
import sys
import time

def clear_screen():
    os.system ('cls' if os.name == 'nt' else 'clear')

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def coloured(text, colour='green'):
    colours = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'cyan': '\033[96m',
        'end': '\033[0m'
    }
    return f"{colours.get(colour, '')}{text}{colours['end']}"

