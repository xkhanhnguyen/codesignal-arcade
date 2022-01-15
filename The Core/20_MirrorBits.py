"""
Reverse the order of the bits in a given integer.

Example

For a = 97, the output should be
solution(a) = 67.

97 equals to 1100001 in binary, which is 1000011 after mirroring, 
and that is 67 in base 10.

For a = 8, the output should be
solution(a) = 1.
"""
def solution(a):
    bi_numb = format(a, "b") # use format to remove the 0b prefix from its output
    return int(bi_numb[::-1],2)

print(solution(97))