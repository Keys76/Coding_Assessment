import time
from functions import *
from data import *
civilisation_number = 1
health = 100
riddle_answer = 0
riddle_attempts = 0

def main():
    while True:
        input_menu = menu()
        if input_menu == "start":
            clear_screen()
            alive = game_loop()
            if alive == "dead":
                print(coloured("GAME OVER","red"))
                main()
        elif input_menu == "instructions":
            clear_screen()
            print(coloured("--------------- INSTRUCTIONS ---------------","bold"))
            animate(coloured("\nObjective:","bold"))
            print(coloured("\n. Travel through different ancient civilisations to complete missions and restore the timeline.","code"))
            print(coloured(". Solve puzzles, make choices, and overcome challenges to progress.","code"))
            animate(coloured("\nControls:","bold"))
            print(coloured("\n. Input your choices by typing the corresponding number or word and pressing Enter.","code"))
            print(coloured(". Follow on-screen prompts to navigate through the game.","code"))
            animate(coloured("\nGameplay Tips:","bold"))
            print(coloured("\n. Be careful with choices — some paths may end your journey","code"))
            print(coloured(". Completing missions in each civilization repairs the timeline","code"))
            continue_game()
            main()
        else:
            clear_screen()
            main()

def game_loop():
    # Clear the screen before starting the animation
    clear_screen()

    # Wait for a second before clearing the screen
    clear_wait()

    # Display the menu
    menu()

    # Display the introduction message
    introduction()

    # Display the agent stats and mission details
    stats(civilisation_number, health)

    # Prompt the user to continue the game
    continue_game()

    # First Mission - Ancient Greece
    print(coloured("🏛  Ancient Greece 🔱", "bold"))
    print()
    animate(coloured(
        "You look around and see tall stone walls and crowded houses behind them. The streets look quiet, with fewer people than you would expect for a big city. "
        "\nMany shops are closed, and travelers seem nervous. Outside the gates, the Sphinx waits, keeping trade and visitors away.","cyan"
        ))
    print()
    animate(coloured(
        "As you leave the quiet streets and walk toward the gates, the Sphinx comes into view. She sits on a rock by the road, her sharp eyes fixed on you. "
        "\nRising to block the way, she spreads her wings and declares: Answer my riddle, or you shall not pass.","cyan"
    ))
    continue_game()
    print(coloured("🏛  Ancient Greece 🔱", "bold"))
    print()
    animate(coloured(
        "The Sphinx's voice is low and steady: 'What walks on four legs in the morning, two legs at noon, and three legs in the evening?'"
        "\nShe watches you closely, waiting for your answer.","cyan"
    ))
    print(coloured("\nYou have 4 choices, choose wisely as it will determine your fate:", "bold"))
    animate(coloured("\n1: Dog", "cyan"))
    animate(coloured("2: Human", "cyan"))
    animate(coloured("3: Old Tree", "cyan"))
    animate(coloured("4: Bird", "cyan"))
    riddle_answer =int(input(coloured("\nType the number that corresponds to your answer and press enter...", "bold")))

    # Loop to give different outcomes based on the user's answer to the riddle
    while riddle_attempts < 1:
        # Check the user's answer and provide the corresponding outcome
        if riddle_answer == 2:
            clear_wait()
            print(coloured("🏛  Ancient Greece 🔱","bold"))
            animate(coloured("\nThe Sphinx's eyes narrow, then she lets out a piercing cry. With a furious beat of her wings, she leaps from the rock and flies away into the mountains."
            "\nThe people of Thebes are freed at last","cyan"))
            continue_game()
            riddle_attempts = riddle_attempts + 1
        # If the answer is incorrect, provide a different outcome
        elif riddle_answer == 1 or riddle_answer == 3 or riddle_answer == 4:
            clear_wait()
            print(coloured("🏛  Ancient Greece 🔱","bold"))
            animate(coloured("\nThe Sphinx's lips curl into a cruel smile. “Wrong,” she hisses, stepping closer. Her wings spread wide as the ground trembles with her power.","cyan"))
            animate(coloured("The air fills with dread. With a swift motion, she strikes you down. Darkness engulfs you as you fall to the ground...","cyan"))
            riddle_attempts = riddle_attempts + 1
            return "dead"
        # If the input is invalid, prompt the user to enter a valid number
        else:
            animate(coloured("\nInvalid input. Please enter a number between 1 and 4.", "red"))
            clear_wait()
            print(coloured("🏛  Ancient Greece 🔱", "bold"))
            print()
            print(coloured(
                "The Sphinx's voice is low and steady: 'What walks on four legs in the morning, two legs at noon, and three legs in the evening?'"
                "\nShe watches you closely, waiting for your answer.","cyan"
            ))
            print(coloured("\nYou have 4 choices, choose wisely as it will determine your fate:", "bold"))
            print(coloured("\n1: Dog", "cyan"))
            print(coloured("2: Human", "cyan"))
            print(coloured("3: Old Tree", "cyan"))
            print(coloured("4: Bird", "cyan"))
            riddle_answer =int(input(coloured("\nType the number that corresponds to your answer and press enter...", "bold")))

main()









 


