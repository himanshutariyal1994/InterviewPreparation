# What is a Binary Search Tree

`Binary Search Trees (BSTs)` are a special kind of binary tree where each node of the tree has key-value pairs. These key-value pairs can be anything, like (username,bank) or (employee, employeeID).

For all the nodes in a BST, **the values of all the keys in the left sub-tree of the node are less than the value of the nodes themselves. All the keys in the right subtree are greater than the values of the node**. This is referred to as the BST rule where `NodeValues(leftsubtree)<=CurrentNodeValue<NodeValues(rightsubtree)`

!["Valid and Invalid BSTs"](/DSA/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Trees/Images/Valid%20Invalid%20BST.png "Valid and Invalid BSTs")

<br/>

# Implementing Binary Search Tree in Python

## The Node Class

To implement a BST, the first thing you’d need is a `node`. A node should have a `value`, a `left child`, a `right child`, and a `parent`.

```python
class Node:
    def __init__(self, val):  # Constructor to initialize the value of the node
        self.val = val
        self.left_child = None  # Sets the left and right children to `None`
        self.right_child = None
        self.parent = None  # Sets the parent to `None`
```

## The BinarySearchTree class

You can then choose to create a wrapper class for the tree itself; this can sometimes make your code cleaner and easier to read, but not always.

```python
class BinarySearchTree:
    def __init__(self, val):  # Initializes a root node
        self.root = Node(val)

BST = BinarySearchTree(6)  # Initializes a BST
print(BST.root)  # print the root node
print(BST.root.val)  # print value of root node
```

<br/>

## Basic Operations in a BST

### Inserting elements in a BST

Here is a description of the algorithm you’d use to insert a new value into a BST.

- **Start from the root node**
- **Check if the value to be inserted is greater than the root/current node’s value**
- **If yes, then repeat the steps above for the right subtree, otherwise repeat the steps above for the left sub-tree of the current node.**
- **Repeat until you find a node that has no right/left child to move onto. Insert the given value there and update the parent node accordingly.**

There are two ways to code a **BST insert function**

- `Iteratively`
- `Recursively`

