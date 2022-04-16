'''
Time complexity: O(N) since each number is iterated once and enqueue(),dequeue() ops happen in O(1) time
Space complexity: O(N) since queue will hold the data in memory
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.previous_element = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_head(self):
        if (self.head != None):
            return self.head.data
        else:
            return False

    def is_empty(self):
        if(self.head is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_tail(self, element):
        temp_node = Node(element)
        if(self.is_empty()):
            self.head = temp_node
            self.tail = temp_node
        else:
            self.tail.next_element = temp_node
            temp_node.previous_element = self.tail
            self.tail = temp_node
        self.length += 1
        return temp_node

    def remove_head(self):
        if(self.is_empty()):
            return False
        nodeToRemove = self.head
        if (self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = nodeToRemove.next_element
            self.head.previous_element = None
            nodeToRemove.next_element = None
        self.length -= 1
        return nodeToRemove.data

    def tail_node(self):
        if (self.head != None):
            return self.tail.data
        else:
            return False


class MyQueue:
    def __init__(self):
        self.queue_list = []
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def size(self):
        return self.queue_size

    def enqueue(self, value):
        self.queue_size += 1
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        self.queue_size -= 1
        return front


def find_bin(number):
    if number < 1:
        return []

    result = []
    queue = MyQueue()
    queue.enqueue(1)

    for index in range(number):
        result.append(str(queue.dequeue()))
        s1 = result[index] + "0"
        s2 = result[index] + '1'
        queue.enqueue(s1)
        queue.enqueue(s2)

    return result


for i in range(1, 10):
    print(f'Binary value till {i} are {find_bin(i)}')
