'''
Manual rotation in Python using an extra array
Space complexity: O(N)
Time complexity: O(N)
'''


def right_rotate(arr, k):
    if len(arr) == 0 or not arr:
        return None

    k, result, n = k % len(arr), [], len(arr)

    for index in range(n-k, n):
        result.append(arr[index])

    for index in range(0, n-k):
        result.append(arr[index])
    return result


'''
Solution based on tricks in Python
Space complexity: O(N)
Time complexity: O(N)
'''


def right_rotate(arr, k):
    if len(arr) == 0 or not arr:
        return None

    k = k % len(arr)
    return arr[-k:] + arr[:-k]


'''
Reverse list k times 
Space complexity: O(1)
Time complexity: O(N)
'''


def right_rotate(arr, k):
    if len(arr) == 0 or not arr:
        return None

    n = len(arr)
    k = k % n

    arr = reverse(arr, 0, n-1)
    arr = reverse(arr, 0, k-1)
    arr = reverse(arr, k, n-1)
    return arr


def reverse(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr
