# Structure of A Doubly Linked List

The constraint which arises when dealing with `singly linked lists` is that for any function which does not operate at the **head** node, we must traverse the whole list in a loop.
While the search operation in a normal list works in the same way, **access** is much faster as lists allow indexing.

Furthermore, since a singly linked list can only be **traversed** in `one direction`, we needlessly have to keep track of **previous** elements. This is where the `doubly linked list` comes to the rescue!

The only difference between `doubly and singly linked lists` is that in DLLs each `node` contains pointers for both the `previous` and the `next` **node**. This makes the DLLs **bi-directional**. A doubly linked list is formed by nodes which are linked together like a chain. To start things off, let’s take a look at its basic structure:

- `Head node` having the data and Pointer to the **next** node
- `Middle node` having the data and Pointers to the **next** and **previous** node
- `Tail node` having data and a Pointer to the **previous** node

Each node holds data along with a **forward** and **backward** pointer to the next node in the list.

<br />
<br />

# Node class needed to implement Doubly linked lists

To implement this in code, we simply need to add a new member to the already constructed **Node** class. Here’s a typical definition of a Node class in `DLLs`:

```python
class Node:
	def __init__(self, data):
		self.data = data # Data field
		self.previous = None # Pointer to the previous node
		self.next = None # Pointer to next node
```

> Explanation: `data` and `next` remain unchanged. The `previous` pointer has been introduced to store information about the preceding node.

<br />
<br />

# LinkedList Class needed to implement Doubly Linked lists

The implementation of the `LinkedList` class remains the same as in `Singly Linked List` except adding a new pointer for `tail`:

```python
class LinkedList:
	def __init__(self):
		self.head = None # Pointer to head node
		self.tail = None # Pointer to tail node
```

> In a singly linked list, `insert_at_tail` method now works in `O(1)`. We can simply set the new node as the next of the `previous` end node and update the `tail`.
> However, the tail really shines in doubly linked lists. Apart from tail operations, `insertion` and `deletion` become **twice** as fast because we can traverse the list from both sides.

<br />
<br />

# Singly vs Doubly Linked Lists

DLLs have a few advantages over SLLs, but these perks do not come without a cost:

- Doubly linked lists can be traversed in both directions, which makes them more compatible with complex algorithms.
- **Nodes** in doubly linked lists require extra memory to store the `previous` pointer.
- Deletion is more efficient in `doubly linked lists` as we do not need to keep track of the `previous` node. We already have a **backwards** pointer for it.

<br />
<br />

# Summary of Doubly Linked List methods in a nutshell (Search/Insert/Delete nodes)

```python
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None


	# Method to check whether linked list is empty
	def is_empty(self):
		return self.head is None


	# Method to get the head node
	def get_head(self):
		return self.head


	# Method to search an element in LL
	def search(self,value):
		# If LL is empty, return False
		if self.is_empty():
			return False

		# Initialise head_node as self.head, and iterate through loop
		# till the tail element
		head_node = self.get_head()
		while head_node.next is not None:
			if head_node.data is value:
				return True

			head_node = head_node.next

		# Since the entire list has been traversed, the element does not
		# exist in the LL, so return False
		return False


	# Method to print all data nodes in Linked list
	def print_linked_list_data():
		# If LL is empty, print no nodes present
		if self.is_empty():
			print('Linked list is empty')

		# Initialise head_node as self.head, and iterate through loop
		# till the tail element
		head_node = self.get_head()
		while head_node.next:
			print(head_node + '-->')
			head_node = head_node.next

		print(head_node.data + '--> None')

	'''
	Insertion in Linked list:
	a. Insertion at head
	b. Insertion at tail
	c. Insertion at k-th index
	'''

	# Insertion at head
	def insert_at_head(self,value):
		# Create a new node
		new_node = Node(value)

		# Set next pointer to the head node
		new_node.next = self.get_head()

		# Reassign head to the new node to ensure that it has been
		# the first node of the LL
		self.head = new_node

		# return the head node for traversal/printing
		return self.head


	# Insertion at tail
	def insert_at_tail(self,value):
		# Create a new node
		new_node = Node(value)

		# If LL is empty, make the new node as head node
		if self.is_empty():
			self.head = new_node
			return self.head

		# Initialise head_node as self.head, and iterate through loop
		# till the tail element
		head_node = self.get_head()

		while head_node.next:
			head_node = head_node.next

		# at this moment head_node is the previous tail node, so
		# point the next pointer of the tail to the new node
		head_node.next = new_node
		return self.head


	# Insertion at k-th index
	def insert_at_k-th_index(self,value,index):
		# Create a new node
		new_node = Node(value)

		# If index is <0, throw error
		if index < 0:
			print('Illegal index')
			return False

		# If index is 0, insert node at head
		if index == 0:
			self.insert_at_head(value)
			return self.head

		counter = 1
		current_node = self.get_head()

		# Iterate till we encounter the tail node. If index and counter match
		# then assign next of new_node to next of the current node, and
		# next of the current node should be new_node
		while current_node.next:
			if counter == index:
				new_node.next = current_node.next
				current_node.next = new_node
				return self.head

			counter += 1
			current_node = current_node.next

		# Return false since the list has completed and the index is not matched
		return False



	'''
	Deletion in Linked list:
	a. Deletion at head
	b. Deletion at tail
	c. Deletion by value
	'''

	# Deletion at head
	def delete_at_head(self):
		# If LL is empty, throw an error
		if self.is_empty():
			print('Linked List is empty')
			return False

		# LL is not empty, so isolate head node from the list and assign None
		# to the next pointer of the head node. Also, assign head to the next of the
		# initial head none
		head_node = self.get_head()
		self.head = head_node.next
		head_node.next = None
		return self.head


	# Deletion at tail
	def delete_at_tail(self):
		# If LL is empty, throw an error
		if self.is_empty():
			print('Linked List is empty')
			return False

		# If only 1 node is present, set head to None
		if self.head.next is None:
			self.head = None
			return self.head

		# LL is not empty, so iterate through LL till we get the second last node
		head_node = self.get_head()
		while head_node.next.next:
			head_node = head_node.next

		# This will be the second last node of the LL, this deleting the tail node
		head_node.next = None
		return self.head


	# Deletion by value
	def deletion_by_value(self,value):
		# If LL is empty, throw an error
		if self.is_empty():
			print('Linked List is empty')
			return False

		# LL is not empty, so set curr_node as head and previous_node as None
		curr_node = self.get_head()
		prev_node = None

		# If only 1 node is present and value equals data at node, set head to None
		if curr_node.data is value:
			self.head = curr_node.next
			curr_node.next = None
			return self.head

		# Iterate through the list to break relnship between prev and curr node
		while curr_node:
			if curr_node.data is value:
				prev_node.next = curr_node.next
				curr_node.next = None
				return self.head

			prev_node = curr_node
			curr_node = curr.node.next

		# Return false since the list has completed and the value is not found in LL
		return False

```
