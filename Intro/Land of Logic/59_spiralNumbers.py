"""
Construct a square matrix with a size N × N containing integers 
from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

solution(n) = [[1, 2, 3],
                [8, 9, 4],
                [7, 6, 5]]
"""


def solution(n):
    # why not [[0] * n] * n
    # https://stackoverflow.com/questions/62017380/difference-between-0mn-and-0-for-i-in-range0-m-for-j-in-range0-n
    ans = [[0] * n for i in range(n)]

    num = 1 # start with number 1

    # set up two pointers to determine 
    # the low value and the high value of each loop of numbers
    low = 0
    high = n - 1 # n is the number of rows
    
    levels = int((n + 1 ) / 2) # how many loops do we need 
    for level in range(levels):
        for i in range(low, high + 1): # go right
            ans[level][i] = num
            num += 1
            
        for i in range(low + 1, high + 1): # go down
            ans[i][high] = num
            num += 1
            
        for i in range(high - 1, low - 1, -1): # go left
            ans[high][i] = num
            num += 1
            
        for i in range(high - 1,low, -1): # go up
            ans[i][low] = num
            num += 1
            
        low  += 1
        high -= 1
    return ans


print(solution(3))