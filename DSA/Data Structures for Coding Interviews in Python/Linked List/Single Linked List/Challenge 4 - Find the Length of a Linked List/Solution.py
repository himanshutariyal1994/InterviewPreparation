'''
Optimal solution is by traversing the whole list and incrementing counter by 1 till we reach the tail node
Time complexity : O(N) since this is a linear algo
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

    def length_linked_list(self):
        if self.is_empty():
            return 0

        len_list = 0
        head_node = self.head

        while head_node:
            len_list += 1
            head_node = head_node.next

        return len_list


'''
Driver code:

linked_list = LinkedList()
for i in range(0, 17, 2):
    linked_list.insert_at_head(i)

linked_list.length_linked_list()
'''
