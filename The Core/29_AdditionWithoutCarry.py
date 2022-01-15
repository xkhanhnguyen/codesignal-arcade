"""
A little child is studying arithmetic. They have just learned how to add two integers, 
written one below another, column by column. But the child always forgets about 
the important partcarrying.

Given two integers, your task is to find the ans that the child will get.

Note: The child had learned from this site, so feel free to check it out too if 
you are not familiar with column addition.

Example

For param1 = 456 and param2 = 1734, the output should be
solution(param1, param2) = 1180.

   456
  1734
+ ____
  1180
The child performs the following operations from right to left:

6 + 4 = 10 but the child forgets about carrying the 1 and just writes down the 0 in the last column
5 + 3 = 8
4 + 7 = 11 but the child forgets about the leading 1 and just writes down 1 under 4 and 7.
There is no digit in the first number corresponding to the leading digit of the second one, 
so the child imagines that 0 is written before 456. Thus, they get 0 + 1 = 1.

"""
def solution(param1, param2):
    # convert int to str
    param1 = str(param1)
    param2 = str(param2)
    
    # add 0 to the left of the number if not the same length
    length = max(len(param1), len(param2))
    str1 = param1.rjust(length, '0')
    str2 = param2.rjust(length, '0')
    ans = ''

    
    for i in range(length):
        ans += str(int(str1[i])+ int(str2[i]))[-1]
        
    return int(ans)
    
print(solution(456, 1734))
