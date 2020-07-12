def solution(A,B):

    
    if len(A) | len(B) == 0:
        return 0
    
    # Brute Force Approach
    # for i in range(0,len(A)-1):
    #     for x in  range(0, len(B)):
    #         if A[i] == B[x]:
    #             return A[i]
    # return 0

    pointer_x = 0
    pointer_y = 0
    list_x = []

    list_length = len(A) - 1
    A.sort()
    B.sort()

    
    while pointer_x < list_length:
        if A[pointer_x] == B[pointer_y]:
            list_x += [A[pointer_x]]
            pointer_x += 1
            pointer_y += 1
        elif A[pointer_x] != B[pointer_y]:
            pointer_x += 1
        else:
            return 0
    return list_x


A = [3,1,4,2,7]
B = [8,2,5,4,6]

print(solution(A,B))