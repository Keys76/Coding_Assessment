import os
import sys
import time

# Function to clear the console screen
def clear_screen():
    os.system ('cls' if os.name == 'nt' else 'clear')


def animate(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Function to return coloured text for terminal output
def coloured(text, colour='green'):
    colours = {
        'red': '\033[91m',
        'green': '\033[92m',
        'cyan': '\033[96m',
        'magenta': '\033[38;5;125m',
        'blue': '\033[38;5;21m',
        'yellow': '\033[38;5;222m',
        'end': '\033[0m'
    }
    return f"{colours.get(colour, '')}{text}{colours['end']}"

def introduction():
    animate(coloured())