'''
* Time Complexity: O(N^2)
* Space Complexity: O(1)
'''


def selection_sort(lst):
    lst_len = len(lst)
    for i in range(lst_len):
        mid = i

        for j in range(i+1, lst_len):
            if lst[j] < lst[mid]:
                mid = j

        if mid != i:
            lst[i], lst[mid] = lst[mid], lst[i]

    return lst


# Driver code
'''
selection_sort([])
selection_sort([731, 22, 53, 14, 255])
selection_sort([352, 6252, 122, 3272, 3262, 22, 353])
'''
