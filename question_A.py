def check_for_overlap(line_1, line_2):
    for num_point in line_2:
        if num_point in xrange(line_1[0], line_1[1]):
            return 'Both lines overlap!'
            break
        else:
            return 'Lines do not overlap!'
            break


line_1 = [1, 4]
line_2 = [5, 6]

print(check_for_overlap(line_1, line_2))
