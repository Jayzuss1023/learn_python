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
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    for r, r_val in enumerate(maze):
        for i, val in enumerate(r_val):
            if (r, i) in path:
                stdscr.addstr(r, i*2, "X", RED)
            else:
                stdscr.addstr(r, i*2, val, BLUE)

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


    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()


        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:

            r, c = neighbor
            if maze[r][c] == "#":
                continue
            if neighbor in visited:
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)




def find_neighbors(maze, row, col):
    neighbors = []

    # ROWS: 
    # The highest point of the maze is 0
    if row > 0: # UP
        neighbors.append((row - 1, col))
    if row < len(maze): # DOWN
        neighbors.append((row + 1, col))

    # COLUMNS:
    if col > 0: # LEFT
        neighbors.append((row, col - 1))
    if col < len(maze[0]): #RIGHT
        neighbors.append((row, col + 1))
    
    return neighbors


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)

