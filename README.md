# Conway's Game of Life

This is a Python implementation of Conway's Game of Life. It is a cellular automaton devised by the mathematician John Horton Conway in 1970. The game simulates the evolution of a grid of cells based on a set of rules, creating fascinating patterns and behaviors.
Prerequisites

    Python 3.x

Usage

    Clone the repository or download the Python script.

git clone https://github.com/RWThompson7/game-of-life.git

Open a terminal or command prompt and navigate to the project directory.

    cd game-of-life

Run the script.

    python game_of_life.py

    Follow the on-screen instructions:

    Enter the number of rows and columns for the grid.
    Choose a starting pattern: "circle", "square", "diamond", or "random".
    If you select "random," enter a probability as a floating-point decimal between 0.1 and 0.9 for starting cells.

    The game will start, and the grid will be displayed in the console. Each generation will be printed, showing the evolution of the cells over time.
    The program will continue for 15 generations by default. If all cells have died before that, the program will end.

Rules

The rules of Conway's Game of Life are as follows:

    Any live cell with fewer than two live neighbors dies (Underpopulation).
    Any live cell with two or three live neighbors survives.
    Any live cell with more than three live neighbors dies (Overpopulation).
    Any dead cell with exactly three live neighbors becomes alive (Reproduction).

Code Explanation

The provided Python code consists of several functions:

    print_grid(grid): Prints the 2D array representing the grid to the console.
    check_grid(grid): Checks if any cell in the grid is alive.
    count_neighbors(grid, row, col): Counts the number of live neighbors a given cell has.
    lifecycle(grid, X, Y): Implements the rules of the Game of Life and returns the updated grid.
    pattern_start(pattern, grid, X, Y): Initializes the grid with a specific pattern.
    main(): Handles user input, initializes the grid, and runs the game for a specified number of generations.

Feel free to modify and enhance the code according to your needs.
Examples

Here are some example patterns you can choose:

    "circle": Creates a circular pattern in the grid.
    "square": Creates a square pattern in the grid.
    "diamond": Creates a diamond pattern in the grid.
    "random": Generates a random grid based on a given probability.

If an invalid pattern choice is entered, the program defaults to a random grid.
Contributions

Contributions to this project are welcome. If you find any bugs or want to add new features, please create an issue or submit a pull request on GitHub.
