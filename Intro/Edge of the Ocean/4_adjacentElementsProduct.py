def solution(inputArray):
    output = []
    i, j = 0, 0
    while i < len(inputArray):
        j = i + 1
        while j < len(inputArray):
            product = inputArray[i] * inputArray[j]
            output.append(product)
            i += 1
            j += 1
        
        i += 1
    return max(output)

