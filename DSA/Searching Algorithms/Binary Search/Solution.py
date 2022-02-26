'''
* Time Complexity: O(log N) since it divides the array in half for each pass
* Space Complexity: O(1)
* The array should be sorted to perform binary search - -> O(N log N) for sorting array
'''


def binary_search(lst, n):
    # Assuming list is sorted in ascending order
    index = -1
    if not lst or len(lst) == 0:
        return index

    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] > n:
            end = mid - 1
        elif lst[mid] < n:
            start = mid + 1
        else:
            return mid

    return index


# Driver code
'''
binary_search([], 1)
binary_search([1, 2, 3, 4, 5], 3)
'''
