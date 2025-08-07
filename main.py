import time
from functions import clear_screen, animate, coloured, clear_wait, introduction 
from data import cities, city, date, health, items

# Clear the screen before starting the animation
clear_screen()

# Animate the cities with different colours
#animate(coloured(cities[0], "cyan"))
#animate(coloured(cities[1], "green"))
#animate(coloured(cities[2], "magenta"))
#animate(coloured(cities[3], "blue"))
#animate(coloured(cities[4], "yellow"))
#animate(coloured(cities[5], "red"))

# Wait for a second before clearing the screen
clear_wait()

# Display the introduction message
introduction()

animate(coloured("Agent Information:", "code"))
print(coloured(f"\nLocation: {cities[0]}", "cyan"))
print(coloured(f"City: {city}", "cyan"))
print(coloured(f"Date: {date}", "cyan"))
print(coloured(f"Health: {health}", "cyan"))
print(coloured("\nItems:", "code"))

