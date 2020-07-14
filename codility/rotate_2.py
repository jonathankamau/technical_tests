def solution(a,k):

    result = [None] * len(A)

    for i in range(len(A)):
        result[(i + k) % len(A)] = A[i]
    
    return result

    # if len(A) == 0:
    #     return []
    # if len(A) == 1:
    #     return A

    # while k != 0:
    #     temp = a.pop()
    #     a.insert(0, temp)
    #     k -= 1

    # return a

A = [5,3,4,1,2]
print(solution(A,2))

        
