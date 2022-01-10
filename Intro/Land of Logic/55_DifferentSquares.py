"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
solution(matrix) = 6.

Here are all 6 different 2 × 2 squares:

- 1 2
  2 2
- 2 1
  2 2
- 2 2
  2 2
- 2 2
  1 2
- 2 2
  2 3
- 2 3
  2 1
"""

def solution(matrix):

    # use set because 
    # Sets cannot have two items with the same value.
    ans = set() 
    temp_str = ''
    
    for r in range(len(matrix)-1):
        for c in range(len(matrix[0])-1):
            temp_str = str(matrix[r][c]) + \
                        str(matrix[r][c + 1]) + \
                        str(matrix[r + 1][c]) + \
                        str(matrix[r + 1][c + 1])
            ans.add(temp_str)
    return ans

print(solution([[1, 2, 1],
                [2, 2, 2],
                [2, 2, 2],
                [1, 2, 3],
                [2, 2, 1]]))