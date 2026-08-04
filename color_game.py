import random
COLORS = ["R", "G", "B", "Y", "W"]
TRIES = 10
COLOR_LENGTH = 4

def generate_code():
    code = []
    for _ in range(COLOR_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():
    while True:
        guess = input("Guess your choice of colors (r g b y, w): ").upper().split(" ")
        print(len(guess))
        if len(guess) != COLOR_LENGTH:
            print(f"You must guess {COLOR_LENGTH} colors")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid {color} Please try again")
                break
            else:
                break

        return guess
        

def check_results(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            # This adds the color into the dictionary and sets it to 0 {"R": 0}
            color_counts[color] = 0
        color_counts[color] += 1



        # The loop above adds the color and counts of each color
        # Below we add which colors are properly positioned
        # This loop will remove from counts to show how many are incorrect
        for guess_color, real_color in zip(guess, real_code):
            if guess_color == real_color:
                correct_pos += 1
                color_counts[guess_color] += 1

        # The above loop accounted for values correctly position
        # Now to evaluate colors + count that still exist, but are NOT correctly positioned
        for guess_color, real_color in zip(guess, real_code):
            if guess_color in color_counts and color_counts[guess_color] > 0:
                incorrect_pos += 1
                color_counts[guess_color] -=1
        
        return correct_pos, incorrect_pos


def game():
    print(f"Welcome to the game!You have {TRIES} to get it right")
    print("The colors you're allowed to use are: ", *COLORS )
    code = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_results(guess, code)

        if correct_pos == COLOR_LENGTH:
            print("You've guess all correct positions!")
            break

        print(f"You have correctly positioned: {correct_pos} | incorrectly positioned: {incorrect_pos}")
        print(f"Number of attemps made: {attempts}")

    else:
        print(f"You've run out of tries! The code was: {code}")

if __name__ == "__main__":
    game()