The following code shows the implementation of inserting in a BST **iteratively** and **recursively**:

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

    def insert(self, val):
        current = self  # points to the root node
        parent = None

        # iterate through the entire tree
        while current:
            parent = current
            current = current.left_child if val < current.val else current.right_child

        if(val < parent.val):
            parent.left_child = Node(val)
        else:
            parent.right_child = Node(val)

    def insert_recursive(self, val):
        if val < self.val:
            if self.left_child:
                self.left_child.insert_recursive(val)
            else:
                self.left_child = Node(val)
                return
        else:
            if self.right_child:
                self.right_child.insert_recursive(val)
            else:
                self.right_child = Node(val)
                return


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert_iteration(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return self.root

    def insert_recursion(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return self.root
```

### Explanation for the recursive case:

The `insert_iteration(val)` function takes an integer value and if the root exists, it calls the Node class’s `insert()` function on it; otherwise,
it makes the root the value to be inserted.

It starts from the `root` of the tree and moves on to the `left or right` sub-tree depending on whether the value
to be inserted is less than or greater than or equal to the node. While traversing, it stores the parent node of each current node
and when the current node becomes empty or None, it inserts the value there. It does so by making the value to be inserted the current
node (which is None)'s parent’s child. In other words, the value is inserted in place of the current node.

### Explanation for the recursive case:

This implementation starts with the `root` and calls the `insert_recursive()` function on its `left` child if **val is less than the value at the root**,
and calls it on its `right` child if **val is greater than or equal to the value at the root**. This continues until a None node is reached.

At that point, a new node is created and returned to the previous leaf node, which is now the parent of the new node that we just created.

<br/>

## Searching for element in BST

We can implement a `search()` function for binary search trees `iteratively` and `recursively` which will return a node from the tree if the value to be searched matches it.

Here is a high-level description of the algorithm:

- Set the **current node** equal to `root`.
- If the **value** is less than the ‘**current node’s**’ value, then move on to the **left-subtree** otherwise move on to the **right sub-tree**
- Repeat until the value at the ‘current node’ is equal to the value searched or it becomes None.
- Return the current node

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

    def insert_iteration(self, val):
        if self:
            self = Node(val)
            return

        current,parent = self,None
        while current:
            parent = current
            if val < current.val:
                current = current.left_child
            else:
                current = current.right_child

        if(val < parent.val):
            parent.left_child = Node(val)
        else:
            parent.right_child = Node(val)

    def search_iterative(self, val):
        current = self
        while current:
            if val < current.val:
                current = current.left_child
            elif val > current.val:
                current = current.right_child
            else:
                return True

        return None


    def search_recursive(self, val):
        if val < self.val:
            if self.left_child:
                return self.left_child.search_recursive(val)
            else:
                return None
        elif val > self.val:
            if self.right_child:
                return self.right_child.search_recursive(val)
            else:
                return None
        else:
            return True

        return None

class BinarySearchTree:
  def __init__(self,data):
    self.root = Node(data)

  def insert(self,data):
    if self.root:
      self.root.insert(data)
    else:
      self.root = Node(data)
      return self.root

  def search(self,data):
    if self.root:
      self.root.search_iterative(data)
    else:
      return None
```

### Explanation for the iterative case

In this implementation, the core of the `search` function is implemented in the `Node` class. The `BinarySearchTree` first checks if **root is None**, if so, it returns **False**, otherwise, it calls the Node class’s `search_iterative()` function on the root.

The `search_iterative()` function sets current to `self` and goes into a while loop which traverses the tree comparing val to the values of the `left` and `right` child nodes. If val is less than the value at the current node, we move on to the left subtree and if it is greater, we move on to the right subtree until we reach a leaf node or the value being searched for.

### Explanation for the recursive case

In this implementation, the main part of the function is in the Node class. **The recursive base-case is if the given node is equal to the one being searched, return True.** If the base cases are not true, the function checks if the value being searched for is less than or equal to the value of the given node. It moves on to the right or left child accordingly and calls the `search_recursive()` function on them if they are not `None`, if they are, it returns False. **If the entire tree has been traversed, it returns False.**

<br/>

## Deletion in a BST

In general, to `delete` a node in a BST, you will search for it and, once found, you’ll make it `None` by making the `left` or `right` child of its parent `None`. However, to make things simpler, we’ve identified **six** possible cases involved in BST node deletion. We’ll tackle each one separately.

1. Deleting in an empty tree
2. Deleting a node with no children, i.e., a leaf node.
3. Deleting a node which has one child only

- Deleting a node which has a right child only
- Deleting a node which has a left child only

4. Deleting a node with two children

### Deleting an empty tree

If the given starting node is `Null` then do nothing and return `False`. This is an edge case for error handling.

### Deleting a Leaf Node

When the node to be deleted is a `leaf` node in a Binary Search Tree, we simply remove that leaf node. We do this by making the parent node’s `left` or `right` child (whichever one the leaf node was) as `None`.

### Deleting a node which has one child

We search for the node, once the node is found we check if and how many children it has. If it has only **one** child, we check the parent node to see if the **current** node is the **left** or **right** child and then replace its child node with the current node.

### Deleting a node with two children

- From the given node to be deleted, find either the node with the smallest value in the right sub-tree or the node with the largest value in the left sub-tree. Suppose you want to find the smallest value in the right sub-tree; you do this by moving on to every node’s left child until the last left child is reached.
- Replace the node to be deleted with the node found (the smallest node in the right sub-tree or the largest node in the left sub-tree).
- Finally, delete the node found (the smallest in the right sub-tree).

```python
# Deleting an empty tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

    def insert(self, val):
        if val < self.val:
            if self.left_child:
                self.left_child.insert(val)
            else:
                self.left_child = Node(val)
                return
        else:
            if self.right_child:
                self.right_child.insert(val)
            else:
                self.right_child = Node(val)
                return

    def search(self, val):
        if val < self.val:
            if self.left_child:
                return self.left_child.search(val)
            else:
                return False
        elif val > self.val:
            if self.right_child:
                return self.right_child.search(val)
            else:
                return False
        else:
            return True
        return False

    def delete(self, val):
        if val < self.val:
            if self.left_child:
                self.left_child = self.left_child.delete(val)
            else:
                return None
        elif val > self.val:
            if self.right_child:
                self.right_child = self.right_child.delete(val)
            else:
                return None
        else:
            # If we want to delete a leaf node
            if self.left_child is None and self.right_child is None:
                self = None
                return None
            # If we want to delete a node with right_child
            elif self.left_child is None:
                temp = self.right_child
                self = None
                return temp
            # If we want to delete a node with left_child
            elif self.right_child is None:
                temp = self.left_child
                self = None
                return temp
            # If we want to delete a node having both child
            else:
                current = self.right_child
                while current.left_child:
                    current = current.left_child
                self.val = current.val
                self.right_child = self.right_child.delete(current.val)

        return self

class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True

    def search(self, val):
        if self.root:
            return self.root.search(val)
        else:
            return False

    def delete(self, val):
        if self.root:
            self.root = self.root.delete(val)
        else:
          return None
```

<br/>

## Pre-order traversal

In this traversal, the elements are traversed in **“root-left-right”** order. We first visit the **root/parent node, then the left child, and then the right child**. Here is a high-level description of the algorithm for Pre-Order traversal, starting from the root node:

- Visit the `current` node, i.e., print the value stored at the node
- Call the `pre_order_traversal()` function on the `left` sub-tree of the `current` Node.
- Call the `pre_order_traversal()` function on the `right` sub-tree of the `current` Node.

### Implementation in Python

```python
# Assume that the Node class is similar to the prev implementation
class BinarySearchTree:
  def __init__(self,val):
      self.root = Node(val)

  def pre_order_traversal(self, node):
        if node:
            print(node.val)
            self.pre_order_traversal(node.left_child)
            self.pre_order_traversal(node.right_child)
```

### Explanation

First, we create an object of the `BinarySearchTree` class and `insert` some values into it. We will then pass the **tree’s root** to the `pre_order_traversal()` function. If the node given is not None, this function prints the value at the node and calls **pre_order_traversal()** on the `left child` first and then on the `right child`.

This is a linear time algorithm, i.e., the **time complexity** of is in `O(n)` because a total of `n recursive calls` occur.

<br/>

## Post-order traversal

In this traversal, the elements are traversed in **left-right-root”** order. We first visit the **the left child, then the right child and lastly root/parent node**. Here is a high-level description of the algorithm for Post-Order traversal, starting from the root node:

- Traverse the `left` sub-tree of the `current` node recursively by calling the `post_order_traversal()` function on it.
- Traverse the `right` sub-tree of the `current` node recursively by calling the `post_order_traversal()` function on it.
- Visit current node and print its value

### Implementation in Python

```python
# Assume that the Node class is similar to the prev implementation
class BinarySearchTree:
  def __init__(self,val):
      self.root = Node(val)

  def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left_child)
            self.post_order_traversal(node.right_child)
            print(node.val)
```

### Explanation

First, we create an object of the `BinarySearchTree` class and `insert` some values into it. We then pass the **tree’s root** to the `post_order_traversal()` function. If the node given is not None, this function calls `post_order_traversal()` on the `left child` first, then on the `right child`, and then finally prints the value at the node.

This is a linear time algorithm, i.e., the **time complexity** of is in `O(n)` because a total of `n recursive calls` occur.

<br/>

## In-order traversal

In this traversal, the elements are traversed in **left-root-right** order. We first visit the **the left child, then root/parent node and lastly the right child**. Here is a high-level description of the algorithm for In-Order traversal, starting from the root node:

- Traverse the `left` sub-tree of the `current` node recursively by calling the `in_order_traversal()` function on it.
- Visit current node and print its value
- Traverse the `right` sub-tree of the `current` node recursively by calling the `in_order_traversal()` function on it.

### Implementation in Python

```python
# Assume that the Node class is similar to the prev implementation
class BinarySearchTree:
  def __init__(self,val):
      self.root = Node(val)

  def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left_child)
            print(node.val)
            self.in_order_traversal(node.right_child)
```

### Explanation

First, we create an object of the `BinarySearchTree` class and `insert` some values into it. We then pass the **tree’s root** to the `in_order_traversal()` function. If the node given is not None, this function calls `in_order_traversal()` on the `left child` first, then on root and lastly on the `right child`

This is a linear time algorithm, i.e., the **time complexity** of is in `O(n)` because a total of `n recursive calls` occur.
