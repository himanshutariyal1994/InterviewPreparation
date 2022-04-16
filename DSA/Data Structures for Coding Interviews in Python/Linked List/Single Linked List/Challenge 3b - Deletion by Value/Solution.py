'''
This algorithm traverses the entire linked list and hence, works in O(n) time.
The algorithm is very similar to delete_at_head. The only difference is that you need to keep track of two nodes, head_node and previous_node.

head_node will always stay one step ahead of previous_node. Whenever head_node becomes the node to be deleted, the previous_node starts 
pointing at the node next to head_node. If head_node is the last element, previous_node will simply point to None.

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

    def deletion_by_value(self, value):
        # Check if the list is empty, if it is return False
        if self.is_empty():
            return False

        # If head node contains the value, set self.head as None to delete the node
        curr = self.head
        if curr.next is None and curr.data == value:
            self.head = curr.next
            curr.next = None
            return True

        previous_node = None
        while curr:
            if curr.data == value:
                previous_node.next = curr.next
                curr.next = None
                return True

            previous_node = curr
            curr = curr.next

        # Since we were not able to find the value after traversing, return False
        return False
