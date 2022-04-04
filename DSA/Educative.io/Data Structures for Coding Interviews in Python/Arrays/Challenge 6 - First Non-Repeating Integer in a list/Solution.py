'''
Time complexity: O(N)
Space complexity: O(N)
'''


def find_first_unique(arr):
    dict = {}

    for num in arr:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    for item in arr:
        if dict[item] == 1:
            return item
    return None
