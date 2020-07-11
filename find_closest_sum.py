def solution(A,B,num):

    A.sort()
    B.sort()

    result = []
    if len(A) | len(B) == 0:
        return 0

    diff = abs(num - (A[-1] + B[-1]))
    x = -2
    print(diff)

    for i in range(len(A)-1,0,-1):
        for x in range(len(B)-1, 0, -1):
            alt_diff = abs(num - (A[i] + B[x]))
            print(alt_diff)
            if alt_diff < diff:
                diff = alt_diff
                result.append([A[i], B[x]])

    return result

A = [-1,3,8,2,9,5]
B = [4,1,2,10,5,20]
num = 24
print(solution(A,B,num))