def unique_pairs(input_list, k):

    pairs = []

    for x in range(0, len(input_list)-1):
        sub_result = k - input_list[x]

        if sub_result in input_list[x:]:
            print (input_list[x], sub_result)
    



unique_pairs([1, 3, 2, 5, 46, 6, 7, 4], 5)