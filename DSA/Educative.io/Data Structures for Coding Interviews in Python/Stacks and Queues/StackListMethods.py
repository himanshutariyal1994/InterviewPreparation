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
