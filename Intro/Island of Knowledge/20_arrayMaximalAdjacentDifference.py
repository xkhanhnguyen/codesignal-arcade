def solution(inputArray):
    max_diff = []
    for i in range(len(inputArray)-1):
        max_diff.append(abs(inputArray[i+1] - inputArray[i]))
    return max(max_diff)
