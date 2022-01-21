"""
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
solution(n) = 11.
"""
def solution(n):
    numb = str(n)
    total = 0 
    for i in numb:
        total += int(i)
    return total

print(solution(29))
