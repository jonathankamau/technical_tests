def solution(A):

    # O(N log N or O(N) time)

    B = sorted(A)
    

    midpoint = len(B) // 2

    for i in range(len(A)-1):

        if B[midpoint] == A[i] and (B[i-1] | B[i+1]) == A[i]:
            return i
    
    return -1

    consecutive_size = 0
    candidate = 0

    for item in A:
        if consecutive_size == 0:
            candidate = item
            consecutive_size += 1
        elif candidate == item:
            consecutive_size += 1
        else:
            consecutive_size -= 1
    occurrence = A.count(candidate)

    if occurrence > (len(A)/2):
        return A.index(candidate)
    else:
        return -1

print(solution([2,4,3,3,3,2,3]))
print(solution([3,4,3,2,3,-1,3,3]))
print(solution([]))
print(solution([1,2,3,4,5]))
print(solution([2,2]))
print(solution([4,4,4,4]))