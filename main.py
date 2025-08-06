import time
from functions import clear_screen, animate, coloured 
from data import cities

# Clear the screen before starting the animation
clear_screen()

# Animate the cities with different colours
animate(coloured(cities[0], "cyan"))
animate(coloured(cities[1], "green"))
animate(coloured(cities[2], "magenta"))
animate(coloured(cities[3], "blue"))
animate(coloured(cities[4], "yellow"))
animate(coloured(cities[5], "red"))

# Wait for a second before clearing the screen
time.sleep(1)
clear_screen()