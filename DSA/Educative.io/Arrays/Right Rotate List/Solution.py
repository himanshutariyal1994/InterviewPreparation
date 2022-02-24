def right_rotate(arr, k):
    if not arr or len(arr) == 0:
        return arr
    else:
        k = k % len(arr)

    return arr[-k:] + arr[:-k]
