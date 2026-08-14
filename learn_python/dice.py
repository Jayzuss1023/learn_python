
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# This game prompts to select a number of players participating
# An array is then created based on how many players. Example for 3 Players: [0, 0, 0] 
# A winning score is set. Monitor the max score in the array
# The game will allow x number of players to roll a die
# The loop will continue through x number of players and will continue until a player has reached the max score
while True:
    players = input("Enter number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        print("players", players)
        # if players >= 2 and players <= 4:
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid, please try again")


max_score = 20
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer:", player_idx + 1, "turn has just started")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll? (Y) ").lower()
            if should_roll != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1. Your turn is done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            
            print("Your score is", current_score)

        player_scores[player_idx] =+ current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player", winning_idx, "won with a score of", max_score)
