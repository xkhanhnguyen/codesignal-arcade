"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
solution(text) = "steady".
"""
import re
def solution(text):
    text = re.split('[^a-zA-Z0-9]+',text). # split on non-alphanumeric characters
    dicts = {}
    for word in text:
        dicts[word] = len(word)
    
    return max(dicts, key=dicts.get)


print(solution("Ready, steady, go!"))
print(solution("ab-CDE-fg_hi"))