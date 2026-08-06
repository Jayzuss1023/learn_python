import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]

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


# Strip text from a path to create a new dir name for it
def get_name_from_paths(paths, to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir = dir_name.replace(to_strip, "")
        new_names.append(new_dir)
    return new_names

# Function that checks if directory exists
# Creates if no directory
def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

# Overwrite dir if it already exists
# Delete a dir if it exists
# Copy dir
# Recursive copy. Copy other dirs and their contents inside one dir
def copy_and_overwrite(source, dest):
    if os.path.exists(dest):
        # permanently delete dir
        shutil.rmtree(dest)
    # Recursively copy all from sourcee to dest,
    shutil.copytree(source, dest)


def make_json_metadata_file(path, game_dirs):
    data = {
        "gameName": game_dirs,
        "numberOfGames": len(game_dirs)
    }

    with open(path, "w") as f:
        json.dump(data, f),


def compile_game_code(path):
    code_file_name = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break
        break

    if code_file_name is None:
        return

    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command, path)


def run_command(command, path):
    cwd = os.getcwd()
    os.chdir(path)

    result = run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)
    print("Complete result", result)

    os.chdir(cwd)

    

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)
    
    game_paths = find_all_game_paths(source_path)
    new_game_dirs = get_name_from_paths(game_paths, "_game")

    create_dir(target_path)

    for src, dest in zip(game_paths, new_game_dirs):
        dest_path = os.path.join(target_path, dest)
        copy_and_overwrite(src, dest_path)
        compile_game_code(dest_path)

    json_path = os.path.join(target_path, "metadata.json")
    make_json_metadata_file(json_path, new_game_dirs)
    



if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source directory and a target - only.")

    # ["target1", "target2", "target3"]
    # [1:] split function cuts out the first argument in a list
    source, target = args[1:]
    main(source, target)