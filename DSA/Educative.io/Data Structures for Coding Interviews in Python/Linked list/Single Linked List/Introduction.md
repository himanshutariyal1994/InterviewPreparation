# Structure of A Singly Linked List

The most primitive form of the linked list data structure is the singly linked list. a linked list is formed by nodes which are linked together like a chain. To start things off, let’s take a look at its basic structure:

- `Head node` having the data and Pointer to the next node
- `Middle node` having the data and Pointer to the next node
- `Tail node` having data and a Pointer to `None`

Each node holds data along with a forward pointer to the next node in the list. The absence of a backwards pointer implies that there is a uni-directional link, i.e., the whole list points in one direction and cannot point backwards. This is why it is called a `singly linked list.`

# Classes needed to implement linked lists

For now, we only need to concern yourself with the two classes needed to implement a singly linked list:

- **Node Class**
- **LinkedList Class**

## Node Class

The Node class has two components:

- Data
- Pointer

`Data` is the value you want to store in the node. Think of it as the value at a specific index in a list. The `data` type can range from string or integer to a user-defined class.
The `pointer` refers us to the next node in the list. It is essential for connectivity.

> Note that `‘pointer’` is a Node type variable.

Here’s a typical definition of a Node class:

```python
class Node:
	def __init__(self, data):
		self.data = data # Data field
		self.next = None # Pointer to next node
```

> Explanation: As we discussed, the `Node` class has two variables. `data` contains your specified value and `next` is the pointer to the next element of the list.

## LinkedList Class

The linked list itself is a `collection` of **Node objects** which we defined above. To keep track of the list, we need a pointer to the first node in the list.

This is where the principle of the **head** node comes in. The **head** does not contain any data and only points to the beginning of the list. This means that, for any operations on the list, we need to traverse it from the **head** (the start of the list) to reach our desired node in the list.

The implementation of the `LinkedList` class is shown below:

```python
class LinkedList:
	def __init__(self):
		self.head = None # Pointer to first node
```

> Explanation: The implementation is fairly simple. When the list is first initialized it has no nodes, so the **head** is set to `None`.

# Linked lists vs Lists

The main difference between lists and linked lists is in the way elements are inserted and deleted. Lists are arranged contiguously in the memory, while nodes of a linked list may be dispersed in the memory.

As for linked lists, insertion and deletion at the head happen in a constant amount of time, whereas at tail, it takes O(n) time. In the case of lists, it takes O(n) time to insert or delete a value. This is because of the different memory layouts of both the data structures.

The following table sums up the performance tradeoff between list and linked list:

| Operation        | Linked List | List            |
| ---------------- | ----------- | --------------- |
| access           | O(n)        | O(1)            |
| insert (at head) | O(1)        | O(n)            |
| delete (at head) | O(1)        | O(n)            |
| insert (at tail) | O(n)        | O(n) / O(1)\*   |
| delete (at tail) | O(n)        | O(n) / O(1)\*\* |

In a linked list, **insertion** and **deletion** happen in a constant amount of time given the pointer of the node to be deleted/inserted. You can simply add or delete a node between two Nodes. However, if we were to delete the tail, we would still have to traverse the linked list and update the tail pointer and set it to the previous node. This will take `O(n)` time. In a list, the two operations would take `O(n)` time since addition or deletion would mean shifting the whole list left or right.

The **access** operation in lists, as we talked about earlier, is much faster `(O(1))` as you can simply use the index of a list to access the value you need. In linked lists, there is no concept of indexing. To reach a certain element in the list, we must **traverse** it from the beginning so it takes `O(N)` time

> Note:\* Insertion at tail for arrays like data structures is in O(n), but in python, the `append` method for lists is able to do it in O(1).

> Note:\*\* Deletion at tail for arrays like data structures is in O(n), but in python, the `pop` method for lists is able to do it in O(1).

# Basic Linked List Operations

The primary operations which are generally a part of the `LinkedList` class are listed below:

- `get_head()` - returns the head of the list
- `is_empty()` - returns true if the linked list is empty
- `print_list()` - print all the data elements by traversing through the linked list
- `insert_at_head(data)` - inserts an element at the start/head of the linked list
- `insert_at_tail(data)` - inserts an element at the end of the linked list
- `delete(data)` - deletes an element with your specified value from the linked list
- `delete_at_head()` - deletes the first element of the list
- `search(data)` - searches for an element with the specified value in the linked list

> If you observe the list of functions mentioned above, `get_head()` and `is_empty()` are helper functions that will prove useful in all the others.

## get_head() method

This method simply returns the **head** node of our linked list

