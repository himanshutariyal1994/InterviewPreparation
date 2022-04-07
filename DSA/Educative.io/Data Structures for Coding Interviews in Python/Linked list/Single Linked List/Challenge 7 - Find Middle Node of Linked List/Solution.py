'''
Non-optimal solution is to add data at each node to a list till the tail element is encountered
Post that, return the data element at correspondng index

Time complexity: O(N) since each node is traversed once
Space complexity: O(N) since data of each node is added to the list
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

    def find_mid(self):
        if self.is_empty():
            return False

        head_node = self.head
        data_list = []

        while head_node:
            data_list.append(head_node.data)
            head_node = head_node.next

        len_list = len(data_list)
        if len_list % 2 == 0:
            return data_list[len_list/2 - 1]
        else:
            return data_list[len_list//2]


'''
Optimal solution is by using 2 pointers (Slow and Fast). The slow pointer will be shifted by 1 node while the fast pointer will be shifted by 2 nodes.

When the Fast pointer reaches the end of the list, the Slow pointer will be at the middle node. Return the data of the middle node

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

    def find_mid(self):
        if self.is_empty():
            return False

        slow_node = self.head
        if slow_node.next is None:
            return slow_node.data

        fast_node = self.head

        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        return slow_node.data
