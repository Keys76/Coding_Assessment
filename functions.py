import os
import sys
import time

# Function to clear the console screen
def clear_screen():
    os.system ('cls' if os.name == 'nt' else 'clear')

# Function to wait for a second and then clear the screen
def clear_wait():
    time.sleep(1)
    clear_screen()

# Function to animate text output with a delay
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
        'code' : '\033[38;5;46m' ,
        'end': '\033[0m'
    }
    return f"{colours.get(colour, '')}{text}{colours['end']}"

# Function to display the introduction message
def introduction():
    animate(coloured("Time Beacon 505 activated...", "code"))
    clear_screen()
    animate(coloured("Loading data...", "code"))
    clear_screen()
    animate(coloured("Complete", "code"))
    clear_wait()
    animate(coloured("Message from commander:", "code"))
    print(coloured("Agent 0712, you are our last hope to save the timeline. There is something trapping the entire agency in a time loop. You must track it down, following its path throughout time, and defeat it.We are all counting on you to save us.", "code"))

