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


def binary_search_using_recursion(lst, n, start, end):
    if start > end:
        return -1

    mid = (start+end)//2

    if lst[mid] > n:
        return binary_search_using_recursion(lst, n, start, mid-1)
    elif lst[mid] < n:
        return binary_search_using_recursion(lst, n, mid+1, end)
    else:
        return mid


# Driver code
'''
binary_search([], 1)
binary_search([1, 2, 3, 4, 5], 3)
binary_search([4, 25, 55, 63, 68, 36, 44], 68)

or 

binary_search_using_recursion([],1,0,-1)
binary_search_using_recursion([1, 2, 3, 4, 5], 3,0,4)
binary_search_using_recursion([4, 55, 25, 63, 68, 36, 44], 68,0,6)
'''
