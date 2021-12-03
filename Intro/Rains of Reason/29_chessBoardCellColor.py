"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.

For cell1 = "A1" and cell2 = "H3", the output should be
solution(cell1, cell2) = false.

"""

def board(letter, number):
    if letter in ['A', 'C', 'E', 'G'] and int(number) %2 == 1:
        return 'b'
    if letter in ['B', 'D', 'F', 'H'] and int(number) % 2 == 0:
        return 'b'
    else:
        return 'w'

def solution(cell1, cell2):
    l1 = cell1[0]
    n1 = cell1[1]
    
    l2 = cell2[0]
    n2 = cell2[1]
    
    if board(l1, n1) == board(l2, n2):
        return True
    else:
        return False
    
    
