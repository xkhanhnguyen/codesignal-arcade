"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
solution(s) = "2a3bc"
"""

def solution(s):
    count = 1
    output = []
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        elif (s[i] != s[i+1]) and count >= 2:
            output.append(count)
            output.append(s[i])
            count = 1
        elif s[i] != s[i+1]:
            output.append(s[i])
            count = 1
        
        if ((i+1) == len(s)-1) and s[i] != s[i+1]:
            output.append(s[i+1])
        elif ((i+1) == len(s)-1) and s[i] == s[i+1]:
            output.append(count)
            output.append(s[i])
 
    return ''.join(map(str, output))

print(solution("aabbbc")) # "2a3bc"
print(solution("abbcabb")) # "a2bca2b"