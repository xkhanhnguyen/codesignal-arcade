"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true.
"""

def solution(inputString):
    reverse_string = []
    for i in reversed(range(len(inputString))):
       reverse_string.append(inputString[i])
    temp = []
    for i in range(len(reverse_string)):
        if reverse_string[i] == inputString[i]:
            # print(inputString[i])
            temp.append(reverse_string[i] )
            # print(len(temp))
    if len(temp) == len(inputString):
        return True
    else:
        return False