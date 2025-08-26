
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
    for d, (dx, dy) in directions.items(): 
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < 3 and 0 <= y < 3 and game_map[x][y]:
            moves.append(d)
    return moves

def play():
    pos = (0, 0) 
    while True:
        show_map(pos)
        place = game_map[pos[0]][pos[1]]
        print("You are at:", place)

        if place == "Colesseum":
            print("You reached the Colesseum")
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
