import random


MAX_LINES = 3
MIN_BET = 1
MAX_BET = 50

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A": 3,
    "B": 6,
    "C": 9,
    "D": 9
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

                
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    current_symbols = all_symbols[:]

    for col in range(cols):
        column = []

        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end=" ")
        print()

def get_deposit():
    while True:
        deposit = input("How much would you like to deposit? ($) ")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("You must place a bet greater than 0")
        else: 
            print("Please enter a number")
    return deposit

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) + "): " )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a number of lines between the range")
        else:
            print("Please enter a number")
        
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? ($): " )
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Your bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
        
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if balance < total_bet:
            print(f"Insufficient funds. You've deposited ${balance}. You're betting against {lines} line at ${bet} per line. This puts your total bet at ${total_bet}")
        else:
            break

    columns = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(columns)
    winnings, winning_lines = check_winnings(columns, lines, balance, symbol_values)
    print(f"You won ${winnings}")
    print(f"Winning lines:", *winning_lines)
    return winnings - total_bet

def main():
    deposit = get_deposit()
    while True:
        play = input("Would you care to play? (q to quit)").lower()
        if play == "q":
            break
        else:
            deposit += spin(deposit)
    
    print(f"You left with ${deposit}")

main()