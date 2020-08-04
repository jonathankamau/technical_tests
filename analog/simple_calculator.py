def evaluate(expression):
    final_result = 0
    stack = []
    current_operand = 0
    num = 1
   

    for index in range(len(expression)):
        item = expression[index]
        if item.isdigit():
            current_operand = int(item)
            continue
        stack.append(num * current_operand)
        current_operand = 0
        if item == '-':
            num = -1
        elif item == '+':
            num = 1
        elif item == '(':
            if num == 1:
                stack.append('+')
            else:
                stack.append('-')
            num = 1
        elif item == ')':
            tmp_num = 0
            while stack[-1] != '+' and stack[-1] != '-':
                tmp_num += stack.pop()
            if stack[-1] == '-':
                tmp_num = -tmp_num
            stack.pop()
            stack.append(tmp_num)
    
    if current_operand != 0:
        stack.append(num * current_operand)
    while stack:
        final_result += stack.pop()


    return final_result


print(evaluate('- (3 + ( 2 - 1 ) )'))
        
