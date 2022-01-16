"""
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

For n = 9, the output should be
solution(n) = 2.

There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
solution(n) = 0.

There are no ways to represent n = 8.
"""
def solution(n):
    count = 0
    base = 1
    while n > 0:
        n -= base
        if n % base == 0:
            count += 1
        base += 1
    return count - 1

# n = 15
# 4 + 5 + 6 = 15
# (3 + 1) + (3 + 2) + (3 + 3) = 15
# 3 + 3 + 3 = 15 - 1 - 2 - 3 ( base number 1, 2, 3)

# 15
# 15 - 1 -> 14 % 1
# 15 - 1 - 2 -> 12 % 2
# 15 - 1 - 2 - 3 -> 9 % 3


print(solution(9))
    