import time
from functions import *
from data import *
number = 1
health = 100

# Clear the screen before starting the animation
clear_screen()

# Wait for a second before clearing the screen
clear_wait()

# Display the introduction message
introduction()

# Display the agent stats and mission details
stats(number, health)

# Prompt the user to continue the game
continue_game()

animate(coloured("🏛 Ancient Greece 🔱", "bold"))
print()
print(coloured(
    "You look around and see tall stone walls and crowded houses behind them. The streets look quiet, with fewer people than you would expect for a big city. "
    "\nMany shops are closed, and travelers seem nervous. Outside the gates, the Sphinx waits, keeping trade and visitors away.","cyan"
    ))







 


