"""

Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

"""

def solution(inputArray, k):
    # inputArray.pop(k)
    # print(inputArray[k::k])
    del inputArray[k-1::k]
    
    return inputArray

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))