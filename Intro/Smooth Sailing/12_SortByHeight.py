def solution(a):
    b = sorted([i for i in a if i!=-1]) # a temp array of sorted height
    p = 0
    for t in range(len(a)):
        if a[t] == -1:
            pass
        else:
            a[t] = b[p] # append the height
            p+=1
    return a
    

