'''
This algorithm traverses the entire linked list and hence, works in O(n) time.
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

    def insert_at_head(self, data):
        # Creating a new node
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node
        return self.head

    def insert_at_kth_index(self, data, pos):
        if not pos or pos < 1:
            print('Illegal position in Linked list')
            return

        # Creating a new node
        new_node = Node(data)

        # check is pos = 1, it means insert at head
        if pos == 1:
            self.insert_at_head(data)

        # Loop through the nodes and change the pointers when we arrive at the counter node
        counter = 1
        head = self.head

        while head.next:
            if counter == pos:
                new_node.next = head.next
                head.next = new_node
                break

            counter += 1
            head = head.next

        return self.head
