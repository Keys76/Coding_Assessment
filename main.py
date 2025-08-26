import time
from functions import clear_screen, clear_wait, coloured, animate, continue_game, shield, plant, stats, introduction, menu
from data import civilisations_dict, items

def main():
    civilisation_number = 1
    agent = {}
    while True:
        clear_screen()
        input_menu = menu(civilisation_number)
        if input_menu == "start" or input_menu == "continue":
            if input_menu == "start":
                civilisation_number = 1
                agent = {
                    "health": 100,
                    "inventory": items.copy(),
                    "coins": 50
                }
            clear_screen()
            alive, agent = game_loop(civilisation_number, agent)
            if alive == "dead":
                clear_screen()
                print(coloured("\nGAME OVER","red"))
                agent = {}
                civilisation_number = 1
                time.sleep(1)
                continue
            else:
                civilisation_number = civilisation_number + 1
                if civilisation_number > 6:
                    clear_screen()
                    print(coloured("Message from commander...","bold"))
                    print(coloured("Congratulations Agent 0712, you have successfully completed all missions and restored the timeline.","code"))
                    break
                else:
                    animate(coloured(f"Congratulations you have completed the mission in {civilisations_dict[civilisation_number-1]['civilisation']}","code"))
                    clear_wait()
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
            menu(civilisation_number)
        else:
            clear_screen()
            menu(civilisation_number)

