def evaluate(expression):
    final_result = 0
    action = '+'
    pointer = 0

    for index in range(0, len(expression)):
        if index == pointer:
            item = expression[pointer]
        if item in ('+', '-'):
            action = item
        elif item.isdigit():
            if action == '-':
                final_result -= int(item)
            else:
                final_result += int(item)
        elif item == '(':
            pointer += 1
        elif item == ')':
            return final_result
    
    return final_result


print(evaluate('- (3 + ( 2 - 1 ) )'))
        
