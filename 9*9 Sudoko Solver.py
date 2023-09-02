import random
import math

def initialize_grid():
    """Initialize an empty Sudoku grid."""
    grid = [[0] * 9 for _ in range(9)]
    return grid

def is_valid_move(grid, row, col, num):
    """Check if placing 'num' at grid[row][col] is a valid move."""
    # Check row and column
    if num in grid[row] or num in [grid[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

def calculate_cost(grid):
    """Calculate the cost of the current grid."""
    cost = 0
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                cost += sum(1 for num in range(1, 10) if not is_valid_move(grid, row, col, num))
    return cost

def simulated_annealing(grid):
    """Solve the Sudoku puzzle using simulated annealing."""
    T = 1.0  # Initial temperature
    alpha = 0.99  # Cooling rate
    max_iterations = 10000  # Maximum number of iterations
    
    current_cost = calculate_cost(grid)
    
    for _ in range(max_iterations):
        if current_cost == 0:
            # Puzzle is solved
            return grid
        
        # Randomly select a cell to change
        row, col = random.randint(0, 8), random.randint(0, 8)
        
        if grid[row][col] != 0:
            continue
        
        # Randomly select a new number for the cell
        new_num = random.randint(1, 9)
        
        # Calculate the change in cost
        original_num = grid[row][col]
        grid[row][col] = new_num
        delta_cost = calculate_cost(grid) - current_cost
        
        if delta_cost <= 0 or random.random() < math.exp(-delta_cost / T):
            # Accept the move
            current_cost = calculate_cost(grid)
        else:
            # Revert the change
            grid[row][col] = original_num
        
        # Decrease the temperature
        T *= alpha
    
    # If we reach this point without solving the puzzle, return None
    return None

def print_grid(grid):
    """Print the Sudoku grid."""
    for row in grid:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Initial Sudoku Grid:")
    print_grid(sudoku_grid)

    solution = simulated_annealing(sudoku_grid)

    if solution:
        print("\nSolved Sudoku Grid:")
        print_grid(solution)
    else:
        print("\nSimulated Annealing did not find a solution.")
