
import os
import sys
import time
from data import items, civilisations_dict


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
def stats(civilisation_number, agent):

    animate(coloured("Agent Information:", "bold"))
    print(coloured(f"\nLocation: {civilisations_dict[civilisation_number]['civilisation']}", "code"))
    print(coloured(f"City: {civilisations_dict[civilisation_number]['city']}", "code"))
    print(coloured(f"Date: {civilisations_dict[civilisation_number]['date']}", "code"))
    print(coloured(f"Health: {agent['health']}", "code"))
    animate(coloured("\nMission Objective:", "bold"))
    print()
    print(coloured(civilisations_dict[civilisation_number]['mission'], "code"))
    animate(coloured(f"\nItems:", "bold"))
    print()
    for i in agent['inventory']:
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

# Function to display a growing plant animation
def plant():
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

# Function to display the game menu and handle user input
def menu(civilisation_number):

    menu_options = {
        "start": "\nStart New Game: Type 'start' and press enter",
        "instructions": "\nInstructions: Type 'instructions' and press enter",
        "continue": f"\nContinue to Level {civilisation_number} : Type 'continue' and press enter"
    }

    clear_screen
    print(coloured("\n----------------- THE TIMEKEEPER'S MISSION ----------------","bold"))

    print(coloured(menu_options["start"],"code"))
    print(coloured(menu_options["instructions"],"code"))

    if civilisation_number > 1:
        print(coloured(menu_options["continue"],"code"))
        
    input_menu = input(coloured("\nType here: ","bold")).lower().strip()
    return input_menu








