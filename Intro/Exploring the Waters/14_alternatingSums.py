def solution(a):
    output = []
    team_1, team_2 =  [], []
    for i in range(len(a)):
        if i % 2 == 0:
            team_1.append(a[i])
        else:
            team_2.append(a[i])
    
    output.append(sum(team_1)) 
    output.append(sum(team_2))
    return output
        
        

