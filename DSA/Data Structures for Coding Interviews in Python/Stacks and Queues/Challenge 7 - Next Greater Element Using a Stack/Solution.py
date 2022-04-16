'''
Non-Optimal solution is Brute force where you iterate through each element and find the greatest element amongst the rightmost present elements

Time complexity: O(N^2) since each element will be iterated n times
Space complexity: O(N) since the result is stored in memory
'''


class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size

    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()


def next_greater_element(lst):
    len_lst = len(lst)
    result = [-1] * len_lst
    for index in range(0, len_lst):
        greatest_element = result[index]

        for j in range(index+1, len_lst):
            if lst[index] < lst[j]:
                greatest_element = lst[j]
                break

        result[index] = greatest_element

    return result


print(next_greater_element([4, 6, 3, 2, 8, 1, 9, 9, 9]))

'''
Optimal solution involves using a stack and checking the value with the topmost element in stack.

The outer for loop begins from the end of lst. In each iteration, the top of the stack is compared with the current element in lst. 
Whenever the current value in lst is larger than top, that value is the next greater element in the list.

The top is popped and the current element in the list is again compared with the new top of the stack in the inner while loop. 
This loop stops when the top of the stack is bigger than the element of the list or the stack becomes empty.

If the stack is empty, it implies that the current element in lst does not have a next greater element. 
Hence, its corresponding index in res would retain the value of -1.

If the stack is not empty, then the current element has a value larger than it. 
Hence, the top value will be assigned to the corresponding index in res.

Continuing this process, we end up with a list containing all the next greater elements for all indices of lst.

Time complexity: O(N) since this involves iterating over the elements once
Space complexity: O(N) since stack will be stored in memory
'''


def next_greatest_element_stack(lst):
    len_lst = len(lst)
    result = [-1] * len_lst
    stack = MyStack()

    for index in range(len_lst-1, -1, -1):
        while not stack.is_empty() and stack.peek() <= lst[index]:
            stack.pop()

        if not stack.is_empty():
            result[index] = stack.peek()

        stack.push(lst[index])

    return result


print(next_greatest_element_stack([4, 6, 3, 2, 8, 1, 9, 2, 7]))
print(next_greatest_element_stack([4, 6, 3, 2, 8, 1, 9, 9, 9]))
