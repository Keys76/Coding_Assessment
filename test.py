
game_map = [
    ["Festive Field", "Freaky Forest", ""],
    ["Fabulous Farm", "Valiant Village", "Radical River"],
    ["Majestic Mountains", "Curble's Campsite", "Tasty Tower"]
]

location_descriptions = {
    "Festive Field": "Where the trees twinkle year-round, the air smells suspiciously like cinnamon, and even the squirrels know how to conga.",
    "Freaky Forest": "Where the trees whisper your secrets, the mushrooms giggle when you step on them, and the raccoons organize weekly séances.",
    "Fabulous Farm": "Where the cows strut like runway models, the corn wears sequins, and every sunrise comes with a disco ball.",
    "Valiant Village": "Where every grandma wields a sword, the chickens patrol in armor, and the town meetings end with epic boss battles.",
    "Radical River": "Where the water surfs itself, the fish wear shades, and even the otters say 'cowabunga' before doing backflips off the rocks.",
    "Majestic Mountains": "Where the cliffs sing opera at dawn, snowflakes sparkle like glitter bombs, and yetis run a five-star hot cocoa spa.",
    "Curble's Campsite": "The only place where you might roast marshmallows, dodge flying raccoons, and accidentally ignite your sleeping bag—all before breakfast.",
    "Tasty Tower": "A dangerously delicious skyscraper where each floor is a new flavor, the elevators run on whipped cream, and one wrong bite could trigger a fondue flood."
}

directions = {
    "N": (-1, 0),  # North → up
    "S": (1, 0),   # South → down
    "E": (0, 1),   # East → right
    "W": (0, -1)   # West → left
}

def show_map(pos):
    for i in range(3):
        row = ""
        for j in range(3):
            if (i, j) == pos:
                row += "[X] "
            elif game_map[i][j]:
                row += "[O] "
            else:
                row += " .  "
        print(row)
    print()

def get_moves(pos):
    moves = []
    for d, (dx, dy) in directions.items(): #d is just the counter
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < 3 and 0 <= y < 3 and game_map[x][y]:
            moves.append(d)
    return moves

def play():
    pos = (0, 0)  # Start at Emond's Field
    print("Your quest is to reach the Tasty Tower!\n")
    while True:
        show_map(pos)
        place = game_map[pos[0]][pos[1]]
        print("You are at:", place)
        print(location_descriptions[place])

        if place == "Tasty Tower":
            print("You reached the Tasty Tower! You win!")
            break

        moves = get_moves(pos)
        print("Available moves:", moves)

        move = input("Move (N/S/E/W): ").upper()
        if move in moves:
            dx, dy = directions[move]
            pos = (pos[0] + dx, pos[1] + dy)
        else:
            print("Invalid move. Try again.\n")
            

play()
