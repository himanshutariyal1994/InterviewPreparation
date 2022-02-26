import enum


'''
Time Complexity : O(N) since it iterates over the length of the list
Space Complexity : O(1)
'''


def linear_search(lst, n):
    index = -1
    if not lst or len(lst) == 0:
        return index

    for i, num in enumerate(lst):
        if num == n:
            return i

    return index


# Driver code
'''
linear_search([],1)
linear_search([1,2,3,4,5],3)
linear_search([4,55,25,63,68,36,44],68)
'''
