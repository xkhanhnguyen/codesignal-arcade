"""
# LeetCode
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
 You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""
from collections import Counter
def solution(nums):
    appears = len(nums) / 2
    num, count = Counter(nums).most_common()[0]
    if count >= appears:
        return num
    

print(solution([1,1,3,2,4,5]))