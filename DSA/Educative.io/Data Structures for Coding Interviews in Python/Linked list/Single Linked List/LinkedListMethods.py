from locale import currency


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # Check if the LL is empty
    def is_list_empty(self):
        return self.head is None

    # Return the head node of the LL
    def get_head_node(self):
        return self.head

    # Return linked list printed in arrow format
    def print_linked_list(self):
        if self.is_list_empty():
            print('None')

        printed_list = ''
        curr_node = self.get_head_node()
        while curr_node:
            printed_list += str(curr_node.data) + ' --> '
            curr_node = curr_node.next

        printed_list += ' None'
        print(f'Linked list: {printed_list}')

    # Return length of linked list
    def length_linked_list(self):
            # Return 0 if list is empty
        if self.is_list_empty():
            print('Linked list is empty')
            return 0

        counter = 0
        head_node = self.get_head_node()

        while head_node:
            counter += 1
            head_node = head_node.next

        return counter

    # return the index of the searched element in LL
    def search_node(self, value):
        if self.is_list_empty():
            print('Linked list is empty')
            return -1

        head_node = self.get_head_node()
        counter = 0

        # Iterate till we encounter None post tail element
        while head_node:
            if head_node.data is value:
                print(f'element found at index {counter}')
                return counter

            counter += 1
            head_node = head_node.next

        # Since element has not been found, return -1
        return -1

    # insert data at head node
    def insert_at_head(self, value):
        # Create the new node
        new_node = Node(value)

        # add node as head node if list is empty
        new_node.next = self.head
        self.head = new_node
        self.print_linked_list()
        return self.head

    # insert at tail node
    def insert_at_tail(self, value):
        # Create the new node
        new_node = Node(value)

        # Add node as head node if list is empty
        if self.is_list_empty():
            self.head = new_node
            return self.head

        # Iterate till head_node equals tail node
        head_node = self.get_head_node()
        while head_node.next:
            head_node = head_node.next

        # till this time, head_node will be the tail node
        # so assign next of tail node to the new node
        head_node.next = new_node
        return self.head

    # insert at k-th index
    def insert_at_kth_index(self, value, k):
        # if k is less than 0, return the head node
        if k < 0:
            print('Illegal value of k')
            return self.head

        # Create a new Node
        new_node = Node(value)

        # If k = 0, insert at head
        if k == 0:
            return self.insert_at_head()

        # take 2 pointers, prev at None and current at head node,
        # and insert element between them as per required index
        counter, curr = 1, self.get_head_node
        while curr.next:
            if counter == k:
                new_node.next = curr.next
                curr.next = new_node
                return self.head

            counter += 1
            curr = curr.next

        # This means that index is greater than length of LL,
        # so return self.head since nothing was added
        return self.head

    # Deletion at head
    def delete_at_head(self):
        # check if list is empty, if True return None
        if self.is_list_empty():
            print('Linked list is empty')
            return None

        # initialise self.head as next element and break association of prev self.head
        # node with next element
        head_node = self.head
        self.head = head_node.next
        self.head.next = None
        return self.head

    # Delete at tail
    def delete_at_tail(self):
        # check if list is empty, if True return None
        if self.is_list_empty():
            print('Linked list is empty')
            return None

        # Check if LL only has 1 node, then delete at head
        if self.head.next is None:
            return self.delete_at_head()

        # Initialise head_node to start of list and navigate till second last node
        # break chain between second last and tail node
        head_node = self.get_head_node()
        while head_node.next.next:
            head_node = head_node.next

        # at this moment, break association between second last and last node
        head_node.next = None
        return self.head

    # Delete at k-th index
    def delete_at_kth_index(self, k):
        # check if k is less than 0, throw error
        if not k or k < 0:
            print('Illegal value of k')
            return None

        # Check if list is empty, then throw error
        if self.is_list_empty():
            print('Linked list is empty')
            return None

        # check if k == 0, then delete head node
        if k == 0:
            return self.delete_at_head()

        counter, head_node, prev_node = 0, self.get_head_node(), None
        while head_node.next:
            if counter == k:
                prev_node.next = head_node.next
                head_node.next = None
                return self.head

            counter += 1
            prev_node = head_node
            head_node = head_node.next

        # This means that k is greater than Length of LL, so return None
        return None

    # Deletion by value
    def delete_by_value(self, value):
        # Check if LL is empty, if True return None
        if self.is_list_empty():
            print('Linked list is empty')
            return None

        # Check if LL has 1 node, and if data at that node equals value
        # so delete the head node
        curr = self.get_head_node()
        if curr.next is None and curr.data == value:
            return self.delete_at_head()

        prev = None
        while curr:
            if curr.data == value:
                prev.next = curr.next
                curr.next = None
                return self.head

            prev = curr
            curr = curr.next

        # This means that element is not found in LL, so return None
        return None

        # Detect loop in Linked list
        def detect_loop(self):
            pass

    # Remove duplicates in Linked list using set
    def remove_duplicates(self):
        # Check if list is empty, if True return None
        if self.is_list_empty():
            return None

        # create a set, keep on adding elements and remove
        # them if they exist in set
        data_set = set()
        curr, prev = self.get_head_node, None
        while curr:
            if curr.data in data_set:
                next = curr.next
                prev.next = next
                curr.next = None
                curr = next
            else:
                data_set.add(curr.data)
                prev = curr
                curr = next

        return self.head

    # Remove duplicates in Linked list without using a set
    def remove_duplicates_without_set(self):
        # Check if list is empty, if True return None
        if self.is_list_empty():
            return None

        # create a set, keep on adding elements and remove
        # them if they exist in set
        curr = self.get_head_node
        while curr and curr.next:
            if curr.next.data == curr.data:
                curr.next = curr.next.next
                curr.next.next = None
            else:
                curr = curr.next

        return self.head

    # Find the middle element in Linked List
    def find_middle_element(self):
        # Check if list is empty, if True return None
        if self.is_list_empty():
            return None

        # Use fast pointer (moves by 2 nodes), slow pointer (moves by 1 node) approach.
        # if the list is not having a loop, when the fast element reaches the end of the list,
        # the slow element will always be at the middle now
        slow = self.get_head_node()

        # if LL has 1 node, return data of head node
        if slow.next is None:
            return slow.data

        fast = slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    # Detect loop in Linked list
    def detect_loop(self):
        # Check if list is empty, if True return False
        if self.is_list_empty():
            print('Linked list is empty')
            return False

        # Check if list has 1 node, then return False
        slow_node = self.get_head_node()
        if slow_node.next is None:
            return False

        # Use fast pointer (moves by 2 nodes), slow pointer (moves by 1 node) approach.
        # if the list is not having a loop, when the fast element reaches the end of the list,
        # it means that there is no loop. If slow node and fast node meets at the same node,
        # it means that there is a loop in the cycle
        fast_node = slow_node

        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

            # If they are at same point, it means that LL has a loop.
            if slow_node == fast_node:
                return True

        # if we are still here, it means that LL does not have a loop.
        return False

    # Reverse a linked list
    def reverse_linked_list(self):
        # check if list is empty, if True return None
        if self.is_list_empty():
            return None

        # Check if list has 1 node, return head node
        curr = self.get_head_node()
        if curr.next is None:
            return self.head

        prev, next = None, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

            # at this moment, prev is at the tail of the original list so assign head node to prev node
            # to set the new head node
        self.head = prev
        return self.head

    # Remove the middle element in Linked List
    def remove_middle_element(self):
        # check if list is empty, if True return None
        if self.is_list_empty():
            print('Linked list is empty')
            return None

        # Check if LL has 1 node, delete that node and return head node
        if self.head.next is None:
            self.head = None
            return self.head

        prev, slow, fast = None, self.head, self.head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

            # at this point, slow will be pointing to the middle node,
            # so set next of prev pointer to next of slow, set next of
            # slow to None and return head node
        prev.next = slow.next
        slow.next = None
        return self.head

    # Remove n-th node from end of Linked List
    def remove_nth_node_from_end(self, n):
        # Check if list is empty, if True return None
        # If n is less than 0, return None
        if self.is_list_empty() or n < 0:
            print('Linked list is empty')
            return None

        counter, first_ptr, second_ptr = 0, self.head, self.head
        while counter < n:
            if second_ptr is None:
                return None

            second_ptr = second_ptr.next
            counter += 1

        if not second_ptr:
            return first_ptr.next

        while second_ptr.next:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        # at this moment, first_ptr is the prev element to the element to delete
        first_ptr.next = first_ptr.next.next
        return self.head

    # Find Union of 2 Linked Lists
    def union_linked_lists(self, list2_head):
        # Check if list 1 is empty, return List 2
        if self.is_list_empty():
            return list2_head

        # Check if list2 is empty, return List 1
        if list2_head is None:
            return self.head

        # loop through list to get tail of list1
        curr = self.head
        while curr:
            curr = curr.next

        # add list 2 to end of list 1
        curr.next = list2_head

        # add list 2 to end of list 1
        return self.remove_duplicates()

    # Find intersection of 2 linked Lists
    def intersection_of_linked_lists(self, list2_head):
        # Check is list 1 is empty, if True return None
        if self.is_list_empty():
            return None

        # Check if list 2 is empty, if True return None
        if list2_head is None:
            return None

        result = LinkedList()
        curr = self.head
        while curr:
            if list2_head.search_node(curr.data):
                result.insert_at_head(curr.data)

            curr = curr.next

        self.remove_duplicates()
        return self.head

    # Find intersection point of 2 Linked Lists (if existing)
    def find_intersection_point_linked_lists(self, list2_head):
        '''
        non-optimal solution is to used set to store nodes in list1 and check whether the same 
        node is present in list2

        Time complexity : O(N)
        Space complexity: O(N)

        hash_set = set()
        curr,curr2 - self.head,list2.head

        while curr:
          if curr not in hash_set:
            hash_set.add(curr)

          curr = curr.next

        while curr2:
          if curr2 in hash_set:
            return curr2

          curr2 = curr2.next

        return None
        '''

        '''
        Using the optimal approach, we will traverse each node towards length of list1 and list2
        if they meet somewhere, it indicates that nodes have the intersecting point

        Time complexity : O(N)
        Space complexity: O(1)
        '''

        curr, curr2 = self.head, list2_head

        while curr != curr2:
            curr = curr.next if curr else list2_head
            curr2 = curr2.next if curr2 else self.head

        # at this point curr will hold either the intersecting node if the
        # 2 LLs intersect or None if they dont
        return curr
