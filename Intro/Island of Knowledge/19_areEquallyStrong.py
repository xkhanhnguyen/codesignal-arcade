def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return sorted([yourLeft,yourRight]) == sorted([friendsLeft,friendsRight])
    # you = sorted([yourLeft, yourRight])
    # friend = sorted([friendsLeft,friendsRight])
    
    # if you == friend:
    #     return True
    # else:
    #     return False
