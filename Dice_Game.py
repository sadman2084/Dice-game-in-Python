import random

# Generating random number from the dice
def roll():
    min_value = 1
    max_value = 6
    roll_result = random.randint(min_value, max_value)
    return roll_result

# Asking how many players will play
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players")
    else:
        print("Invalid, Try Again")

max_score = 50
player_scores = [0 for _ in range(players)]### 0 to number of players initialized

# Main game loop
while max(player_scores) < max_score:
    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[player_index])
        current_score = 0  
        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() == "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

        player_scores[player_index] += current_score
        print("Your updated total score is:", player_scores[player_index])

print("Game Over! Maximum score reached by a player.")
