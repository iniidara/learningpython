# Python Learning Journey

This repository is a personal collection of Python exercises and small experiments. It records a practical learning process: starting with strings and dictionaries, then adding loops, functions, input validation, random programs, file handling, automation, and object-oriented programming.

The files are not one application. Each script focuses on a particular idea or exercise. Some are complete demonstrations, while others are deliberately unfinished experiments that show what was being learned at the time.

## What This Repository Covers

- Strings and formatted output
- Dictionaries, lists, and nested data
- Loops and conditional logic
- Interactive input with `input()`
- Input validation and string methods
- Functions and reusable pieces of logic
- Random numbers and simple games
- Table formatting and nested loops
- File creation and writing quiz data
- Clipboard and command-line automation
- Classes, methods, special methods, and object composition

## Suggested Learning Path

The filenames do not guarantee the exact order in which the exercises were written, but the code suggests the following progression.

### 1. Strings and output

`stringmanipulation.py` is an early foundation exercise. It explores multiline strings, quotation marks, and how Python displays text.

### 2. Dictionaries and state

`dictionaries.py` introduces key/value data, checking whether a key exists, and adding values to a dictionary.

`characterCount.py` builds on that idea by counting how often each character appears. It uses a dictionary as an accumulator and demonstrates `setdefault()` and repeated updates inside a loop.

`input.py` makes dictionaries interactive by creating a small birthday database. It combines `input()`, a loop, dictionary lookups, updates, and `break` to keep the program running until the user chooses to stop.

### 3. Loops and validation

`validateinput.py` demonstrates a common real-world pattern: keep asking until the user enters acceptable data. It uses `isdecimal()` and `isalnum()` to validate an age and password.

`isphonenumber.py` packages phone-number validation into a function. This introduces early returns, indexing, string methods, and the idea that a function can answer a yes-or-no question.

### 4. Functions and collection processing

`fantasygame.py` uses a function to turn a list of collected loot into item totals. It demonstrates list iteration, dictionary mutation, aggregation, and separating calculation from printing.

`totalbrought.py` attempts a similar calculation with nested dictionaries: determining how many of an item a group of guests brought. It is currently incomplete, but it represents a useful next step in working with nested data.

### 5. Interactive programs and games

`gamme.py` is a coin-toss guessing game. It combines random numbers, normalized input, conditionals, repeated attempts, and `break`.

`tictactoe.py` represents a board with a dictionary and prints it as a grid. It currently focuses on displaying structured data rather than implementing a complete playable game.

### 6. Nested loops and formatted tables

`printtable.py` calculates the width of each column in a two-dimensional list and prints an aligned table. It is a good exercise in nested loops, `max(..., key=len)`, string alignment, and formatted output.

`table.py` appears to be an unfinished alternative or continuation of the table-formatting exercise. Its incomplete loop shows the work-in-progress stage of the exercise.

### 7. Automation and external modules

`ppppd.py` experiments with copying text to the clipboard and reading it back using `pyperclip`.

`mapIt.py` begins a command-line map utility. It reads an address from command-line arguments or the clipboard and prepares it for use with a browser. This introduces `sys.argv`, fallback logic, and the idea of connecting a Python script to another application.

### 8. Larger programs and file generation

`randomquizgen.py` is the most integrated exercise in the directory. It:

- Stores Nigerian states and capitals in a dictionary
- Randomizes the order of quiz questions
- Creates multiple quiz versions
- Builds answer keys
- Writes quiz data to files
- Uses formatted strings and nested loops

This project brings together data structures, randomness, copying, file I/O, formatting, and program structure in one script. It is a useful milestone because the individual Python features now work together to produce a practical result.

### 9. Object-oriented programming

`fractionclass.py` introduces a `Fraction` class, instance attributes, a constructor, and `__str__()` for readable output.

`fractionclass2.py` extends that class with addition, multiplication, inversion, and in-place state changes. This shows the transition from storing data in objects to giving objects behavior.

`classes.py` defines a `Coordinate` class with a distance method and a string representation. It introduces geometric calculation and object methods.

`circleclass.py` builds on coordinates with a `Circle` class. The circle uses a coordinate object to determine whether a point lies inside it, demonstrating composition: one object working with another object.

## File Guide

