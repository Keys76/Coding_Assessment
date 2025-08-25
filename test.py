level = 1

def main():
    level = 2


def this_one():
    print("This one")

def that_one():
    print("That one")

def game_loop(level):

    civilisation_director= {1: this_one, 2: that_one}

    mydict[level]()

game_loop(level)

