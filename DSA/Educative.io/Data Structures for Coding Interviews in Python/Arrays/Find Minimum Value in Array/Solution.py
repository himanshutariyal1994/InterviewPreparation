'''
Time Complexity : O(n)
Space Complexity : O(1)
'''


def find_minimum(lst):
    min = lst[0]

    for num in lst:
        if min > num:
            min = num

    return min
