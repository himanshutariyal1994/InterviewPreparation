'''
Time Complexity: O(N)
Space Complexity: O(N
'''
# using list comprehension


def remove_even(lst):
    return [number for number in lst if number % 2 != 0]


# using normal logic
def remove_even(lst):
    odd_numbers = []

    for num in lst:
        if num % 2 != 0:
            odd_numbers.append(num)

    return odd_numbers
