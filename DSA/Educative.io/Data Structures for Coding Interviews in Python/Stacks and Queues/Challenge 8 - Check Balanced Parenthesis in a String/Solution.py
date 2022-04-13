'''
This is a simple algorithm. We iterate over the string, one character at a time. Whenever we find a closing parenthesis, we can deduce that the 
string is unbalanced based on two conditions:

a. The stack is empty.
b. The top element in the stack is not an opening parenthesis of the same type.

If any of these conditions are True, we return False. If a parenthesis in the string is an opening parenthesis, it is simply pushed into the stack.
 If all the parentheses are balanced, the stack should be empty by the end because we pop every opening parenthesis once its closing parenthesis 
 is found. In the end, if stack is not empty, we return False.

Time complexity : O(N) where N is the length of the string
'''


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


def is_balanced(exp):
    # initialise a stack instance
    stack = MyStack()

    # Store the opening parenthesis in a list
    opening_paren_list = ['{', '[', '(']

    # Store the parenthesis pair in a list
    parenthesis_pair = ['{}', '()', '[]']

    for paren in exp:
        # if the parenthesis is a opening one, push it on top of stack
        if paren in opening_paren_list:
            stack.push(paren)
        else:
            # If the stack is empty, return False since there is no balancing opening parenthesis
            if stack.is_empty():
                return False

            # Pop the opening parenthesis from stack and check whether it balances or not.
            # If not, return False else continue
            opening_paren = stack.pop()
            if opening_paren + paren not in parenthesis_pair:
                return False

    # This indicates that the parenthesis were balanced, so return True
    return stack.is_empty()


# Testing driver code
print(is_balanced('{[()]}'))  # True
print(is_balanced('[{}]'))  # True
print(is_balanced('[{(}]'))  # False
print(is_balanced('({[}])'))  # False
print(is_balanced(''))  # True
