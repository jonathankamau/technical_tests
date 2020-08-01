def staircase(n):
    first, second = 1,1

    for index in range(n):
        first, second = second, first + second
    
    return first

# Test Cases
print(staircase(4))
# 5
print(staircase(5))
# 8