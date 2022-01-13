"""
grid is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits 
so that each column, each row, and each of the nine 3 × 3 sub-grids that compose 
the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents
 a correct solution to grid.

Example

For
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = true;

For
grid = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = false.

The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
These examples are represented on the image below.

"""

def solution(grid):
    # check row
    for row in grid:
        if sorted(list(set(row))) != sorted(row):
            return False
    # check col
    for col in range(len(grid)):
        cols = []
        for row in grid:
            cols += [row[col]]
        if sorted(list(set(cols))) != sorted(cols):
            return False
    # check sub-grids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            sub_grid = grid[row][col: col+3]
            sub_grid.extend(grid[row+1] [col: col+3])
            sub_grid.extend(grid[row+2] [col: col+3])
            if sorted(list(set(sub_grid))) != sorted(sub_grid):
                return False

    return True




false_grid = [[1,3,4,2,5,6,9,8,7], 
                [4,6,8,5,7,9,3,2,1], 
                [7,9,2,8,1,3,6,5,4], 
                [9,2,3,1,4,5,8,7,6], 
                [3,5,7,4,6,8,2,1,9], 
                [6,8,1,7,9,2,5,4,3], 
                [5,7,6,9,8,1,4,3,2], 
                [2,4,5,6,3,7,1,9,8], 
                [8,1,9,3,2,4,7,6,5]]
                
true_grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]

print(solution(true_grid)) 
# print(solution(false_grid)) 