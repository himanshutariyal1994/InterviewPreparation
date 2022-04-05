'''
This algorithm traverses the entire linked list and hence, works in O(n) time.

Time complexity : O(n) 
Space complexity : O(1).
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

    def delete_at_tail(self):
        # Check if the list is empty, if it is return None
        if self.is_empty():
            return self.head  # None

        # If only 1 node is present, set head to None
        if self.head.next is None:
            self.head = None
            return self.head

        # Else find the node where next.next is None, remove the next association
        # of that node
        temp_node = self.head
        while temp_node.next.next is not None:
            temp_node = temp_node.next

        temp_node.next = None
        return self.head
