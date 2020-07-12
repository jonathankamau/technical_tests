def solution(N,A):

    start_line = 0
    counter = [start_line] * N
    var_max = 0

    for i in A:
        if i > N:
            start_line = var_max
        elif counter[i-1] < start_line:
            counter[i-1] = start_line + 1
        else:
            counter[i-1] += 1
        if i < N and counter[i-1] > var_max:
            var_max = counter[i-1]

    for i in range(len(counter)):
        if counter[i] < start_line:
            counter[i] = start_line
    
    return counter

N = 5
A = [3,4,4,6,1,4,4]
print(solution(N,A))