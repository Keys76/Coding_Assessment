
civilisations_dict = {
    1: {"civilisation": "Ancient Greece", "city": "Thebes", "date": "429 BCE", "mission": "Find the sphinx who is reigning terror over the city of Thebes, you must answer its riddle to pass."},
    2: {"civilisation": "Ancient China", "city": "Yangtze River Basin", "date": "3001 BCE", "mission": "Trade with villagers to get seeds and water to grow a rice plant so you can replenish you supplies."},
    3: {"civilisation": "Ancient Rome", "city": "Rome", "date": "352 CE", "mission": "mission 3"},
    4: {"civilisation": "Final Battle", "city": "Time Void", "date": "-", "mission": "mision 4"},
} 

# List of items available in the game
items = [
    "Time Beacon 108",
    "Bottle of Water",
    "First Aid Kit",
    "Flashlight",
    "Map",
    "One set of rations"
]

game_map = [
    ["Basillica", "Roman Forum", "Pantheon"],
    ["Trevi Fountain", "Sistine Chapel", "Catacombs"],
    ["Paletine Hill", "Circus Maximus", "Colosseum"]
]

directions = {
    "N": (-1, 0),  # North → up
    "S": (1, 0),   # South → down
    "E": (0, 1),   # East → right
    "W": (0, -1)   # West → left
}
