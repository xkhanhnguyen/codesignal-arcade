"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
solution(n) = 52;
For n = 1001, the output should be
solution(n) = 101.
"""

def solution(n):
    n = str(n)
    ans = 0

    for i in range(len(n)-1):
        if int(n[i]) < int(n[i+1]):
            ans = int(n[:i] + n[i+1:])
            break
    if ans == 0:
        ans = int(n[:-1])

    return ans

print(solution(1001))

