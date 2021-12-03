def solution(matrix):
    sum = 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col] != 0:
                sum += matrix[row][col]
            else:
                break
    return sum

    

