import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    for r, r_val in enumerate(maze):
        for i, val in enumerate(r_val):
            stdscr.addstr(r, i*2, val)

def find_start(maze, symbol):
    # Loop through the maze to view each row
    # Loop through each row to view their value
    # Return starting position
    for r, row in enumerate(maze):
        for i, val in enumerate(row):
            if val == symbol:
                return r, i
    
    return None

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        # get() returns what is in the set of "q"
        current_pos, path = q.get()
        # row and column from find_start's returned value
        row, col = current_pos

        if maze[row][col] == end:
            return path


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.clear()
    print_maze(maze, stdscr)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)