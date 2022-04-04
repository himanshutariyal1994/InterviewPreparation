def find_product(arr):
    result = []
    left_side = 1
    right_side = 1

    for i in range(0, len(arr)):
        result.append(right_side)
        right_side *= arr[i]

    for i in range(len(arr)-1, -1, -1):
        result[i] *= left_side
        left_side *= arr[i]

    return result
