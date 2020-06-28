def insertion_sort(array):
    for index in range(1, len(array)):
        position = index
        temp_value = array[index]
        while position > 0 and array[position - 1] > temp_value:
            array[position] = array[position - 1]
            position = position - 1
            array[position] = temp_value

"""
During the first passthrough, in which temp_value is the value at index 1, a maximum of one comparison is made, since there is only one value to the left of the temp_value. On the second passthrough, a maximum of two comparisons are made, and so on and so forth. On the final passthrough, we need to compare the temp_value with every single value in the array besides temp_value itself. In other words, if there are N elements in the array, a maximum of N - 1 comparisons are made in the final passthrough.



"""
