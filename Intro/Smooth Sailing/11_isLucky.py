def solution(n):
    a_string = str(n)
    sum1, sum2 = 0, 0
    half = int(len(a_string)/2)
    # print(half)
    for i in range(len(a_string)):
        for e1 in range(0, half):
            sum1 += int(a_string[e1])
           
        for e2 in range(half, len(a_string)):
            # print(a_string[e2])
            sum2 += int(a_string[e2])
    if sum1 == sum2:
        return True
    else:
        return False
    