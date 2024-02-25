# Dice-game-in-Python


This is a simple console-based dice game implemented in Python. The game allows 2 to 4 players to take turns rolling a six-sided die in an attempt to accumulate points. The first player to reach or exceed a total score of 50 wins the game.

## How to Play

1. **Setup**
   - Run the `Dice_Game.py` script in a Python environment.
   - Follow the prompts to enter the number of players (2 to 4 players).

2. **Gameplay**
   - Each player takes turns rolling a six-sided die.
   - On each turn, a player can choose to roll the die or end their turn.
   - If a player rolls a 1, their turn ends, and they lose all points accumulated during that turn.
   - If a player rolls any other number (2 to 6), that number is added to their current turn score.
   - Players can continue rolling until they choose to end their turn or until they roll a 1.
   
3. **Winning the Game**
   - The game continues until one player reaches or exceeds a total score of 50.
   - Once a player achieves the winning score, the game ends, and that player is declared the winner.

## Features

- Dynamic player count: Players can choose to play with 2 to 4 players.
- Random dice rolls: Dice rolls are generated randomly using Python's `random` module.
- Score tracking: The game keeps track of each player's total score and displays it after each turn.
- Error handling: Input validation ensures that players enter valid inputs for the number of players.

## Contributing

Contributions are welcome! If you'd like to suggest improvements, report bugs, or contribute new features, feel free to submit a pull request or open an issue on the GitHub repository.

---
