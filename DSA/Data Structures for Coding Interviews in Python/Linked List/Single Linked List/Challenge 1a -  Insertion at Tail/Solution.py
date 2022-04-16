'''
This algorithm traverses the entire linked list and hence, works in O(n) time.
'''


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        # Creating a new node
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node
        return self.head

    def insert_at_tail(self, data):
        # Creating a new node
        new_node = Node(data)

        # Check if the list is empty, if it is simply point head to new node
        if self.is_empty():
            self.head = new_node
            return self.head

        # if list not empty, traverse the list to the last node
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next

        # Set the next of the previous node to new node
        temp_node.next = new_node
        return self.head
