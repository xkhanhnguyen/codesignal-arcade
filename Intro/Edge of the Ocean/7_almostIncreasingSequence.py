# def solution(sequence):
#     temp = 0
#     # print(temp)
#     for i in range(len(sequence)-1):
#         if sequence[i+1] <= sequence[i]:
#             print(sequence[i+1], sequence[i])
#             temp += 1
#             # del sequence[i+1]
            
#         # sequence = sequence.pop(i+1)
#         #     print('here1', temp)
#         # else:
#         #     for j in range(i+1, len(sequence)-1):
                
#         #         if sequence[j+1] <= sequence[i]:
#         #             temp += 1
#         #             break
                
#             # print(temp, 'compare', sequence[i], 'index-i=', i , '--', sequence[j],'indexj=', j)
                        
         
#     if temp >1 :
#         print('temp', temp)
#         return False
#     else:
#         return True
        
def almostIncreasingSequence(sequence):
    removeCount = 0
    if sequence[0] >= sequence[1]:
        removeCount += 1
    i = 2
    while i < len(sequence):
        if sequence[i - 1] >= sequence[i]:
            removeCount += 1
            if sequence[i - 2] >= sequence[i]:
                sequence[i] = sequence[i - 1]
        i += 1
    return (removeCount < 2)

