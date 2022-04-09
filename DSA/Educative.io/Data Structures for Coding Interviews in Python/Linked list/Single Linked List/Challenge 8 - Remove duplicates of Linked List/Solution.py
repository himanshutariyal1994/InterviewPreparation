'''
Non-optimal solution is to add each data to a set, and if the data node exist then delete that node

Time complexity: O(N) since each node is traversed once
Space complexity: O(N) since data of each node is added to the set
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

    def remove_duplicates(self):
        if self.is_empty():
            return None

        head_node = self.head
        if head_node.next is None:
            return head_node

        data_set = set()
        prev_node = None

        while head_node:
            if head_node.data in data_set:
                next = head_node.next
                prev_node.next = next
                head_node.next = None
                head_node = next
            else:
                data_set.add(head_node.data)
                prev_node = head_node
                head_node = head_node.next

        return self.head


'''
Optimal solution is by using single pointer without using a set to store data. Rationale is that list is sorted, so duplicate element
will be the next element for sure

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

    def remove_duplicates(self):
        if self.is_empty():
            return None

        head_node = self.head
        if head_node.next is None:
            return head_node

        while head_node and head_node.next:
            if head_node.data == head_node.next.data:
                head_node.next = head_node.next.next
                head_node.next.next = None
            else:
                head_node = head_node.next

        return self.head
