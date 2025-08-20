import time
from functions import *
from data import *

# Clear the screen before starting the animation
clear_screen()

# Wait for a second before clearing the screen
print(coloured("                         ","back"))

print(coloured("         ","back"),coloured("     ","black_back"),coloured("         ","back"))
print(coloured("    ","back"),coloured("   ","black_back"),coloured("       ","t"),coloured("   ","black_back"),coloured("    ","back"))

print(coloured("  ","back"),coloured(" ","black_back"),coloured("               ","t"),coloured(" ","black_back"),coloured("  ","back"))
print(coloured("  ","back"),coloured(" ","black_back"),coloured("               ","t"),coloured(" ","black_back"),coloured("  ","back"))
print(coloured("  ","back"),coloured(" ","black_back"),coloured("               ","t"),coloured(" ","black_back"),coloured("  ","back"))
print(coloured("  ","back"),coloured(" ","black_back"),coloured("               ","t"),coloured(" ","black_back"),coloured("  ","back"))

print(coloured("    ","back"),coloured(" ","black_back"),coloured("           ","t"),coloured(" ","black_back"),coloured("    ","back"))
print(coloured("    ","back"),coloured(" ","black_back"),coloured("           ","t"),coloured(" ","black_back"),coloured("    ","back"))

print(coloured("      ","back"),coloured(" ","black_back"),coloured(" ","shadow"),coloured("      ","t"),coloured(" ","black_back"),coloured("     ","back"))
print(coloured("       ","back"),coloured(" ","black_back"),coloured("     ","shadow"),coloured(" ","black_back"),coloured("       ","back"))

print(coloured("          ","back"),coloured("   ","black_back"),coloured("          ","back"))
print(coloured("                         ","back"))

time.sleep(10000000)
clear_wait()
        
# Display the introduction message
introduction()

number = 1

# Display the agent stats and mission details
stats()







