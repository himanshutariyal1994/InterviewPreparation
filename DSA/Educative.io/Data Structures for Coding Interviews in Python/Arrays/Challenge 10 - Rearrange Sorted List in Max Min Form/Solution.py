'''
Using extra space - rearrangement in a new array
Time complexity : O(N)
Space complexity : O(N)
'''


def max_min(lst):
    if not lst or len(lst) == 0:
        return None

    result, n = [], len(lst)//2

    for i in range(0, n):
        result.append(lst[~i])
        result.append(lst[i])

    if len(lst) % 2 == 1:
        result.append(lst[n])

    return result


'''
Optimal solution : rearrangement in place
Time complexity : O(N)
Space complexity : O(1)

Use Euclid's Theorem : a = qb + r
'''


def max_min_2(lst):
    if not lst or len(lst) == 0:
        return None

    len_lst = len(lst)
    max_index, min_index, max_ele = len_lst - 1, 0, lst[-1] + 1

    for index in range(len_lst):
        if index % 2 == 0:
            lst[index] += (lst[max_index] % max_ele) * max_ele
            max_index -= 1
        else:
            lst[index] += (lst[min_index] % max_ele) * max_ele
            min_index += 1

    for index in range(len_lst):
        lst[index] //= max_ele

    return lst


max_min_2([1, 2, 3, 4, 5, 6, 7])
