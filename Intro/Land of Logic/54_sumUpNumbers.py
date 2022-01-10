"""
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
solution(inputString) = 14.
"""

import re
def solution(inputString):
    price = [int(x) for x in re.findall('[0-9]+', inputString) if x.isdigit()]
    print(price)
    return sum(price)

print(solution("2 apples, 12 oranges")) #14
print(solution("there are some (12) digits 5566 in this 770 string 239")) #6587
print(solution("abcdefghijklmnopqrstuvwxyz1AbCdEfGhIjKlMnOpqrstuvwxyz23,74 -"))