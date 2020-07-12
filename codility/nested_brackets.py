def solution(S):
    valid = True
    stack = []

    for i in S:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        if i == ')':
            valid = False if not stack or stack.pop() != '(' else valid
        elif i == ']':
            valid = False if not stack or stack.pop() != '[' else valid
        elif i == '}':
            valid = False if not stack or stack.pop() != '{' else valid
    
    if len(stack) > 0:
        valid = False
    
    return 1 if valid == True else 0
         




S = "{{{{"
print(solution(S))