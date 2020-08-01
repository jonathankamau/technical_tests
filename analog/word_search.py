def word_search(matrix, word):
    word_list = list(word)
    word_list.reverse()

    for item_list_index in range(0, len(matrix), 1):
        print(matrix[item_list_index])
        for item in matrix[item_list_index]:
            if word_list:
                if item == word_list[-1]:
                    word_list.pop()

    return True if len(word_list) == 0 else False



 # Test Case.
matrix = [
 ['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

print(word_search(matrix, 'FOAM'))
# True