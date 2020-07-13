def solution(A):

    # Using Kandane's Algorithm
    # My initial solution

    # B = []

    # for i in range(len(A)-1):
    #     B.append(A[i+1] - A[i])

    # global_max = B[0]
    # local_max = B[0]

    # for i in range(1,len(B)):
    #     sum_items = B[i] + local_max
    #     if B[i] < sum_items:
    #         local_max = sum_items
    #     if B[i] > sum_items:
    #         local_max = B[i]
            
    #     if global_max < local_max:
    #         global_max = local_max
    
    # return global_max

    # Optimum Solution

    global_max = 0
    local_max = 0

    for i in range(1, len(A)):
        d = A[i] - A[i-1]
        local_max = max(d, local_max + d)
        global_max = max(local_max, global_max)
    return global_max

# print(solution([5,-4,8,-10,-2,4,-3,2,7,-8,3,-5,3])) 
print(solution([114,132,119,91,84,29,61,76,38,21,9,63,45,68,81,124,118,78,44,59,80])) 