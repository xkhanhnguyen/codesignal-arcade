"""
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
solution(n) = 0;
For n = 100, the output should be
solution(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
solution(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
"""
def solution(n):
    string = str(n)
    count = 0
    while len(string) != 1:
        count += 1
        total = 0
        for i in string:
            total += int(i)
        string = str(total)
    return count



print(solution(5))
print(solution(91))