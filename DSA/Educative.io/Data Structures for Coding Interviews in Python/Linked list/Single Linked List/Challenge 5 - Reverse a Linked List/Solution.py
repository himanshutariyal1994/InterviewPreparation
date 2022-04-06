'''
Optimal solution is by using 2 pointer approach  (curr to head and prev to None initially) and setting current.next to previous,
moving previous to current and current = current.next till None is achieved

At the end, set self.head as the previous node

Time complexity : O(N) since each node is traversed once
Space complexity : O(1)
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

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        if self.is_empty():
            print('Linked list is empty')

        head_node = self.head
        print_str = ''
        while head_node.next:
            print_str += str(head_node.data) + ' --> '
            head_node = head_node.next
        print_str += str(head_node.data) + ' --> None'
        print(print_str)

    def reverse_linked_list(self):
        if self.is_empty():
            return 0

        curr_node = self.head
        prev_node = None
        next_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node
        return self.head


'''
Driver code:

linked_list = LinkedList()
for i in range(0, 17, 2):
    linked_list.insert_at_head(i)

linked_list.print_linked_list()
linked_list.reverse_linked_list()
linked_list.print_linked_list()
'''
