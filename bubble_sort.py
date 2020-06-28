def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
                unsorted_until_index = unsorted_until_index - 1


list = [65, 55, 45, 35, 25, 15, 10] 
bubble_sort(list)
print list

"""
In a worst-case scenario, where the array is not just randomly shuffled, but sorted in descending order 
(the exact opposite of what we want), we’d actually need a swap for each comparison. 
So we’d have ten comparisons and ten swaps in such a scenario for a grand total of twenty steps.
If you look precisely at the growth of steps as N increases, you’ll see that it’s growing by approximately N2.
Therefore, in Big O Notation, we would say that Bubble Sort has an efficiency of O(N2).
"""
