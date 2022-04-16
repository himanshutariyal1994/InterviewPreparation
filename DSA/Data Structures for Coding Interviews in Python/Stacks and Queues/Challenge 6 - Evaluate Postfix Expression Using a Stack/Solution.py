'''
Here we simply check that if the token is an operator, we will pop 2 elements from the stack and post evaluating them, store the result back to the
stack. If it not an operator, simply push the element to the stack

Time complexity : O(N) where N is the length of the string
Space complexity: O(N) since we store stack in memory
'''


import math


class MyStack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)
        return self.stack_list[-1]

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


def evaluate_post_fix(exp):
    # initialise a stack instance
    stack = MyStack()

    # Create a list of all allowed operators
    operator_list = set('+-*/')

    # Create a dictionary of operator vs function
    operator_fn = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: x-y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x/y)
    }

    for char in exp:
        # if the character is a operator, extract the top 2 elements from stack and
        # perform the operation. Return None if the stack is empty or has less than
        # 2 numbers whenever we encounter a operator
        if char in operator_list:
            if stack.is_empty() or stack.size() < 2:
                return 0
            else:
                left = int(stack.pop())
                right = int(stack.pop())
                stack.push(int(operator_fn[char](right, left)))
        else:
            # This indiactes a number. push it on top of the stack
            stack.push(int(char))

    # The stack will have the final output calculated, so return it
    return stack.pop()


# Testing driver code
print(evaluate_post_fix('921*-8-4+'))  # 3
print(evaluate_post_fix('642/+'))  # 8
