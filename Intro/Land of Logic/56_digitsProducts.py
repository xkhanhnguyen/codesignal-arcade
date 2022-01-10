"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
solution(product) = 26;
For product = 19, the output should be
solution(product) = -1.
"""

def solution(product):
    if product == 0:
        return 10
    for i in range(3600):
        total = 1
        for j in str(i):
            total *= int(j)
            print(j, total)
        if total == product:
            return i
    return -1
    


print(solution(12))