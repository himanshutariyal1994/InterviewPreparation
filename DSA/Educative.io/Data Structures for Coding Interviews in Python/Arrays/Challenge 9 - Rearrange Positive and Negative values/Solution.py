def rearrange(lst):
    if not lst or len(lst) == 0:
        return lst

    left_pos_index = 0

    for i in range(0, len(lst)):
        if lst[i] < 0:
            lst[i], lst[left_pos_index] = lst[left_pos_index], lst[i]
            left_pos_index += 1

    return lst
