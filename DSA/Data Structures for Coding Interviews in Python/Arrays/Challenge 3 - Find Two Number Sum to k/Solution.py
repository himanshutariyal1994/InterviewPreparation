'''
Time Complexity: O(N)
Space Complexity: O(N)
'''


def find_sum(lst, k):
    dict = set()

    for num in lst:
        if num in dict:
            return [num, k-num]
        dict.add(k-num)
    return None
