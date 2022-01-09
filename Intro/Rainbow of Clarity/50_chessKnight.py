"""
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.


Example

For cell = "a1", the output should be
solution(cell) = 2.



For cell = "c2", the output should be
solution(cell) = 6.

"""

def solution(cell):
    x = 'abcdefgh'
    cell = x.index(cell[0]), int(cell[1])
    steps = [
            [-2, -1], [-1, -2], [1, -2], [2, -1],
            [2, 1], [1, 2], [-1, 2], [-2, 1]
            ]
    count = 0
    for i in range(len(steps)):
        temp_row = cell[0] + steps[i][0]
        temp_col = cell[1] + steps[i][1]
        if 0 <= temp_row <= 7 and \
            1 <= temp_col <= 8:
            count +=1
    return count


print(solution("g6"))
