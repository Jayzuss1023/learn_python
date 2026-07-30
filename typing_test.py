import curses
from curses import wrapper
import time
import random

# Select a random line from text file
def read():
    with open("typing.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def start_screen(stdscr):
    # Clears the screen
    stdscr.clear()
    # Add text to the screen
    stdscr.addstr("Welcome to your typing test!!")
    stdscr.addstr("\nPress any key to begin")
    stdscr.addstr("\n")
    # Refresh the screen
    stdscr.refresh()
    # Gets the key the user types in. Screen will close if this is not included
    stdscr.getkey()

def display_text(stdcsr, target, current, wpm=0):
    stdcsr.addstr(target)
    stdcsr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        if current[i] != target[i]:
            stdcsr.addstr(0, i, char, curses.color_pair(2))
        else:
            stdcsr.addstr(0, i, char, curses.color_pair(1))


def wpm_test(stdcsr):
    target_text = read()
    users_text = []
    wpm = 0
    start_time = time.time()
    stdcsr.nodelay(True)


    while True:
        # Account for returning a max of 1 second
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(users_text) / (time_elapsed / 60)) / 5)

        stdcsr.clear()
        display_text(stdcsr, target_text, users_text, wpm)
        stdcsr.refresh()

        # Convert users_text array into a string and match to the test text
        if "".join(users_text) == target_text:
            stdcsr.nodelay(False)
            break

        try:
            key = stdcsr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        # Account for deleting on backspace and not allow the users text to exceed the length of the prompt
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(users_text) > 0:
                users_text.pop()
        elif len(users_text) < len(target_text):
            users_text.append(key)

def main(stdcsr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    start_screen(stdcsr)
    
    # Loop that promps user to continue when finishing test
    while True:
        wpm_test(stdcsr)
        stdcsr.addstr(2, 0, "You have completed the typing test! Print any key to start again!")
        key = stdcsr.getkey()

        if ord(key) == 27:
            break
        

wrapper(main)