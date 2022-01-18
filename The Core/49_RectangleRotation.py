"""
A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. 
Its center (the intersection point of its diagonals) coincides with the point (0, 0), 
but the sides of the rectangle are not parallel to the axes; instead, 
they are forming 45 degree angles with the axes.

How many points with integer coordinates are located inside the given rectangle 
(including on its sides)?

Example

For a = 6 and b = 4, the output should be
solution(a, b) = 23.

The following picture illustrates the example, and the 23 points are marked green.
"""
# https://medium.com/hard-mode/coding-challenge-rectangle-rotation-10e2a2416ef3

from math import prod

def solution(a, b):
    aHalfBisect = (a / 2 ** 0.5) / 2
    bHalfBisect = (b / 2 ** 0.5) / 2
    
    rect1 = [int(aHalfBisect) * 2 + 1, int(bHalfBisect) * 2 + 1]
    rect2 = [0]*2

    if aHalfBisect - int(aHalfBisect) < 0.5: 
        rect2[0] = rect1[0] - 1
    else: 
        rect2[0] = rect1[0] + 1
    
    
    if bHalfBisect - int(bHalfBisect) < 0.5:
        rect2[1] = rect1[1] - 1
    else: 
        rect2[1] = rect1[1] + 1

    

    return prod(rect1) + prod(rect2)

print(solution(6, 4))
