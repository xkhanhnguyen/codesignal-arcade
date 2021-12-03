def square_matrix(a):
    sum = 0
    for row in range(3):
        for col in range(3):
            sum += a[row][col]
    return sum // 9


def solution(image):
    r = len(image)
    c = len(image[0])
    new_image = []
    rowp, colp = 0 , 0 
    square, square_row, new_row = [], [], []
    while (rowp <= r - 3):
        while (colp <= c - 3):
            for row in range(rowp, rowp + 3):
                for col in range(colp, colp + 3):
                    square_row.append(image[row][col])
                square.append(square_row)
                square_row = []
            
            # print(len(square))
            new_row.append(square_matrix(square))
            # print(new_row)
            
            square = []
                
            colp += 1
                
                                
        new_image.append(new_row)
        # print(new_image)
        new_row = []
        rowp += 1 
        colp = 0 
    return new_image





