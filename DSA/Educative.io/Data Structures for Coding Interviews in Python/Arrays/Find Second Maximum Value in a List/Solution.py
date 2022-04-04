# Brute force approach
'''

def find_second_maximum(lst):
    if (not lst or len(lst) < 2):
        return -1

    lst.sort()
    return lst[-2]
'''

# Optimal approach


def find_second_maximum(lst):
    if not lst or len(lst) < 2:
        return -1

    first_max = float("-inf")  # or use -math.inf
    second_max = float("-inf")

    for num in lst:
        if first_max < num:
            second_max = first_max
            first_max = num
        elif second_max < num and num != first_max:
            second_max = num

    return second_max
