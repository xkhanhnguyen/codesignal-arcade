def solution(a, b):
    if a==b:
        return True
    
    i = 0
    while i < len(a):
        if a[i]==b[i]:
            a.pop(i)
            b.pop(i)
        else:
            i +=1
    if len(a) != 2:
        return False
    b.reverse()
    if a == b:
        return True
    else:
        return False



 