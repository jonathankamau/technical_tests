def solution(A):

    # total_passes = 0
    # total = 0
    
    # # My initial solution
    # for i in range(len(A)):
    #     if A[i] == 0:
    #         total += A[i:].count(1)
    
    # return total_passes

    # My improved solution
    # suffix_sum = []
    # total = 0
    # passes = 0
    # suffix_sum.append(total)

    # for i in range(len(A)-1, -1, -1):

    #     total += A[i]
    #     suffix_sum.append(total)
    
    # suffix_sum.reverse()

    

    # for i in range(len(A)):

    #     if A[i] == 0:
    #         passes += suffix_sum[i]
    
    # return passes

# Solution from course

    suffix_sum = [0] * (len(A) + 1) 
    passes = 0

    for i in range(len(A)-1, -1, -1):
        suffix_sum[i] = A[i] + suffix_sum[i+1]
        if A[i] == 0:
            passes += suffix_sum[i]
        if passes > 1000000000:
            return -1
    
    return passes

print(solution([0,1,0,1,1]))