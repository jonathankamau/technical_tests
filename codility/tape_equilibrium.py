"""

"""

def solution(A):

    left = A[0]
    right = sum(A[1:])
    diff = abs(left - right)

    for i in range(1, len(A)):
        ldiff = abs(left - right)

        
        

        if ldiff < diff:
            diff = ldiff
        
        left += A[i]
        right -= A[i]

    return diff
    
#A = [3,1,2,4,3]
A = [1,1,3]
print(solution(A))