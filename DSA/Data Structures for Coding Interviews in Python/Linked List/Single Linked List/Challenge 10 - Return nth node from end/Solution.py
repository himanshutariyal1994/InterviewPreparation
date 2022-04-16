'''
Non-Optimal solution is to calculate the length of list, and then return data for the (len-n+1)th element from the front

Time complexity: O(N) since each node is traversed twice, one for calculating length and other for traversal
Space complexity: O(1) since no extra memory is used
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

    def length_list(self):
        if self.is_empty():
            return 0

        counter = 0
        curr = self.head

        while curr:
            counter += 1
            curr = curr.next

        return counter

    # Return the data value of the n'th node deleted
    def remove_nth(self, n):
        # Check if list is empty, if True return None
        if self.is_empty():
            print('Linked list is empty')
            return -1

        len_list = self.length_list()
        fwd_index = len_list - n + 1

        if fwd_index < 0 or fwd_index > len_list:
            return -1

        if fwd_index == 0:
            return self.head.data

        counter, curr = 0, self.head
        while curr:
            if counter == fwd_index:
                return curr.data

            curr = curr.next
            counter += 1

        return -1


'''
Optimal solution is to keep 2 pointers: the first pointer will be at head and the second pointer will be at the n-th index.
Once the second pointer reach the end, teh first pointer will be at nth position from the end

Time complexity : O(N) since nodes are traversed only once
Space complexity: O(1)
'''


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head is None

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

    def length_list(self):
        if self.is_empty():
            return 0

        counter = 0
        curr = self.head

        while curr:
            counter += 1
            curr = curr.next

        return counter

    # Return the data value of the n'th node deleted
    def remove_nth(self, n):
        # Check if list is empty, if True return None
        if self.is_empty():
            print('Linked list is empty')
            return -1

        # check if n is less than 0, return None if True
        if n < 0:
            return -1

        counter = 0
        first_node, second_node = self.head, self.head

        # Move second pointer n-times ahead
        while counter < n:
            if second_node is None:
                return -1

            second_node = second_node.next
            counter += 1

        # Iterate till second node reaches end, at that point
        # first node will be at the correct point
        while second_node:
            first_node = first_node.next
            second_node = second_node.next

        return first_node.data
