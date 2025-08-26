from functions import *
from data import *

# Lists
weapons = ["Mace", "Rifle", "Sword"]
special_attacks = ["Slash", "Stab", "Throw"]

# Health values
player_health = 100
enemy_health = 90
new_weapon = None

enemy = "shadowy creature"
enemy_damage = 15  

# Weapon damage dictionary
weapon_damage_values = {
    "Mace": 35,
    "Rifle": 15,
    "Sword": 25
}

# Show starting options
print("\nIn front of you appears", len(weapons), "weapons:", weapons)
print("\nYou have", len(special_attacks), "attack options:", special_attacks)

# Weapon management
print(coloured("\n Weapon Management ", "bold"))
print("\n1. Add a new weapon")
print("2. Remove a weapon")
print("3. Continue to battle")

weapon_choice = input("\nChoose an option (1, 2, or 3): ")

if weapon_choice == "1":
    new_weapon = input("Enter the name of the weapon to add: ")
    weapons.append(new_weapon)
    print(new_weapon, "has been added to your arsenal.")
elif weapon_choice == "2":
    print("Current Weapons:", weapons)
    weapon_to_remove = input("Enter the name of the weapon to remove: ")
    if weapon_to_remove in weapons:
        weapons.remove(weapon_to_remove)
        print(weapon_to_remove, "has been removed.")
    else:
        print("That weapon is not in your list.")
elif weapon_choice == "3":
    print("\nContinuing to battle...")

# Updated weapon list
print("\nYou have", len(weapons), "weapons:", weapons)

print("\nYour health:", player_health)
print("Enemy health:", enemy_health)
print()


while player_health > 0 and enemy_health > 0:
    weapon = input("Choose your weapon: ")
    attack = input("Choose your special attack: ")

    # Work out weapon damage
    if weapon in weapon_damage_values:
        damage = weapon_damage_values[weapon]
    elif new_weapon is not None and weapon == new_weapon:
        damage = 20
    else:
        print("Invalid weapon! You miss your turn.")
        continue

    # Deal damage to enemy
    enemy_health = enemy_health - damage
    print("You attack with", weapon, "and deal", damage, "damage.")
    print("Enemy health:", enemy_health)

    if enemy_health <= 0:
        break

    # Enemy’s turn
    print("Enemy's turn")
    player_health = player_health - enemy_damage
    print(enemy, "attacks you for:", enemy_damage, "damage!")
    print("Your health:", player_health)

if player_health > 0:
    print("\nYou win the battle against the", enemy + "!")
else:
    print("\nYou have been defeated by the", enemy + ".")
