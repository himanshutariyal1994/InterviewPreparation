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

    def search_iterative(self, val):
        if not self.root:
            return None
        else:
            return self.root.search_iterative(val)

    def search_recursive(self, val):
        if not self.root:
            return None
        else:
            return self.root.search_recursive(val)

    def delete(self, val):
        if self.root:
            self.root = self.root.delete(val)
        else:
            return None

    def pre_order_traversal(self, node):
        if node:
            print(node.val)
            self.pre_order_traversal(node.left_child)
            self.pre_order_traversal(node.right_child)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left_child)
            self.post_order_traversal(node.right_child)
            print(node.val)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left_child)
            print(node.val)
            self.in_order_traversal(node.right_child)


BST = BinarySearchTree(6)
BST.insert_iteration(4)
BST.insert_iteration(9)
BST.insert_iteration(5)
BST.insert_iteration(2)
BST.insert_iteration(8)
BST.insert_iteration(12)

BST.pre_order_traversal(BST.root)
print('*******************')
BST.post_order_traversal(BST.root)
print('*******************')
BST.in_order_traversal(BST.root)
