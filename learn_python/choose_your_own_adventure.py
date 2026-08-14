# Understanding If/Elif
# Creating a mini game where the user's decision affects there journey

name = input("Type your name ")

print("Welcome", name, "to your adventure")

answer = input(
    "You are on a dirt road. It has come to an end. You can go left or right. Please choose."
)

if (answer == "left"):
    answer = input("You can you a river. You can either walk around, or swim across it ")

    if (answer == "swim"):
        print("You swam and were eaten by an alligator")

    if (answer == "walk"):
        print("You walked too to no end and lost the game")
    
    else:
        print("Not a valid option. You lose")

elif (answer == "right"):
    answer = input("You came to a rusty old bridge. Do you want to Cross or Return? (cross/return) ")

    if (answer == "return"):
        print("You're sent back and lose!")

    elif (answer == "cross"):
        answer = input("Your crossing has lead you to a stranger. Talk to them? ")
        
        if (answer == "yes"):
            print("Game complete. You've won!")

        elif (answer == "no"):
            print("Ignoring the stranger lead you to losing.")

        else:
            print("Not a valid response. You lose!")


print("Thank you for playing", name)