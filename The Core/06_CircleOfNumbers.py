"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
solution(n, firstNumber) = 7.

"""

def solution(n, firstNumber):
    output = firstNumber + ( n // 2)
    if output > n:
        return output - n
    elif output == n:
        return 0
    return output

# def solution2(n, firstNumber):
#     return (firstNumber + n / 2) % n


print(solution(10,2)) #7
print(solution(10,7)) #2
print(solution(6,3))


