def next_bigger(n):
    # Number to list
    list = [x for x in str(n)]
    # Iterate list backwards
    for i in range(len(list) - 2, -1, -1):
        # first list[i] item that bigger than previous
        if list[i] < list[i + 1]: 
            # next smaller than list[i] digit in the right side of list
            temp_min = min([x for x in list[i + 1:] if x > list[i]])
            temp_min_ind = list[i + 1:].index(temp_min)
            # Switch list[i] and next smaller
            list[i], list[i + 1 + temp_min_ind] = list[i + 1 + temp_min_ind], list[i]
            # Sort right side descending
            list[i + 1:] = sorted(list[i + 1:])
            # Test whether first digit isnt 0
            if list[0] != "0":
                # Return integer
                return int("".join(list))
    return -1


print(next_bigger(59884848459853))

'''
59884848459853
59884848483559
'''

