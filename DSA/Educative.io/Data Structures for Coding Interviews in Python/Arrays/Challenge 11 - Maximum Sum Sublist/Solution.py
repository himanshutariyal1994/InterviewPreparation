'''
Brute force approach
Time complexity : O(N^2)
Space complexity : O(1)
'''


def find_max_sum_sublist(lst):
    global_max = float('-inf')
    for i in range(len(lst)):
        cur_sum = 0
        for j in range(i, len(lst)):
            cur_sum += lst[j]
            global_max = max(global_max, cur_sum)
    return global_max


'''
Use Kadane's algorithm for obtaining the sub-optimal sum. This algorithm takes a dynamic
programming approach to solve the maximum sublist sum problem.

The basic idea of Kadane’s algorithm is to scan the entire list and at each position find
the maximum sum of the sublist ending there. This is achieved by keeping a current_max for
the current list index and a global_max.

The algorithm is as follows:

current_max = A[0]
global_max = A[0]
for i = 1 -> size of A
    current_max = max (A[i], current_max+A[i])
    global_max = max(global_max, local_max)


Time Complexity : O(N)
Space Complexity : O(1)
'''


def find_max_sum_sublist(lst):
    if not lst or len(lst) == 0:
        return None

    local_max, global_max = 0, float('-inf')

    for num in lst:
        local_max = max(num, local_max+num)
        global_max = max(local_max, global_max)

    return global_max


lst = [-4, 2, -5, 1, 2, 3, 6, 22, -3, 445, -5, 1]
print("Sum of largest subarray: ", find_max_sum_sublist(lst))
print("Sum of largest subarray2: ", find_max_sum_sublist([-4, -2, 0, 5, -5]))
