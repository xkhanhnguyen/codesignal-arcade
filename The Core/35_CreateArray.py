"""
Given an integer size, return array of length size filled with 1s.

Example

For size = 4, the output should be
solution(size) = [1, 1, 1, 1].
"""
def solution(size):
    arr = []
    for i in range(size):
        arr.append(1)
    return arr

# return [1] * size
    