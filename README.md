Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.



To carry out this game, three classes were created, the CARD class, which will have a method that will randomly select a number between 1 and 13, for that the RANDOM library will also be imported, the second class that was created was PLAYER , this class has three methods WINNER, LOSER and SCORE, these methods will allow adding or subtracting the points that the player accumulates, if he gives a correct answer 100 points will be added to his score, on the other hand if he gives a wrong answer, 75 will be deducted points from the score, finally the SCORE method will return the current score that the player has. Finally, the last class that was created was the MANAGER class, which is in charge of directing the game, it has three methods that will allow the player to interact with the other classes and carry out the game.
