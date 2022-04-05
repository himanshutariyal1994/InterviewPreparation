'''
This algorithm traverses the entire linked list and hence, works in O(n) time.
It used the iterative approach rather than the recursive approach

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

    def search(self, value):
        # Check if the list is empty, if it is return False
        if self.is_empty():
            return False

        # if list not empty, traverse the list to the last node
        temp_node = self.head
        while temp_node:
            if temp_node.data == value:
                return True

            temp_node = temp_node.next

        # We have traverse to the end of the list, return False
        return False
