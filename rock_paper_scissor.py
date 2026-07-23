# A simple rock, paper, scissors game
# User vs System
# Tally total wins for each
# Announce score at the end
import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # Rock: 0 | Paper: 1 | Scissors: 2
    computer_pick = options[random_number]

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
        continue
    else:
        print("You lost this round!")
        computer_wins += 1
    
print("You won:", user_wins, "times")
print("The computer won:", computer_wins, "times")
print("Goodbye!")