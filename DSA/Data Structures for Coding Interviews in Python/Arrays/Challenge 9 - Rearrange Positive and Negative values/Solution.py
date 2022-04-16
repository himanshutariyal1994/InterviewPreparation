'''
Using extra space - non optimal solution
Time complexity: O(N)
Space complexity: O(N)
'''


def rearrange(lst):
    if not lst or len(lst) == 0:
        return lst

    neg_nums, pos_nums = [], []

    for num in lst:
        if num > 0:
            pos_nums.append(num)
        else:
            neg_nums.append(num)

    return neg_nums + pos_nums


'''
Optimal solution - rearranging in place
Time complexity: O(N)
Space complexity: O(1)
'''


def rearrange(lst):
    if not lst or len(lst) == 0:
        return lst

    left_pos_index = 0

    for i in range(0, len(lst)):
        if lst[i] < 0:
            if left_pos_index != i:
                lst[i], lst[left_pos_index] = lst[left_pos_index], lst[i]
            left_pos_index += 1

    return lst
