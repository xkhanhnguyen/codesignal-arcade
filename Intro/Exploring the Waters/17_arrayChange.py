def solution(inputArray):
    count_move = 0
    for i in range(len(inputArray)-1):
        temp = inputArray[i] + 1
        if inputArray[i+1] < temp :
            count_move +=  temp - inputArray[i+1]
            inputArray[i+1] = temp 
          
    return count_move
        

