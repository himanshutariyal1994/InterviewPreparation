'''
Non-optimal solution is to add each data to a set, and if the data node exist then delete that node

Union
Time complexity: O(N) since each node is traversed once, and O(N) for removing duplicates
Space complexity: O(1) since no extra memory is used

Intersection
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

    def union(self, head_list2):
        if self.is_empty():
            return head_list2

        if head_list2 is None:
            return self.head

        head_node = self.head
        while head_node.next:
            head_node = head_node.next

        head_node.next = head_list2
        self.remove_duplicates()
        return self.head

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

    def intersection(self, head_list2):
        if self.is_empty():
            return head_list2

        if head_list2 is None:
            return self.head

        result = LinkedList()
        curr = self.head
        while curr:
            if head_list2.search_node(curr.data):
                result.insert_at_head(curr.data)

            curr = curr.next

        self.remove_duplicates()
        return self.head
