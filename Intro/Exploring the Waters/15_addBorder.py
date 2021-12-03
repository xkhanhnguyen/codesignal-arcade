def solution(picture):
    total = len(picture[0]) + 2
    output = []
    temp = ""
    for i in range(total):
        temp += '*'
    output.append(temp)
    for i in range(len(picture)):
        output.append('*' + picture[i] + '*')
    output.append(temp)
    return output