```python
class Node:
		def __init__(self, data):
				self.data = data
				self.next = None

class LinkedList:
		def __init__(self):
				self.head = None

		def get_head(self):
				return self.head


lst = LinkedList()  # Linked List created
print(lst.get_head())  # Returns None since headNode does not contain any data
```

> Note: The time complexity for `get_head()` is `O(1)` as we simply return the head.

## is_empty()

The basic condition for our list to be considered empty is that there are no nodes in the list. This implies that head points to `None`.

```python
class Node:
		def __init__(self, data):
				self.data = data
				self.next = None


class LinkedList:
		def __init__(self):
				self.head = None

		def get_head(self):
				return self.head

		def is_empty(self):
				return True if self.head is None else False


lst = LinkedList()  # Linked List created
print(lst.is_empty())  # Returns True
```

> Note: Even when a linked list is empty, the `head` must always exist. Time complexity will be in O(1) as all we need to do is check whether the `head` node points to `None` or not.

# Single Linked List Insertion

The three types of insertion strategies used in singly linked-lists are:

- Insertion at the head
- Insertion at the tail
- Insertion at the kth index

## Insertion at Head

> This type of insertion means that we want to insert a new element as the `first` element of the list. As a result, the **newly added** node will become the `head`, which in turn will point to the previous first node.

The implementation of this operation is simple and straightforward. It is all about correctly manipulating the next_element of the node being inserted.

```python
class Node:
		def __init__(self, data):
				self.data = data
				self.next = None


class LinkedList:
		def __init__(self):
				self.head = None

		# Insertion at Head
		def insert_at_head(self, data):
				# Create a new node containing your specified value
				temp_node = Node(data)
				# The new node points to the same node as the head
				temp_node.next = self.head
				self.head = temp_node  # Make the head point to the new node
				return self.head  # return the new list

		def get_head(self):
				return self.head

		def is_empty(self):
				return True if self.head is None else False

		# Printing out the contents of linked list
		def print_list(self):
				if(self.is_empty()):
						print("List is Empty")
						return False
				temp = self.head
				while temp.next is not None:
						print(temp.data, end=" -> ")
						temp = temp.next
				print(temp.data, "-> None")
				return True


list = LinkedList()
list.print_list()

print("Inserting values in list")
for i in range(1, 10):
		list.insert_at_head(i)

list.print_list()
```

Now, we are at the main part of the code - `insert_at_head()` takes an integer value as `data` and inserts it just after `head` to make it the first element of the list.
The function follows these steps to insert a new node:

- Create a new `Node` object with the given **data**, called `temp_node`.
- Make the `next` of `temp_node` equal to the original `head` .
- `temp_node` will become the `next` of `head`.

At every instance, we point the head to a new node. Therefore, the time complexity for insertion at head is `O(1)`.

# Single Linked List Deletion

> The `deletion` operation combines principles from both `insertion` and `search`. It uses the `search` functionality to find the value in the list.

Deletion is one of the instances where linked lists are more efficient than arrays. In an array, you have to shift all the elements backward if one element is deleted. Even then, the end of the array is empty and it takes up unnecessary memory. In the case of linked lists, the node can simply be removed in constant time.

The three types of deletion strategies used in singly linked-lists are:

- Deletion at the head
- Deletion at the tail
- Deletion by value

## Deletion at Head

> This operation simply deletes the first node from a list. If the list is empty, the function does nothing.

The implementation of this operation is simple and straightforward. It is all about correctly manipulating the next_element of the node being inserted.

```python
class Node:
		def __init__(self, data):
				self.data = data
				self.next = None


class LinkedList:
		def __init__(self):
				self.head = None

		def get_head(self):
				return self.head

		def is_empty(self):
				return True if self.head is None else False

		# Deletion at Head
		def delete_at_head(self):
				# Get Head and firstElement of List
				first_element = lst.get_head()

				# if List is not empty then link head to the
				# nextElement of firstElement.
				if first_element:
						self.head = first_element.next
						first_element.next = None
				return

		# Printing out the contents of linked list
		def print_list(self):
				if(self.is_empty()):
						print("List is Empty")
						return False
				temp = self.head
				while temp.next is not None:
						print(temp.data, end=" -> ")
						temp = temp.next
				print(temp.data, "-> None")
				return True


list = LinkedList()
list.print_list()

print("Inserting values in list")
for i in range(1, 10):
		list.insert_at_head(i)

list.delete_at_head()
list.print_list()
```

There is nothing too complicated going on here. We access the first element of the list

> first_element = lst.get_head()

`first_element` can either be a node (the list is not empty) or not intialized (if the list is empty).

If a node is found, its `next` becomes the `head`. Time complexity will be `O(1)`

Now, `first_element` has been removed from the linked list and its **deletion from memory** will be handled by Python since we haven’t specified a destructor.
