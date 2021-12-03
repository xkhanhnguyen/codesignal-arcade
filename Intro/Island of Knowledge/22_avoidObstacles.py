def solution(inputArray):
    a = sorted(inputArray)
    # print(a)
    step = 1
    obs = True
    while (obs):
        obs = False
        step += 1
        for i in range(len(a)):
            if a[i] % step == 0:
                obs = True
                break
    return step
            
    

