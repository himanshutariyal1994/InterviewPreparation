'''
Non-optimal approach involves creating a new stack to hold minimum value in the original stack.
When the end user pushed a value in the stack, we will check teh new min value to be pushed on top of the stack
Thus, when we call the min() function, it will always return the top of the min_items stack

Time complexity : O(1) where minimum value is getting called in constant time
Space complexity: O(N) since we are storing each node in a min item array as well
'''


class MinStack:
    # Constructor
    def __init__(self):
        self.list = []
        self.min_items = []

    def is_empty(self):
        return len(self.list) == 0

    def pop(self):
        # If stack is empty, return None
        if self.is_empty():
            return None

        # Return the last element of the list (min element)
        self.min_items.pop()
        return self.list.pop()

    # Pushes value into new stack
    def push(self, value):
        self.list.append(value)

        # Now check to push min value in stack on top of min_items stack
        if len(self.min_items) == 0 or self.min_items[-1] > value:
            self.min_items.append(value)
        else:
            self.min_items.append(self.min_items[-1])

    # Returns the topmost element in stack
    def top(self):
        if self.is_empty():
            return None

        return self.list[-1]

    # Returns minimum value from new stack in constant time
    def min(self):
        if self.is_empty():
            return None

        return self.min_items[-1]


'''
optimal approach involves creating a new variable to hold minimum value in the original stack in the tuple form.
When the end user pushed a value in the stack, it will push the min value to the second element in the added tuple node
Thus, when we call the min() function, it will always return the top of the min_items stack

Time complexity : O(1) where minimum value is getting called in constant time
Space complexity: O(N) since we are storing each node in a min item array as well
'''


class MinStack:
    # Constructor
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def pop(self):
        # If stack is empty, return None
        if self.is_empty():
            return None

        # Return the last element of the list
        return self.list.pop()[0]

    # Pushes value into new stack
    def push(self, value):
        min_value = value if self.is_empty() else self.list[-1][1]
        self.list.append((value, min(min_value, value)))

    # Get the topmost element in the stack
    def top(self):
        if self.is_empty():
            return None

        return self.list[-1][0]

    # Returns minimum value from new stack in constant time
    def min(self):
        if self.is_empty():
            return None

        return self.min_items[-1][1]
