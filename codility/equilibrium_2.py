def solution(a):

    list_length = len(a)-1
    
    p = sum(a) - a[0]
    v = 1
    X = a[0]

    diff = abs(X - p)

    if len(a) == 0:
        return 0
    
    while v <= list_length:
        X += a[v]
        p -= a[v]

        new_diff = abs(X - p)

        if new_diff < diff:
            diff = new_diff
        v += 1
        
    
    return diff



A = [1,1,3]
print(solution(A))