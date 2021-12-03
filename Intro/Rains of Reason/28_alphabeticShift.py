"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".
"""

def solution(inputString):
    new_String = []
    for i in inputString:
        new_String.append(chr(ord(i) + 1))
        new_String = [a.replace('{', 'a') for a in new_String]

    return ''.join(map(str,new_String))


    
# chr() takes in an integer i and converts it to a character c, so it returns a character string.
# The ord() function takes a string argument of a single Unicode character and returns its 
# integer Unicode code point value. It does the reverse of chr().
print(solution("crazy"))