# Sushi-Slicer
Language: Python

Packages needed: Pygame, os, random 

Images: please download the “sushi” folder

For our project, we will be coding a game called Sushi Slicer, which resembles the phone game Fruit Ninja, except using sushi ingredients instead of fruits. The user will be given the choice to choose between Sushi Slicer mode and Fruit Ninja mode within our Sushi Slicer game. The components of our game that will appear on the screen include a background of seaweed/wooden backboard (depends on mode the user chooses), a point tracker, three lives, a riceglob/bomb (for immediate termination), and different sushi ingredients: shrimp, crab, eel, avocado, cucumber, salmon, tuna, carrot, and tamago, or fruits: guava, melon, orange, and pomegranate.

The game begins with a start screen. Our game has two modes: Sushi Slicer and Fruit Ninja. Sushi Slicer mode will have sushi ingredients thrown up in the air with seaweed as the background. In Fruit Ninja mode, instead of sushi ingredients, fruits will be thrown up into the air with a wooden background. The start screen instructions indicate that if the user presses “space”, the game will be Fruit Ninja mode whereas if the user presses “return”, the game will be Sushi Slicer mode. If the user presses any other key, the game will not start and will remain on the start screen.

To slice the fruits/ingredients, the user will simply have to move the mouse across the fruit/ingredient. Once the object is sliced, the object will turn into an image that represents the cut version of that object. For instance, a sliced sushi ingredient will result in a sushi roll being animated while a sliced fruit will generate a halved fruit. In the initial rounds of the game, the game difficulty will start off as easy and only a few sushi ingredients/fruits will be thrown up. As the user makes it past certain point benchmarks, specifically 4 and 10 points, the game will start to throw an increasing number of objects for the user to slice. 

Once the ingredient is sliced, the user’s score will be incremented by 1; if special items, such as a tamago (in the Sushi Slicer mode) or a guava (in the Fruit Ninja mode), are sliced, 2 points will be added to the score. In addition to sushi ingredients/fruits, objects that lead to immediate termination will also be thrown up into the screen. In the Sushi Slicer mode, slicing a rice glob automatically ends the game; in the Fruit Ninja mode, slicing a bomb automatically ends the game. For both modes, if the user fails to slice an ingredient, a life will be subtracted. The termination of 3 lives will automatically end the game, if a rice glob or bomb has not been sliced up until that point. 

When the game ends, a screen displaying the player’s score will appear, as well as lines asking which mode the player would like to play next. The score will then reset to zero and the difficulty level will be reset. 
 
