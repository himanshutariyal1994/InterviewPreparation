# What is a Queue?

Similar to the Stack, a `queue` is another linear data structure that stores the elements in a sequential manner. The only significant difference between `Stacks` and `Queues` is that instead of using the **LIFO principle**, queues implement the `FIFO` method which is short for `First in First Out`.

According to FIFO, the **first element inserted is the one that comes out first**. We can think of a queue as a pipe with two ends called **front and rear / back**. `Elements from a queue are always deleted from the front and added at the rear`. Queues are slightly trickier to implement as compared to stacks because we have to keep track of both ends of the array.

<br/>

## What are Queues Used for?

Most operating systems also perform operations based on a `Priority Queue (a kind of queue)` which allows operating systems to switch between appropriate processes. They are also used to store packets on routers in a certain order when a network is congested. `Implementing a cache also heavily relies on queues`.

We generally use Queues when:

- We want to **prioritize** something over another
- A resource is shared between multiple devices

<br/>

## How do Stacks work?

A typical **queue** needs the following set of functions to work perfectly. The entire functionality of queues depends on the first **two** functions and the rest are just helper functions to produce simple, and understandable code.

| Function           | What does it do?                                 |
| ------------------ | ------------------------------------------------ |
| `enqueue(element)` | inserts element at the end of the queue          |
| `dequeue()`        | removes an element from the start of the queue   |
| `front()`          | returns the first element of the queue           |
| `rear()`           | returns the last element inserted into the queue |
| `is_empty()`       | checks if the queue is empty                     |
| `size()`           | returns the size of the queue                    |

<br/>

## Types of queue

Listed below are the **four** most common types of queues.

- **Linear Queue**
- **Circular Queue**
- **Priority Queue**
- **Double-ended Queue**

The queue that we have discussed so far was a `linear` queue. The following section describes the rest 3 types of **queues**

### Circular Queue

> `Circular queues` are almost similar to linear queues with only one exception. As the name itself suggests, circular queues are `circular` in structure which means that **both ends are connected to form a circle**. Initially, the front and rear part of the queue point to the same location. Eventually they **move** apart as more elements are inserted into the queue.

### Priority Queue

> In `priority queues`, **all elements have a priority associated with them** and are sorted such that the **most prioritized object** appears at the `front` and the **least prioritized object** appears at the `end` of the queue. These queues are widely used in most operating systems to determine which programs should be given more priority.

### Double-Ended Queue

> The `double-ended queue` acts as a queue from **both ends(back and front)**. It is a flexible data structure that provides `enqueue` and `dequeue` functionality on both ends in **O(1)**. Hence, it can act like a normal linear queue if needed.

<br/>

## Implementing a stack

> `Queues` are implemented in many ways. They can be represented by using `Lists`, `Linked Lists`, or even `Stacks`. But most commonly `Lists` are used as the easiest way to implement Queues.

> With typical arrays, however, the `time complexity is O(n)` when `dequeuing` an element from the **beginning** of the queue. This is because when an element is removed, the addresses of all the subsequent elements must be shifted by 1, which makes it less efficient. **With linked lists and doubly linked lists, the operations become faster.**. So we can use a `doubly-linked list` to implement queues for optimising time complexity

```python
# Implementing a Custom Queue class using Doubly Linked Lists.
# Note: The Doubly Linked list class must be implemented first
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    # Check if Linked List is empty
    def is_empty(self):
        return True if self.head is None else False

    # Return the head node of the Doubly LL
    def get_head(self):
        return None if self.is_empty() else self.head.data

    # Return the tail node of the Doubly LL
    def get_tail(self):
        return None if self.is_empty() else self.tail.data

    # Print the Doubly Linked List
    def print_list(self):
        if self.is_empty():
            return 'None'
        else:
            list_str, head_node = '', self.head
            while head_node:
                list_str += str(head_node.data) + ' <-> '
                head_node = head_node.next

            list_str += 'None'
            return list_str

    # Insert data at tail node
    def insert_at_tail(self, value):
        node = Node(value)

        # If LL is empty, assign node as head and tail node
        # else set next of tail as new node, prev of new node as tail node
        # and assign tail node as the new node
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1
        return node.data

    # Remove data at head node
    def delete_at_head(self):
        # Check if LL is empty, if True return None
        if self.is_empty():
            print('Doubly Linked List is empty')
            return None

        head_node = self.head
        if head_node.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = head_node.next
            self.head.prev = None
            head_node.next = None

        self.length -= 1
        return head_node.data

    # Return length of Doubly LL
    def length_list(self):
        return 0 if self.is_empty() else self.length


class QueuesDoublyLinkedList:
    def __init__(self):
        self.items = DoublyLinkedList()

    # Check if the queue is empty
    def is_empty(self):
        return self.items.is_empty()

    # Return the size of items in queue
    def size(self):
        return self.items.length_list()

    # print queue in list form
    def print_queue(self):
        print(f'Queue : {self.items.print_list()}')

    # Return the element at the front
    def front(self):
        return None if self.is_empty() else self.items.get_head()

    # Return the element at the rear
    def rear(self):
        return None if self.is_empty() else self.items.get_tail()

    # Push a new element to the rear
    def enqueue(self, value):
        return self.items.insert_at_tail(value)

    # Remove an element from the front
    def dequeue(self):
        return self.items.delete_at_head()


queue_inst = QueuesDoublyLinkedList()
print(f'Queue empty: {queue_inst.is_empty()}')

for i in range(1, 5):
    queue_inst.enqueue(i)

queue_inst.print_queue()
print(f'Element at the front: {queue_inst.front()}')
print(f'Element at the rear: {queue_inst.rear()}')
print(f'Size of items in queue: {queue_inst.size()}')

print(f'Element removed from queue: {queue_inst.dequeue()}')
print(f'Element popped from stack: {queue_inst.dequeue()}')
print(f'Element at the front now: {queue_inst.front()}')
print(f'Element at the rear now: {queue_inst.rear()}')
print(f'Size of queue now: {queue_inst.size()}')
print(f'Stack empty: {queue_inst.is_empty()}')
```

The simple `Queues` class called `QueuesDoublyLinkedList` will consist of the member functions given above and a **doubly linked list** called `items` that will hold all the elements of the queue.

> The `is_empty`() function checks whether the queue is empty or not. If the length of the list is 0, then the function will return **True**. Otherwise, it will return **False**.

> The `front()` function returns the element in the front. **In case of an empty stack_list, it would return None.**

> The `rear()` function returns the element in the rear. **In case of an empty stack_list, it would return None.**

> The `size()` method simply returns the number of elements in the queue.

> The `enqueue(value)` method simply adds the value to the rear of the list

> The `dequeue()` method will remove the element from the front of the list and returns it back to the calling function

<br/>

## Complexities of Stack Operations

| Operation          | Time Complexity |
| ------------------ | --------------- |
| `enqueue(element)` | O(1)            |
| `dequeue() `       | O(1)            |
| `front() `         | O(1)            |
| `rear() `          | O(1)            |
| `is_empty()`       | O(1)            |
| `size()`           | O(1)            |
