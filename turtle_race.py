import random
import turtle
import time

WIDTH, HEIGHT = 500, 500
COLORS = ["white", "blue", "red", "green", "purple", "black"]


def get_number_of_racers():
    racers = 0
    
    while True:
        racers = input("Enter number of racers (2 - 8): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Must enter a valid digit!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("You're not in range! (2 - 10)")

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2  + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randint(0, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
        
    


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

racers = get_number_of_racers()
init_turtle()
colors = COLORS[:racers]
random.shuffle(COLORS)
winner = race(colors)
print(winner)