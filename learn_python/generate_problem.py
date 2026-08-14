import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5

# Prompt the userr to solve a series of math problems while tracking there time

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    exp = str(left)  + operator + str(right)
    answer = eval(exp)

    return exp, answer

start_time = time.time()
wrong = 0

for i in range(TOTAL_PROBLEMS):
    exp, ans = generate_problem()
    while True:
        guess = input("Solve for problem #" + str(i + 1) + ": " + exp + "= ")
        if guess == str(ans):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time)

print("Congrats! You finished in: " + str(total_time) + " seconds!")
print("You've got " + str(wrong) + " answers incorrect")