import os
import sys
import time
from data import * 

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
        'code' : '\033[38;5;28m' ,
        'bold' : '\033[1m',
        'end': '\033[0m'
    }
    return f"{colours.get(colour, '')}{text}{colours['end']}"

# Function to display the introduction message
def introduction():
    animate(coloured("Time Beacon 108 activated...", "code"))
    clear_screen()
    animate(coloured("Loading data...", "code"))
    clear_screen()
    animate(coloured("Complete", "code"))
    clear_wait()
    animate(coloured("Message from commander:", "code"))
    print(coloured("Agent 0712, you are our last hope to save the timeline.\nThere is something trapping the entire agency in a time loop.\nYou must track it down, following its path throughout history, and defeat it.\nWe are all counting on you to save us.", "code"))
    time.sleep(10)
    clear_screen()

# Function to display agent stats and mission details
def stats():
    animate(coloured("Agent Information:", "bold"))
    print(coloured(f"\nLocation: {civilisations[0]}", "cyan"))
    print(coloured(f"City: {cities}", "cyan"))
    print(coloured(f"Date: {date}", "cyan"))
    print(coloured(f"Health: {health}", "cyan"))
    animate(coloured(f"\nItems:", "bold"))
    print()
    for i in items:
        print(coloured(i, "cyan"))
    animate(coloured("\nMission Objective:", "bold"))
    print()
    print(coloured(missions[0], "cyan"))


