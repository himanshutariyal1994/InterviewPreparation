'''
Time Complexity : O(N)
Space Complexity : O(1)
'''


def find_minimum(lst):
    if len(lst) == 0 or lst is []:
        return None

    min = lst[0]

    for num in lst:
        if min > num:
            min = num

    return min