def game_loop(civilisation_number, agent):

    if civilisation_number == 1:

        riddle_attempts = 0
        time.sleep(2)

        # Clear the screen before starting the animation
        clear_screen()

        # Wait for a second before clearing the screen
        clear_wait()

        # Display the introduction message
        introduction()

        # Display the agent stats and mission details
        stats(civilisation_number, agent)

        # Prompt the user to continue the game
        continue_game()

        # First Mission - Ancient Greece
        print(coloured("🏛  Ancient Greece 🔱", "bold"))
        print()
        print(coloured(
            "You look around and see tall stone walls and crowded houses behind them. The streets look quiet, with fewer people than you would expect for a big city. "
            "\nMany shops are closed, and travelers seem nervous. Outside the gates, the Sphinx waits, keeping trade and visitors away.","cyan"
            ))
        print()
        print(coloured(
            "As you leave the quiet streets and walk toward the gates, the Sphinx comes into view. She sits on a rock by the road, her sharp eyes fixed on you. "
            "\nRising to block the way, she spreads her wings and declares: Answer my riddle, or you shall not pass.","cyan"
        ))
        continue_game()
        print(coloured("🏛  Ancient Greece 🔱", "bold"))
        print()
        print(coloured(
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
                return "win", agent
            # If the answer is incorrect, provide a different outcome
            elif riddle_answer == 1 or riddle_answer == 3 or riddle_answer == 4:
                clear_wait()
                print(coloured("🏛  Ancient Greece 🔱","bold"))
                animate(coloured("\nThe Sphinx's lips curl into a cruel smile. “Wrong,” she hisses, stepping closer. Her wings spread wide as the ground trembles with her power.","cyan"))
                animate(coloured("The air fills with dread. With a swift motion, she strikes you down. Darkness engulfs you as you fall to the ground...","cyan"))
                riddle_attempts = riddle_attempts + 1
                return "dead", agent
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

    elif civilisation_number == 2:

        food_question = 0
        trade_counter = 0
        animate(coloured("ALERT","red"))
        animate(coloured("\nAgent energy depleted: consume food","bold"))

        while food_question == 0: 
            food = input(coloured("\nDo you want to eat your rations?: y/n... ","bold"))
            if food == "y":
                clear_screen()
                animate(coloured("\nYou energy levels are replenished","bold"))
                agent["inventory"].remove("One set of rations")
                food_question = 1
            elif food == "n":
                print(coloured("You died of hunger","red"))
                continue_game
                food_question = food_question + 1
                return "dead", agent
            else:
                animate(coloured("\nInvalid input","red"))
        
        clear_screen()
        stats(civilisation_number, agent)
        continue_game()
        print(coloured("⛩️ Ancient China 🐉","bold"))
        print(coloured(
            "\nNow that you do not have any food in your inventory you will need to trade your coins with villagers here in the Yangtze River basin of "
            "\nAncient China for seeds to grow your own food.","green"
            ))
        print(coloured(
            "\nThere are five villagers willing to trade seeds with you." 
            "\nThey will each present their offer one by one and you can choose wether or not to accept it."
            "\nHowever if you choose to continue to the next offer, you will not be able to go back."
        ))
        continue_game()
        print(coloured("⛩️ Ancient China 🐉","bold"))

        # Villager 1
        while trade_counter == 0:
            print(coloured("\nVillager: Aapti","green"))
            print(coloured("Offer: 10 seeds","green"))
            print(coloured("Cost: 30 coins","green"))
            seed_trade = input("\nDo you want to accept this offer?(y/n)...")
            if seed_trade == "y":
                agent["coins"] = agent["coins"] - 30
                clear_wait()
                print(coloured("⛩️ Ancient China 🐉", "bold"))
                print(coloured("\nTrade accepted"))
                trade_counter = 1
            elif seed_trade == "n":
                clear_wait()
                print(coloured("⛩️ Ancient China 🐉", "bold"))
                print(coloured("\nOffer declined, moving to next villager"))
                # Villager 2
                while trade_counter == 0:
                    print(coloured("\nVillager: Curtis","green"))
                    print(coloured("Offer: 5 seeds","green"))
                    print(coloured("Cost: 15 coins","green"))
                    seed_trade = input("\nDo you want to accept this offer?(y/n)...")
                    if seed_trade == "y":
                        agent["coins"] = agent["coins"] - 15
                        clear_wait()
                        print(coloured("⛩️ Ancient China 🐉", "bold"))
                        print(coloured("\nTrade accepted"))
                        trade_counter = 1
                    elif seed_trade == "n":
                        clear_wait()
                        print(coloured("⛩️ Ancient China 🐉", "bold"))
                        print(coloured("\nOffer declined, moving to next villager"))
                        # Villager 3
                        while trade_counter == 0:
                            print(coloured("\nVillager: Sienna","green"))
                            print(coloured("Offer: 20 seeds","green"))
                            print(coloured("Cost: 20 coins","green"))
                            seed_trade = input("\nDo you want to accept this offer?(y/n)...")
                            if seed_trade == "y":
                                agent["coins"] = agent["coins"] - 20
                                clear_wait()
                                print(coloured("⛩️ Ancient China 🐉", "bold"))
                                print(coloured("\nTrade accepted"))
                                trade_counter = 1
                            elif seed_trade == "n":
                                clear_wait()
                                print(coloured("⛩️ Ancient China 🐉", "bold"))
                                print(coloured("\nOffer declined, moving to next villager"))  
                                # Villager 4
                                while trade_counter == 0:
                                    print(coloured("\nVillager: Max","green"))
                                    print(coloured("Offer: 15 seeds","green"))
                                    print(coloured("Cost: 35 coins","green"))
                                    seed_trade = input("\nDo you want to accept this offer?(y/n)...")
                                    if seed_trade == "y":
                                        agent["coins"] = agent["coins"] - 35
                                        clear_wait()
                                        print(coloured("⛩️ Ancient China 🐉", "bold"))
                                        print(coloured("\nTrade accepted"))
                                        trade_counter = 1
                                    elif seed_trade == "n":
                                        clear_wait()
                                        print(coloured("⛩️ Ancient China 🐉", "bold"))
                                        print(coloured("\nOffer declined, moving to next villager")) 
                                        # Villager 5
                                        while trade_counter == 0:
                                            print(coloured("\nVillager: Keira","green"))
                                            print(coloured("Offer: 50 seeds","green"))
                                            print(coloured("Cost: 5 coins","green"))
                                            seed_trade = input("\nDo you want to accept this offer?(y/n)...")
                                            if seed_trade == "y":
                                                agent["coins"] = agent["coins"] - 5
                                                clear_wait()
                                                print(coloured("⛩️ Ancient China 🐉", "bold"))
                                                print(coloured("\nTrade accepted"))
                                                trade_counter = 1
                                            elif seed_trade == "n":
                                                agent["inventory"].append("50 seeds")
                                                agent["coins"] = agent["coins"] - 5
                                                clear_wait()
                                                print(coloured("⛩️ Ancient China 🐉", "bold"))
                                                print(coloured("\nThe last offer will be taken by default"))
                                                trade_counter = 1                                  
                                            else:
                                                print()
                                                print(coloured("Invalid input","red"))                                  
                                    else:
                                        print()
                                        print(coloured("Invalid input","red"))                                 
                            else:
                                print()
                                print(coloured("Invalid input","red")) 
                        
                    else:
                        print()
                        print(coloured("Invalid input","red")) 
            else:
                print()
                print(coloured("Invalid input","red"))

        clear_screen()
        print(coloured("⛩️ Ancient China 🐉","bold"))
        print()
        print(coloured("You have enough seeds to start growing your rice plant","green"))
        continue_game()
        plant()
        time.sleep(3)
        clear_screen()
        agent["inventory"].append("Rice")
        stats(civilisation_number, agent)
        return "win", agent

    elif civilisation_number == 3:
        print("debug")

               
main()

