def solution(statues):

    statues.sort()
    print(statues)
    output = 0
    for i in range(len(statues)-1):
        output = output + statues[i+1] - statues[i] - 1
        print(output)
    return output
