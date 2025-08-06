import time
from functions import clear_screen, animate, coloured, clear_wait 
from data import cities

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

# Display a message indicating the activation of the Time Beacon
animate(coloured("Time Beacon 505 activated...", "code"))
clear_screen()
animate(coloured("Loading data...", "code"))
clear_screen()
animate(coloured("Complete", "code"))

clear_wait()

animate(coloured("Message from commander:", "code"))
print(coloured("Agent 0712, you are our last hope to save the timeline. There is something trapping the entire agency in a time loop. You must track it down, following its path throughout time, and defeat it.We are all counting on you to save us.", "code"))

