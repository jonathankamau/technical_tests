def solution(a,k):

    result = [None] * len(A)

    for i in range(len(A)):
        result[(i + k) % len(A)] = A[i]
    
    return result

A = [5,3,4,1,2]
print(solution(A,2))

        
