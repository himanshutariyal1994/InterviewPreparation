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
