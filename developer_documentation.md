**Game Map / Flowchart**
- Insert your flowchart or room map here as an image:

	*I do not need to put the image here as it is on google classroom.*

- Rooms: 

	*Ancient Greece, Ancient China, Ancient Rome, and a Final Battle.*

- Decision Points:

	*Main menu – start, instructions, or quit*

	*Weapon management – add, remove, or continue*

	*Battle – choose weapon, choose special attack*

	*Enemy counter – damage changes depending on enemy*

	*Extras – villager trading, restart after death* 

- Puzzle Areas:

	*Riddle challenge – at the start of a civilisation (tests knowledge/problem-solving).*

	*Villager trading puzzle – decide whether to trade or not, affects inventory.*

	*Battle system – challenge of choosing correct weapon/attack to defeat enemy.*

	*Resource management – ration use (lose or preserve items depending on choice).*

**Reflection (200+ Words)**

My game was a time travel themed adventure that travelled though different ancient civilisations like Ancient Greece. The player would complete a puzzle or challenge in each level. Something in my game that worked well and as planned in my game was the weapon management system, as users could choose to add or remove weapons from their arsenal before fighting, making it seem more interactive. To make this work I used the .append() and the .remove() functions inside an if/elif/else statement. Another part of my code that worked well was the riddle challenge because it adds a puzzle element to the game, inviting the player to think differently. One challenge that I faced was passing and tracking variables across different functions, I had to ensure that none of the variables were referenced before being assigned inside functions and loops. Something that went wrong in my game was that when I changed my inventory list during the game, it wouldn’t reset when the game restarted. To combat this problem I put my items list into a dictionary as a copy using .copy(), then I just referenced it through the dictionary when changing it. As I created my game, it got more complex and sophisticated as I went along, for example, I combined my lists into a few dictionaries which meant that many parts of my code took a lot less time to create. One way I did this was combining four different lists called; civilisations, cities, date, and mission into one dictionary because they all lined up with each other. One improvement that I could make in the future would be to have more branching storylines in the non-battle levels. I could do this by changing the challenge in Ancient China where you have to trade for rice plant seeds so that the amount of excess coins and seeds that the player ends up with actually matters later in the game. For example, the player could have the opportunity to buy an extra powerful attack in the final battle, but only if they have enough coins left over from the trading. This would make the storylines more interesting and relevant to the game, making the game more fun for the player. A coding concept that I understand a lot more after doing this project is dictionaries. This is because I actually used them in a practical way to store my data, seeing firsthand how much more efficient than lists they are. My understanding of dictionaries will be helpful in future projects because they are a very common, useful, and efficient way of storing data in python. 

**AI Usage Declaration**

I used Microsoft Copilot in Week 2 to help with a function to colour my text becuase I could not install Colorama on my laptop. I adapted the suggestion by adding many more colours and backgrounds to the function from this website: https://misc.flogisoft.com/bash/tip_colors_and_formatting. I have commented the relevant part in my `functions.py` file.

**Helper Function Use**

Tick the helper functions you used and explain how:

☑ cls() – Clears the screen between rooms 
- *Used to create smooth transitions between screens in the game.*

☑ animate() – Typewriter effect 

- *Used for certain strings and descriptions in my game.*

☑ coloured() – Highlight text for clues or danger

- *Used to make the text and visuals more interesting.*

**Checklist Before Submission**

☑ I have a `.py` file that runs without errors

☑ My game has 4+ rooms and player choices

☑ I used at least 2 helper functions

☑ I have submitted a flowchart or game map

☑ I have written a reflection (200+ words)

☑ I’ve documented any use of AI honestly according to the task and school policy
