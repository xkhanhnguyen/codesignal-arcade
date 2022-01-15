"""
Define an integer's roundness as the number of trailing zeroes in it.

Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.

Example

For n = 902200100, the output should be
solution(n) = true.

One of the possible ways to increase roundness of n is to swap digit 1 with digit 0 preceding it: 
roundness of 902201000 is 3, and roundness of n is 2.

For instance, one may swap the leftmost 0 with 1.

For n = 11000, the output should be
solution(n) = false.

Roundness of n is 3, and there is no way to increase it.
"""
def solution(n):
    string = str(n)
    # Check for immediate rejection
    if '0' not in string or len(string) < 2:
        return False
    # Since we know there's a 0, if it's not on
    # the left, then we know to accept
    if string[-1] != '0':
        return True
    # If there is only one 0, it must be at the end, so reject.
    if string.count('0') == 1:
        return False
    # If there are any numbers between the first 0
    # and the end of the string, then accept.
    first_zero = string.find('0')
    ans = string[first_zero:]
    return ans.count('0') != len(ans)