| File | Main lesson | Current state |
| --- | --- | --- |
| `stringmanipulation.py` | Multiline strings and output | Small demonstration |
| `dictionaries.py` | Dictionary lookup and insertion | Complete exercise |
| `characterCount.py` | Counting with a dictionary | Complete exercise |
| `input.py` | Interactive dictionary program | Working demonstration |
| `validateinput.py` | Repeated input validation | Working demonstration |
| `isphonenumber.py` | Functions and string validation | Working demonstration |
| `fantasygame.py` | Inventory aggregation | Complete exercise |
| `totalbrought.py` | Nested dictionary totals | Incomplete |
| `gamme.py` | Random guessing game | Working but lightly validated |
| `tictactoe.py` | Dictionary-based board display | Display exercise |
| `printtable.py` | Dynamic table formatting | Complete exercise |
| `table.py` | Table-formatting experiment | Does not compile yet |
| `ppppd.py` | Clipboard interaction | Small experiment |
| `mapIt.py` | Command-line and clipboard automation | Partially implemented |
| `randomquizgen.py` | Randomized quiz and file output | Largest integrated exercise |
| `fractionclass.py` | First class and `__str__()` | Introductory OOP |
| `fractionclass2.py` | Methods and object state | OOP extension |
| `classes.py` | Coordinate objects and distance | Working OOP exercise |
| `circleclass.py` | Composition and geometry | Working OOP exercise |

## Learning Milestones

The repository shows several important steps in the learning process:

1. Moving from printing values to storing information in dictionaries and lists.
2. Using loops to process multiple values instead of handling each value manually.
3. Turning repeated logic into functions such as phone validation and inventory totals.
4. Building interactive programs that respond to user input.
5. Combining several concepts in a practical program, especially the quiz generator.
6. Using an external package and interacting with the clipboard.
7. Writing data to files instead of keeping every result only in memory.
8. Modeling data and behavior with classes and methods.
9. Combining objects through composition in the coordinate and circle exercises.

## How to Run the Exercises

Python 3 is required. From this directory, a script can generally be started with:

```text
python filename.py
```

For example:

```text
python randomquizgen.py
```

The interactive programs wait for input in the terminal. `randomquizgen.py` creates quiz output files in the current working directory.

The clipboard exercises use the third-party `pyperclip` package. Install it with:

```text
python -m pip install pyperclip
```

`ppppd.py` and `mapIt.py` may also depend on the operating system's clipboard support. `mapIt.py` is intended to open or prepare a map address, but its browser-opening step is not finished yet.

## Current Development Notes

This is a learning repository, so unfinished code is part of its history. The main areas that still need attention are:

- `table.py` contains an incomplete `for` statement and cannot compile.
- `totalbrought.py` ends with an undefined name, so its total-calculation function is unfinished.
- `mapIt.py` prepares an address but does not complete the browser-opening behavior.
- `fractionclass2.py` returns floating-point results for arithmetic instead of new fraction objects.
- The fraction classes do not yet protect against a zero denominator.
- Some scripts accept invalid input or edge cases without explaining what went wrong.
- Naming conventions vary between `camelCase` and Python's usual `snake_case` style.
- Several examples rely on global data rather than passing data into functions.
- There are currently no automated tests or dependency file.

These are not failures of the learning process. They are useful markers of the next concepts to practice: debugging, defensive programming, refactoring, testing, and organizing reusable code.

## Suggested Next Steps

1. Finish `totalbrought.py`, then pass the guest data into the function instead of relying on global variables.
2. Complete `table.py` or remove it once `printtable.py` becomes the preferred version.
3. Finish `mapIt.py` with `webbrowser.open()` and validate missing or empty addresses.
4. Add zero-denominator checks and fraction-returning arithmetic to the fraction classes.
5. Normalize function and variable names to `snake_case`.
6. Add a small test file for phone validation, inventory totals, fractions, and geometry boundaries.
7. Use `with open(...)` when working with files and document generated filenames.
8. Add a `requirements.txt` containing `pyperclip` if the clipboard exercises will be run on another computer.
9. Add short usage examples and expected output for the interactive scripts.

## Overall Progress

This directory shows a broad and practical Python learning path. The strongest progression is from isolated language features to small programs that combine those features, followed by experiments with external tools and object-oriented design. `randomquizgen.py` is the clearest example of the concepts working together, while the fraction, coordinate, and circle files show the beginning of a more structured way to model problems.

The next stage is less about learning entirely new syntax and more about making the existing programs reliable: complete unfinished exercises, handle edge cases, separate input from logic, write tests, and turn successful experiments into reusable modules.
