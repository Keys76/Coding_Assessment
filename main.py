import time
from functions import *
from data import *
number = 1
health = 100

# Clear the screen before starting the animation
clear_screen()

# Wait for a second before clearing the screen
clear_wait()

plant2()
time.sleep(1000000)

# Display the introduction message
introduction()

# Display the agent stats and mission details
stats(number, health)

# Prompt the user to continue the game
continue_game()

print(coloured("🏛  Ancient Greece 🔱", "bold"))
print()
animate(coloured(
    "You look around and see tall stone walls and crowded houses behind them. The streets look quiet, with fewer people than you would expect for a big city. "
    "\nMany shops are closed, and travelers seem nervous. Outside the gates, the Sphinx waits, keeping trade and visitors away.","cyan"
    ))
print()
animate(coloured(
    "As you leave the quiet streets and walk toward the gates, the Sphinx comes into view. She sits on a rock by the road, her sharp eyes fixed on you. "
    "\nRising to block the way, she spreads her wings and declares: Answer my riddle, or you shall not pass.","cyan"
))
continue_game()
print(coloured("🏛  Ancient Greece 🔱", "bold"))
print()
animate(coloured(
    "The Sphinx's voice is low and steady: 'What walks on four legs in the morning, two legs at noon, and three legs in the evening?'"
    "\nShe watches you closely, waiting for your answer.","cyan"
))










 


