def solution(inputString):
    temp = inputString.split(".")
    if len(temp) != 4:
        return False
            
    for i in temp:
        if not i.isdigit(): 
            return False
        if i[0] == '0' and len(i) > 1:
            return False
        if int(i) not in range(256):
            return False
    return True
       
