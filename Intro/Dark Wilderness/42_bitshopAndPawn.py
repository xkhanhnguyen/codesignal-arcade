"""

    Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.
    
    Example
    
    for "A1" and "C3" output should be true,
    for "H1" and "H3" output should be false,
    [input] string cell1
    
    coordinates of the white bishop
    [input] string cell2
    
    coordinates of the black pawn
    [output] boolean
"""
def solution(bishop, pawn):
    x = 'abcdefgh'
    # cartesian coordinates, for example a1 would be (0, 1)
    bishop = x.index(bishop[0]), int(bishop[1])
    pawn = x.index(pawn[0]), int(pawn[1])
    
    if bishop[0] == pawn[0] or bishop[1] == pawn[1]:
        return False
        
    slope = ((bishop[1] - pawn[1]) / (bishop[0] - pawn[0]))
    
    if slope == 1 or slope == -1:
        return True
    else:
        return False


print(solution('a1', 'c3')) #true
print(solution('g1','f3')) #false