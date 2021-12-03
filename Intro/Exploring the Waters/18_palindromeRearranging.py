def solution(inputString):
    # temp = []
    temp = {i:inputString.count(i) for i in inputString}
    count_value, count_key = 0, 0
    for key,value in temp.items():
        if value %2 != 0:
            count_value +=1
        else:
            count_key +=1
    
    if count_value == 0 or count_value == 1:
        return True
    else:
        return False
     
    # if count_key % 2 == 0 and count_key != 0:
    #     print(count_key, 'key')
    #     return True  
    # if count_value == 1 and len(inputString) % 2 !=0:
    #     return True   
    # if count_value > 1:
    #     print(count_value, 'value')
    #     return False
    

