import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"

def find_all_game_paths(source):
    game_paths = []
    # os.walk() will look at the root thats passed in, go into it's directories and then into their files
    # root > directories > files of the directories
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory:
                # Directory only returns the name not the file path
                path = os.path.join(source, directory)
                game_paths.append(path)
        break
    return game_paths

# Function that checks if directory exists
# Creates if no directory
def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)
    source_paths = find_all_game_paths(source_path)

    create_dir(target_path)

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source directory and a target - only.")

    # ["target1", "target2", "target3"]
    # [1:] split function cuts out the first argument in a list
    source, target = args[1:]
    main(source, target)