"""
Given a string, find the shortest possible string which can be achieved by adding characters
to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
solution(st) = "abcdcba".
"""

def solution(st):
    if st == st[::-1]:
        return st
    index = 0
    substring = st[index:]
    while substring != substring[::-1]:
        index += 1
        substring = st[index:]

    return st + st[index -1::-1]




print(solution('abcdc'))
print(solution('ababab'))