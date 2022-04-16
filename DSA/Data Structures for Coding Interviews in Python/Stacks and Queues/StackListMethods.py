'''
Implementing Stack using a list
'''


from collections import deque


class StackList:
    def __init__(self):
        self.list = []

    # Return the size of stack
    def size(self):
        return len(self.list)

    # Check if the stack is empty
    def is_empty(self):
        return not self.list or len(self.list) == 0

    # print stack in list form
    def print_stack(self):
        print(f'Stack : {self.list}')

    # Return the top element of the stack
    def peek(self):
        return None if self.is_empty() else self.list[-1]

    # Remove the top element from stack
    def pop(self):
        if self.is_empty():
            return None

        return self.list.pop()

    # Push a new element to top of stack
    def push(self, value):
        self.list.append(value)
        return self.list[-1]


stack_inst = StackList()
print(f'Stack empty: {stack_inst.is_empty()}')

for i in range(1, 5):
    stack_inst.push(i)

stack_inst.print_stack()
print(f'Top element in stack at the moment: {stack_inst.peek()}')
print(f'Size of stack: {stack_inst.size()}')

print(f'Element popped from stack: {stack_inst.pop()}')
print(f'Element popped from stack: {stack_inst.pop()}')
print(f'Top element in stack now: {stack_inst.peek()}')
print(f'Size of stack now: {stack_inst.size()}')
print(f'Stack empty: {stack_inst.is_empty()}')


'''
Implementing Stacks using deque(). Import deque from the collections module
'''
stack = deque(
    [], maxlen=100)  # maxlen indicates the max elements that could be inserted in deque

# Pushing elements on stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# Pushing elements on the left end
stack.appendleft(0)
stack.appendleft(-1)
stack.appendleft(-2)

# Extending elements on the left end
stack.extendleft([-3, -4])
stack.extendleft([-5, -6])
stack.extendleft([-7, -8])

# Extending elements on the right end
stack.extend([5, 6, 7, 8])
stack.extend([9, 10])

# Printing stack values
print(stack)

# Removing elements from stack
print(stack.pop())  # 10
print(stack.pop())  # 9
print(stack.pop())  # 8

# Removing elements on the left end
print(stack.popleft())  # -8
print(stack.popleft())  # -7
print(stack.popleft())  # -6

# Print number of elements in stack
print(len(stack))  # 13

# Check if stack is empty
print(len(stack) == 0)
