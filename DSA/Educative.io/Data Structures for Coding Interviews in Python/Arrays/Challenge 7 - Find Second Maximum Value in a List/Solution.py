'''
Brute force approach
Time complexity: O(N log N)
Spaxe Complexity: O(1)

def find_second_maximum(lst):
    if (not lst or len(lst) < 2):
        return -1

    lst.sort()
    return lst[-2]
'''

# Optimal approach
'''
Time complexity: O(N)
Space complexity: O(1)
'''


def find_second_maximum(lst):
    if len(lst) <= 1 or not lst:
        return None

    max_ele, second_max = float('-inf'), float('inf')
    for num in lst:
        if num > max_ele:
            second_max = max_ele
            max_ele = num
        elif num > second_max and num != max_ele:
            second_max = num

    return second_max
