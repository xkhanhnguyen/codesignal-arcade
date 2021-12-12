"""
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
solution(s) = 3.

There are 3 different characters a, b and c.


"""

def solution(s):
    unique_string = []
    for c in s:
        if c not in unique_string:
            unique_string.append(c)
    return len(unique_string)


print(solution("cabca"))


# better solution 
# def solution(s):
    # return len(set(s))
    # len(set(x)) tells you the size of the set of unique elements of x 