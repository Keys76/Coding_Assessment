
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
        'end': '\033[0m',
        'back': '\033[48;5;224m',
        't': '\033[48;5;21m',
        'black_back': '\033[48;5;0m',
        'grey_back': '\033[48;5;245m',
        'white_back': '\033[48;5;231m',
        'plant': '\033[48;5;22m',
        'sky' : '\033[48;5;45m'
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
    animate(coloured("Message from commander:", "bold"))
    print(coloured("\nAgent 0712, you are our last hope to save the timeline.\nThere is something trapping the entire agency in a time loop.\nYou must track it down, following its path throughout history, and defeat it.\nWe are all counting on you to save us.", "code"))
    continue_game()

# Function to display agent stats and mission details based on the current number
def stats(number, health):

    if number == 1:
        animate(coloured("Agent Information:", "bold"))
        print(coloured(f"\nLocation: {civilisations[0]}", "code"))
        print(coloured(f"City: {cities[0]}", "code"))
        print(coloured(f"Date: {date[0]}", "code"))
        print(coloured(f"Health: {health}", "code"))
        animate(coloured("\nMission Objective:", "bold"))
        print()
        print(coloured(missions[0], "code"))
    elif number == 2:
        animate(coloured("Agent Information:", "bold"))
        print(coloured(f"\nLocation: {civilisations[1]}", "code"))
        print(coloured(f"City: {cities[1]}", "code"))
        print(coloured(f"Date: {date[1]}", "code"))
        print(coloured(f"Health: {health}", "code"))
        animate(coloured("\nMission Objective:", "bold"))
        print()
        print(coloured(missions[1], "code"))  
    elif number == 3:
        animate(coloured("Agent Information:", "bold"))
        print(coloured(f"\nLocation: {civilisations[2]}", "code"))
        print(coloured(f"City: {cities[2]}", "code"))
        print(coloured(f"Date: {date[2]}", "code"))
        print(coloured(f"Health: {health}", "code"))
        animate(coloured("\nMission Objective:", "bold"))
        print()
        print(coloured(missions[2], "code"))
    elif number ==4:
        animate(coloured("Agent Information:", "bold"))
        print(coloured(f"\nLocation: {civilisations[3]}", "code"))
        print(coloured(f"City: {cities[3]}", "code"))
        print(coloured(f"Date: {date[3]}", "code"))
        print(coloured(f"Health: {health}", "code"))
        animate(coloured("\nMission Objective:", "bold"))
        print()
        print(coloured(missions[3], "code"))
    elif number == 5:
        animate(coloured("Agent Information:", "bold"))
        print(coloured(f"\nLocation: {civilisations[4]}", "code"))
        print(coloured(f"City: {cities[4]}", "code"))
        print(coloured(f"Date: {date[4]}", "code"))
        print(coloured(f"Health: {health}", "code"))
        animate(coloured("\nMission Objective:", "bold"))
        print()
        print(coloured(missions[4], "code"))
    elif number == 6:
        animate(coloured("Agent Information:", "bold"))
        print(coloured(f"\nLocation: {civilisations[5]}", "code"))
        print(coloured(f"City: {cities[5]}", "code"))
        print(coloured(f"Date: {date[5]}", "code"))
        print(coloured(f"Health: {health}", "code"))
        animate(coloured("\nMission Objective:", "bold"))
        print()
        print(coloured(missions[5], "code"))
    animate(coloured(f"\nItems:", "bold"))
    print()
    for i in items:
        print(coloured(i, "code"))

# Function to display a shield graphic
def shield():
    print(coloured("                         ","back"))

    print(coloured("         ","back"),coloured("     ","black_back"),coloured("         ","back"))
    print(coloured("    ","back"),coloured("   ","black_back"),coloured("       ","t"),coloured("   ","black_back"),coloured("    ","back"))

    print(coloured("  ","back"),coloured(" ","black_back"),coloured("               ","t"),coloured(" ","black_back"),coloured("  ","back"))
    print(coloured("  ","back"),coloured(" ","black_back"),coloured("               ","t"),coloured(" ","black_back"),coloured("  ","back"))
    print(coloured("  ","back"),coloured(" ","black_back"),coloured("               ","t"),coloured(" ","black_back"),coloured("  ","back"))
    print(coloured("  ","back"),coloured(" ","black_back"),coloured("               ","t"),coloured(" ","black_back"),coloured("  ","back"))

    print(coloured("    ","back"),coloured(" ","black_back"),coloured("           ","t"),coloured(" ","black_back"),coloured("    ","back"))
    print(coloured("    ","back"),coloured(" ","black_back"),coloured("           ","t"),coloured(" ","black_back"),coloured("    ","back"))

    print(coloured("      ","back"),coloured(" ","black_back"),coloured("       ","t"),coloured(" ","black_back"),coloured("      ","back"))
    print(coloured("       ","back"),coloured(" ","black_back"),coloured("     ","t"),coloured(" ","black_back"),coloured("       ","back"))

    print(coloured("          ","back"),coloured("   ","black_back"),coloured("          ","back"))
    print(coloured("                         ","back"))

# Function to prompt the user to continue the game
def continue_game():
    animate(coloured("\nPress Enter to continue...", "bold"))
    input()  # Wait for user input to continue
    clear_screen()

def plant():
    print()
    print()
    print(coloured("   ","t"))
    clear_wait()
    print()
    print(coloured("   ","t"))
    print(coloured("   ","t"))
    clear_wait()
    print(coloured("   ","t"))
    print(coloured("   ","t"))
    print(coloured("   ","t"))

def plant2():
    for i in range(16):
        print(coloured("                 ","sky"))
    print(coloured("  ","sky"),coloured(" ","plant"),coloured("            ","sky"))
    clear_wait()
    for i in range(15):
        print(coloured("                 ","sky"))
    print(coloured("  ","sky"),coloured(" ","plant"),coloured("            ","sky"))
    print(coloured("  ","sky"),coloured(" ","plant"),coloured("            ","sky"))
    clear_wait()
    for i in range(14):
        print(coloured("                 ","sky"))
    print(coloured("  ","sky"),coloured("    ","plant"),coloured("         ","sky"))
    print(coloured("  ","sky"),coloured(" ","plant"),coloured("            ","sky"))
    print(coloured("  ","sky"),coloured(" ","plant"),coloured("            ","sky"))
    clear_wait()
    for i in range(13):
        print(coloured("                 ","sky"))
    print(coloured(" ","sky"),coloured("      ","plant"),coloured("        ","sky"))
    print(coloured("  ","sky"),coloured("    ","plant"),coloured("         ","sky"))
    print(coloured("  ","sky"),coloured(" ","plant"),coloured("            ","sky"))
    print(coloured("  ","sky"),coloured(" ","plant"),coloured("            ","sky"))
    

