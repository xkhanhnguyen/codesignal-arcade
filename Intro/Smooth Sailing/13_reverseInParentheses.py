# def reverseInParentheses(s):
#     stack = []
#     for x in s:
#         if x == ")":
#             tmp = ""
#             while stack[-1] != "(":
#                 tmp += stack.pop()
#                 print(tmp)
#             stack.pop() # pop the (
#             for item in tmp:
#                 stack.append(item)
#                 print(stack)
#         else:
#             stack.append(x)

#     return "".join(stack)

def reverseInParentheses(s):
    stack = []
    for elem in s:
        if elem == ")":
            temp = ""
            while stack[-1] != "(":
                temp += stack.pop()
            stack.pop()
            
            for item in temp:
                stack.append(item)
        else:
            stack.append(elem)
            
    return "".join(stack)