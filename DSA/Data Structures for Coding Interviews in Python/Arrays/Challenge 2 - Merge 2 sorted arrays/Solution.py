import array

'''
Using a new array
Time Complexity : O(n+m)
Space Complexity : O(n+m)
'''


def merge_lists(lst, lst2):
    i = 0
    j = 0
    arr = array.array('i', [])

    while i < len(lst) and j < len(lst2):
        if lst[i] < lst2[j]:
            arr.append(lst[i])
            i += 1
        else:
            arr.append(lst2[j])
            j += 1

    if i < len(lst):
        arr.extend(lst[i:])

    if j < len(lst2):
        arr.extend(lst2[j:])

    return arr.tolist()


'''
Not Using a new array
Time Complexity: O(m(n+m)
Space Complexity: O(1)
'''


def merge_lists(lst, lst2):
    i = 0
    j = 0

    while i < len(lst) and j < len(lst2):
        if lst[i] > lst2[j]:
            lst.insert(i, lst2[j])
            i += 1
            j += 1
        else:
            i += 1

    if j < len(lst2):
        lst.extend(lst2[j:])

    return lst
