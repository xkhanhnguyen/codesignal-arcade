"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".
"""


def solution(inputString):
    output = ""
    for char in inputString:
        print(char)
        if char.isdigit():
            output += char
        else:
            break

    return output
# print(solution("123aa1"))
# print(solution("  3) always check for whitespaces"))