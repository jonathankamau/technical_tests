

def solution(A):

    A.sort()
    
    if len(A) == 1:
        return A[0]
    for index in range(len(A)-1, 0, -2):
        if A[index] != A[index-1]:
            return A[index]
    

A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))