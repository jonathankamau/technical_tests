def solution(X, A):

    listsize = len(A) - 1
    start_index = 0
    last_index = listsize

    

    if len(A) == 0:
        return -1

    while start_index <= last_index:
        n = (last_index + start_index) // 2
        if X == A[n]:
            return n
        if X < A[n]:
            last_index = n - 1
        else:
            start_index = n + 1
    return -1




    # for K in range(0,len(A)-1):
    #     if A[K] == X:
    #         return K
    
    # return -1

X = 1
A = [1]
print(solution(X,A))