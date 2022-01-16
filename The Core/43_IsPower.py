"""
Determine if the given number is a power of some non-negative integer.

Example

For n = 125, the output should be
solution(n) = true;
For n = 72, the output should be
solution(n) = false.

"""
def solution(n):
    if n == 1:
        return True

    a = 2
    b = 2
    while a ** 2 <= n:
        while a ** b <= n:
            if a ** b == n:
                return True
            b += 1
        b = 2
        a += 1
    return False


print(solution(72))