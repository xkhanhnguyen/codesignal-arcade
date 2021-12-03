def Minesweeper(matrix, r, c, row, col):
    mine = 0
    # top left 
    if not ((r < 1) or (c < 1)):
        if matrix[r - 1][c - 1]:
            mine += 1
            
    # top middle
    if not (r < 1):
        if matrix[r - 1][c]:
            mine += 1
    
    # top right
    if not ((r < 1) or (c >= col - 1)):
        if matrix[r - 1][c + 1]:
            mine += 1
         
    # left
    if not (c < 1):
        if matrix[r][c - 1]:
            mine += 1
    
    # right 
    if not (c >= col - 1):
        if matrix[r][c + 1]:
            mine += 1
            
    # bottom left
    if not ((r >= row - 1) or (c < 1)):
        if matrix[r + 1][c - 1]:
            mine += 1
            
    # bottom middle
    if not (r >= row - 1):
        if matrix[r + 1][c]:
            mine += 1
            
    # bottom right
    if not ((r >= row - 1) or (c >= col - 1)):
        if matrix[r + 1][c + 1]:
            mine += 1
    return mine


def solution(matrix):
    row = len(matrix)
    col = len(matrix[0])
    output = []
    for r in range(row):
        temp = []
        for c in range(col):
            temp.append(Minesweeper(matrix, r, c, row, col))
            
        output.append(temp)
                
    return output
            

