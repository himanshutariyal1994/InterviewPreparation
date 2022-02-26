'''
* Time Complexity: O(N^2)
* Space Complexity: O(1)
'''


def bubble_sort(lst):
    lst_len = len(lst)
    for i in range(lst_len):
        for j in range(0, lst_len-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


print(bubble_sort([352, 6252, 122, 3272, 3262, 22, 353]))

# Driver code
'''
bubble_sort([])
bubble_sort([731, 22, 53, 14, 255])
bubble_sort([352, 6252, 122, 3272, 3262, 22, 353])
'''
