def solution(inputArray):
    output = []
    max_len = len(max(inputArray, key=len))
    # print(max_len)
    for i in range(len(inputArray)):
        if max_len <= len(inputArray[i]):
            max_len =  len(inputArray[i])
            # print(max_len, inputArray[i])
            output.append(inputArray[i])
        
    return output
    

