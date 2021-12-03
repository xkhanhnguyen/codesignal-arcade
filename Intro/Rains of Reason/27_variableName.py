""" 
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
solution(name) = true;
For name = "qq-q", the output should be
solution(name) = false;
For name = "2w2", the output should be
solution(name) = false.

"""

def solution(name):
    if name[0].isdigit():
        return False 
        
    else:
        for i in name:
            if not (i.isalnum() or i == '_'):

                return False
        return True

 # isalnum() checks whether a string contains only letters or numbers or both       

    
print(solution("var_1__Int"))
print(solution("qq-q"))
print(solution("2w2"))