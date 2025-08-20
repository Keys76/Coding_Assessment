import time
from functions import *
from data import *

# Clear the screen before starting the animation
clear_screen()

# Wait for a second before clearing the screen
print(coloured("                       ","back"))

print(coloured("        ","back"),coloured("     ","black_back"),coloured("       ","back"))
print(coloured("   ","back"),coloured("   ","black_back"),coloured("     ","testicles"),coloured("   ","black_back"),coloured("  ","back"))

print(coloured(" ","back"),coloured(" ","black_back"),coloured("               ","testicles"),coloured(" ","black_back"),coloured(" ","back"))
print(coloured(" ","back"),coloured(" ","black_back"),coloured("               ","testicles"),coloured(" ","black_back"),coloured(" ","back"))
print(coloured(" ","back"),coloured(" ","black_back"),coloured("               ","testicles"),coloured(" ","black_back"),coloured(" ","back"))
print(coloured(" ","back"),coloured(" ","black_back"),coloured("               ","testicles"),coloured(" ","black_back"),coloured(" ","back"))

print(coloured("  ","back"),coloured("  ","black_back"),coloured("         ","testicles"),coloured(" ","black_back"),coloured("  ","back"))
print(coloured("  ","back"),coloured("  ","black_back"),coloured("         ","testicles"),coloured(" ","black_back"),coloured("  ","back"))

print(coloured("     ","back"),coloured(" ","black_back"),coloured("     ","testicles"),coloured(" ","black_back"),coloured("    ","back"))
print(coloured("      ","back"),coloured(" ","black_back"),coloured("   ","testicles"),coloured(" ","black_back"),coloured("     ","back"))
print(coloured("         ","back"),coloured("   ","black_back"),coloured("        ","back"))

print(coloured("                       ","back"))

time.sleep(10000)
# Display the introduction message
introduction()

# Display the agent stats and mission details
stats()







