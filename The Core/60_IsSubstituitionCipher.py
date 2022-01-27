# CodeSignal 
"""
A ciphertext alphabet is obtained from the plaintext alphabet by means of rearranging some characters. 
For example "bacdef...xyz" will be a simple ciphertext alphabet where a and b are rearranged.

A substitution cipher is a method of encoding where each letter of the plaintext alphabet 
is replaced with the corresponding (i.e. having the same index) letter of some ciphertext alphabet.

Given two strings, check whether it is possible to obtain them from each other using some 
(possibly, different) substitution ciphers.

Example

For string1 = "aacb" and string2 = "aabc", the output should be
solution(string1, string2) = true.

Any ciphertext alphabet that starts with acb... would make this transformation possible.

For string1 = "aa" and string2 = "bc", the output should be
solution(string1, string2) = false."""


from collections import Counter
import string


def solution(string1, string2):
    map_string = zip(string1, string2)
    s1 = Counter(string1).keys()
    s2 = Counter(string2).keys()
    s3 = Counter(map_string).keys()
    return len(s1) == len(s2) == len(s3)
    

print(solution("aacb", "aabc"))