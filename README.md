# learn_python

Practice repo for Python. Most files are small, standalone scripts I wrote while learning: terminal games, a few string/number problems, and some file/system utilities.

Nothing here is part of a packaged app. Pick a `.py` file and run it.

## Technologies

- **Python 3** (standard library for most scripts)
- **curses** — typing test and maze path visualization
- **turtle** — turtle race
- **pygame** — aim trainer
- **cryptography** (`Fernet`) — password manager encryption
- **Go** (optional) — sample game folders under `data/` that `get_game_data.py` can copy and compile

## Highlights

**Games**

- `aim_trainer.py` — click targets against a timer (pygame)
- `turtle_race.py` — pick how many turtles will race. first to the finish wins
- `slot_machine.py` — deposit, pick lines/bet, spin, check payouts
- `maze.py` — Locate quickest route from `O` to `X` on a grid, drawn in the terminal
- `typing_test.py` — WPM test using lines from `typing.txt`
- `color_game.py` — Mastermind-style code guessing
- `choose_your_own_adventure.py` — branching text stories. `story.txt` is a sample

**String / number practice**

- `romanizer.py` — Arabic numbers to Roman numerals.
- `string_to_int.py` — `atoi`-style parse with sign, whitespace, and 32-bit clamping
- `zizag_conversion.py` — zigzag string conversion
- `longest_palendrome.py` — longest palindromic substring
- `countingBits.py` — count `1` bits and collect their positions

**Utilities**

- `generate_pwd.py` — random password with optional digits/symbols
- `password_manager.py` — encrypt/decrypt stored passwords with a Fernet key
- `get_game_data.py` — walk a source folder, copy `*game*` dirs, write JSON metadata, compile `.go` files
- `copy_folder_to_directory.py` — scheduled folder copy
- `calc_time.py` — countdown/alarm
- `generate_problem.py` — timed math problems
- `dice.py` / `rock_paper_scissor.py` — small random games

## Technologies

- **Python 3** - standard library for most scripts
- **curses** — typing test and maze path visualization
- **turtle** — turtle race
- **pygame** — aim trainer
- **cryptography** (`Fernet`) — password manager encryption
