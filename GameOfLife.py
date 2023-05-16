import random as rand
'''
Conway's Game of Life
Ryan Thompson
STAT 400
4/17/23
'''
def print_grid(grid): # Prints the 2D array to the console
    for row in grid:
        print(''.join(['1' if cell else '0' for cell in row])) # Transforms the True values into 1's and the False value to 0

def check_grid(grid): # Function checks to make sure all the values in the grid are alive or dead
    for row in grid:
        if True in row: 
            return False # If even a single cell is alive, the function will return False
    return True # Returns True if all cells are dead

def count_neighbors(grid, row, col): # Counts the number of neighbors a given cell has
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and (i != row or j != col): # Edge case catcher for proper count of nearby cells
                count += grid[i][j]
    return count

def lifecycle(grid, X, Y):
    # Any live cell with fewer than two live neighbors dies
    # Any live cell with two or three live neighbors lives on
    # Any live cell with more than three live neighbors dies
    # Any dead cell with exactly three live neighbors becomes alive
    update = [[False for _ in range(X)] for _ in range(Y)] # Creates a new grid of nulls that will be updated corresponding to the original grid
    for y in range(Y):
        for x in range(X):
            count = count_neighbors(grid, x, y) # Gets neighbor count for every value in the 2D array
            # Cell is alive
            if grid[y][x]: 
                update[y][x] = count in [2,3] # Cell dies or lives dpending on whether it's count value is 2 or 3
            # Cell is dead
            else:
                update[y][x] = count == 3 # Cell becomes alive in the new grid if the count == 3
    return update # Returns the new grid in place of the old one

def pattern_start(pattern, grid, X, Y): # Creates the starting pattern scaled to the size of the 2D array
    max_shape_size = min(X, Y) // 2 - 1 # Creates a numeric value of the maximum possible size the shape can feasibly be given the 2D array
    center_x = X // 2
    center_y = Y // 2
    size = min(max_shape_size, max(1, max_shape_size // 2))
    if pattern == "circle":
        for y in range(center_y - size, center_y + size + 1): # Loops and Math to create the circle in the grid
            for x in range(center_x - size, center_x + size + 1):
                if (x - center_x) ** 2 + (y - center_y) ** 2 <= size ** 2: 
                    grid[y][x] = True
    elif pattern == "square":
        for y in range(center_y - size, center_y + size + 1): # Loops to print the square
            for x in range(center_x - size, center_x + size + 1):
                if x >= 0 and x < X and y >= 0 and y < Y: 
                    grid[y][x] = True
    elif pattern == "diamond":
        for y in range(center_y - size, center_y + size + 1): # Loops to print the diamond in the grid
            for x in range(center_x - size, center_x + size + 1):
                if abs(x - center_x) + abs(y - center_y) <= size and x >= 0 and x < X and y >= 0 and y < Y:
                    grid[y][x] = True
    else:
        print("Invalid pattern choice, defaulting to random grid.") # If an invalid shape is entered, defaults to random
        valid_input = False
        while not valid_input:
            START = float(input('Enter a probability as a floating point decimal between 0.1 and 0.9 for starting cells: '))
            if START > 1 or START < 0.1:
                print("Invalid decimal. Try again.")
            else:
                valid_input = True
                grid = [[rand.random() < START for _ in range(X)] for _ in range(Y)] # Creates a grid of random values based on the START value
    return grid
    
def main():
    print("Welcome to Conway's Game of Life\n") # Inputs for the program
    X = int(input('How many rows?: '))
    Y = int(input('How many columns?: '))
    pattern = input('Enter "circle", "square", "diamond" or "random" to choose a starting pattern: ')
    start_grid = [[False for _ in range(X)] for _ in range(Y)]
    if pattern == "random":
        valid_input = False
        while not valid_input:
            START = float(input('Enter a probability as a floating point decimal between 0.1 and 0.9 for starting cells: '))
            if START > 1 or START < 0.1:
                print("Invalid decimal. Try again.")
            else:
                valid_input = True
                grid = [[rand.random() < START for _ in range(X)] for _ in range(Y)]
    else:
        grid = pattern_start(pattern, start_grid, X, Y) # Jumps to the shape starter
    for i in range(15):
        print('')
        print(i+1)
        print_grid(grid)
        print('')
        grid = lifecycle(grid, X, Y)
        if check_grid(grid) ==  True:
            print('All cells have perished. Ending Program.')
            break
main()