def solution(s1, s2):

    count = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                print( i, j)
                
                count +=1
                s2 = s2.replace(s2[j],"",1)
                break
            
    return count