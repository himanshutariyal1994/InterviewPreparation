'''
Using space optimised prefix and suffix products
Time Complexity: O(N)
Space Complexity: O(N)
'''


def find_product(arr):
    n, ans, suffix_prod = len(arr), [1]*len(arr), 1
    for i in range(1, n):
        ans[i] = ans[i-1] * arr[i-1]
    for i in range(n-1, -1, -1):
        ans[i] *= suffix_prod
        suffix_prod *= arr[i]
    return ans


'''
Using space optimised prefix and suffix products in one pass
Time Complexity: O(N)
Space Complexity: O(N)
'''


def find_product(arr):
    ans, suf, pre = [1]*len(arr), 1, 1
    for i in range(len(arr)):
        ans[i] *= pre               # prefix product from one end
        pre *= arr[i]
    ans[-1-i] *= suf            # suffix product from other end
    suf *= arr[-1-i]
    return ans
