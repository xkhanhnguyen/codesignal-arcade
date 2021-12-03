""" 
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.

"""


def solution(n):
    n = str(n)
    temp = []
    for i in range(len(str(n))):
        if int(n[i]) % 2 == 0:
            temp.append(n[i])
        
    return len(temp) == len(n)


print(solution(248622))
print(solution(642386))