"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.

"""

def solution(inputArray, k):
    sum_ = sum(inputArray[:k])
    output = []
    output.append(sum_)
    for i in range(len(inputArray) - k):
        sum_ += (inputArray[i+k] - inputArray[i])
        output.append(sum_)
        print(output)
    return max(output)



# print(solution([2, 3, 5, 1, 6], 2))
# print(solution([1, 3, 2, 4],3))
print(solution([3, 2, 1, 1],1))