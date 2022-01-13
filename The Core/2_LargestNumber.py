"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
solution(n) = 99.

"""
def solution(n):
    ans = ''
    for i in range(0,n):
        ans += '9'
    return int(ans)

print(solution(3))