'''
Non-optimal solution is to add each node in the hashSet when visited, and check if a particular node has been repeated or not.
If repeated, it indicates that there is a cycle in the LL 
Time complexity: O(N) since each node is traversed once
Space complexity: O(N) since each node is added in the hash set
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

    def detect_cycle(self):
        if self.is_empty():
            return False

        hash_set = set()
        temp_node = self.head

        while temp_node:
            if temp_node in hash_set:
                return True

            hash_set.add(temp_node)
            temp_node = temp_node.next

        return False


'''
Optimal solution is by using Floyd's Hare and Tortoise algorithm. We will use 2 pointers (Slow and Fast). The slow pointer will be shifted by 
1 node while the fast pointer will be shifted by 2 nodes.

If the Fast pointer reaches None before Slow pointer, it indicates that there is no cycle. But if Fast pointer is at the same node as the slow
pointer, it indicates that there is a loop in the LL

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

    def detect_cycle(self):
        if self.is_empty():
            return False

        slow_node = self.head
        fast_node = self.head

        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

            if slow_node == fast_node:
                return True

        return False
