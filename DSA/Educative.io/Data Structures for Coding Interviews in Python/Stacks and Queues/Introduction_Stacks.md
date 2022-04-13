# What is a Stack?

We are all familiar with the famous `Undo` option which exists in almost all popular applications. Ever wondered how that works? Well, you store the previous states of your work (which are limited to a specific number) in the memory in such an order that the last one appears first. You can’t really do this with simple lists very efficiently for reasons we will explore in the coming chapters. So this is where the `Stack` data structure comes in handy.

`Stacks` follow the `Last in First Out (LIFO)` ordering. This means that the **last element added is the element on the top and the first element added is at the bottom**.

A real-life example of Stack could be a stack of books. So, in order to get the book that’s somewhere in the middle, you will have to remove all the books placed at the top of it. Also, the last book you added to the stack of books is at the top!

<br/>

## What are Stacks Used for?

Despite the simple implementation stacks can be used to solve very **complex** problems. There are many famous algorithms such as `Depth First Search` and the `Expression Evaluation Algorithm`, which harness the functionality of Stacks. Stacks are used:

- To **backtrack** to the previous task/state, for example, in recursive code
- To store a **partially completed task**, for example, when you are exploring two different paths on a Graph from a point while figuring out the smallest path to the target.

<br/>

## How do Stacks work?

**Stacks** can be implemented in many ways, but a typical `Stack` must offer the following functionalities:

| Function        | What does it do?                               |
| --------------- | ---------------------------------------------- |
| `push(element)` | Inserts an element at the top                  |
| `pop()`         | Removes an element from the top and returns it |
| `peek()`        | Returns the top element of the stack           |
| `is_empty()`    | Returns a boolean True if the stack is empty   |
| `size()`        | Returns the size of the stack                  |

<br/>

## Implementing a stack

> In **Python**, you can use the pre-built `Stack` class by importing them into your program. However, implementing a `Stack` from scratch will allow us to truly master the ins and outs of the data structure.

> Stacks can be implemented using `Lists` or `Linked Lists` in Python. Each implementation has its own advantages and disadvantages. Here, however, we will show an implementation of stacks using `normal lists`.

### Implementing Stack using lists

```python
## Implementing a Custom Stack class using lists
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

for i in range(1,5):
  stack_inst.push(i)

stack_inst.print_stack()
print(f'Top element in stack at the moment: {stack_inst.peek()}')
print(f'Size of stack: {stack_inst.size()}')

print(f'Element popped from stack: {stack_inst.pop()}')
print(f'Element popped from stack: {stack_inst.pop()}')
print(f'Top element in stack now: {stack_inst.peek()}')
print(f'Size of stack now: {stack_inst.size()}')
print(f'Stack empty: {stack_inst.is_empty()}')
```

> The simple `Stack` class called `StackList` will consist of the member functions given above and a list called `list` that will hold all the elements of the stack.

> The `is_empty`() function checks whether the stack is empty or not. If the length of the array is 0, then the function will return **True**. Otherwise, it will return **False**.

> The `peek()` function returns the last element in the list, which we are considering to be the top of the stack. **In case of an empty stack_list, it would return None.**

> The `size()` method simply returns the number of elements in the stack.

> The `push(value)` method simply adds the value to the end of the list or in case of a stack, at the top of it.

> The `pop()` method will remove the last element of list or the top element of stack and return it to the calling function

<br/>

### Implementing Stack using deque (Double Ended Queue)

> Here, however, we will show an implementation of stacks using `deque` or `doubled ended queue` present in the `collections` module in Python.

```python
# Implementing Stack using deque()
# For more methods refer to: https://www.geeksforgeeks.org/deque-in-python/

from collections import deque
stack = deque(
    [], maxlen=100)  # maxlen indicates the max elements that could be inserted in deque

# Pushing elements on stack on the rear end
# Time complexity : O(1)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# Pushing elements on the front end
# Time complexity : O(1)
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

# Removing elements from the rear end in stack
# Time complexity : O(1)
print(stack.pop())  # 10
print(stack.pop())  # 9
print(stack.pop())  # 8

# Removing elements from the left end in stack
# Time complexity : O(1)
print(stack.popleft())  # -8
print(stack.popleft())  # -7
print(stack.popleft())  # -6

# Print number of elements in stack
print(len(stack))  # 13

# Check if stack is empty
print(len(stack) == 0)
```

<br/>

## Complexities of Stack Operations

### Using lists

| Operation       | Time Complexity |
| --------------- | --------------- |
| `push(element)` | O(1)            |
| `pop()`         | O(1)            |
| `peek()`        | O(1)            |
| `is_empty()`    | O(1)            |
| `size()`        | O(1)            |

### Using deque

| Operation             | Time Complexity |
| --------------------- | --------------- |
| `append(element)`     | O(1)            |
| `pop()`               | O(1)            |
| `appendleft(element)` | O(1)            |
| `popleft()`           | O(1)            |
| `len()`               | O(1)            |
