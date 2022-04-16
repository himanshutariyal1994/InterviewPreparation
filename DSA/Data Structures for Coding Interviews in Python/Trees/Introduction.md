# What is a Tree?

Trees consist of `vertices (nodes)` and `edges` that connect them. Trees are `hierarchical` in nature and are are similar to `Graphs`, except that a `cycle cannot exist` in a Tree - they are `acyclic`. In other words, there is always `exactly one` path between any two nodes.

Some terminologies in Trees:

- `Root Node`: A node with no parent nodes. Generally, trees don’t have to have a root but rooted trees have one `distinguished` node
- `Child Node`: A Node which is linked to an upper node (Parent Node)
- `Parent Nodes`: A Node that has links to one or more Child Nodes
- `Sibling Node`: Nodes that share same Parent Node
- `Leaf Node`: A node that doesn’t have any Child Node
- `Ancestor Nodes`: the nodes on the path from a `node D` to the root node. **Ancestor nodes include node D’s parents, grandparents, and so on**

The figure below shows all the terminologies described above:

!["Basic Structure of a Tree"](/DSA/Educative.io/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Trees/Images/Basic%20Structure%20of%20a%20Tree.png "Basic Structure of a Tree")

In the figure above, **1** is the `Root` as well as `parent node` to child nodes **2,3, and 4**. Node **3** is a parent node to child nodes **6 and 7**. And as nodes **2,3, and 4** share the same parent node **1**, so they are siblings to each other. Similarly, **6 and 7** are also `sibling` nodes as their parent is same, that is **3**.

<br/>

# Other Terminology and Formulas

Some other common terminologies used in trees are:

- `Sub-tree`: For a particular non-leaf node, a collection of nodes, essentially the tree, starting from its child node. The tree formed by a node and its descendants.

- `Degree of a node`: Total number of children of a node

- `Length of a path`: The number of edges in a path

- `Depth of a node n`: The length of the path from a node n to the root node. The depth of the root node is 0.

- `Level of a node n`: (Depth of a Node)+1

- `Height of a node n`: The length of the path from n to its deepest descendant. So the height of the tree itself is the height of the root node and the height of leaf nodes is always 0.

- `Height of a Tree`: Height of its root node

!["Level, Depth and height of a tree"](/DSA/Educative.io/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Trees/Images/Level,%20Depth%20and%20Height%20in%20a%20Tree.png "Level, Depth and height of a tree")

!["Subtrees of a Tree"](/DSA/Educative.io/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Trees/Images/Subtrees%20in%20a%20Tree.png "Subtrees of a Tree")

<br/>

# Types of Trees

Many different types of trees exist which are optimized for particular use-cases. Each tree type offers its own particular structure and hence space-time complexity for different operations. Some commonly used trees include:

- `Binary Trees`
- `Binary Search Trees`
- `AVL Trees`
- `Red-Black Trees`
- `2-3 Trees`

## The N-ary Tree

In graph theory, an `N-ary tree` is a `rooted` tree in which each node has no more than `N` children. It is also sometimes known as a `k-way tree, a k-ary tree, or an M-ary tree`. **A binary tree is a special case where k=2**, so they can have a maximum of 2 child nodes and a minimum of 0 child nodes.

<br/>

# What makes a Tree balanced?

A **binary tree** is `height-balanced` if, for each node in the tree, **the difference between the height of the right subtree and the left subtree** is `atmost one`.

> `|Height(LeftSubTree) - Height(RightSubTree)| <= 1`

The figure below shows a height balanced tree:

!["Height balanced tree"](/DSA/Educative.io/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Trees/Images/Height%20balanced%20tree.png "Height balanced tree")

<br/>

## High-level Algorithm to determine if a tree is height-balanced

- Start from the leaf nodes and move towards the root

- Along with traversing the tree, compute heights of the `left-subtree` and `right-subtree` of each node. **The height of a leaf node is always 0**

- At each node, **check if the difference between the height of the left and right sub-tree is more than 1, if so, it means that the tree is not balanced.**

- If you have completely traversed the tree and haven’t caught the above condition, then the tree is balanced.

<br/>

# What is a Binary Tree?

A **binary tree** is a tree in which each node has between `0-2` children. They’re called the **left** and **right** children of the node. The figure below shows what a Binary Tree looks like:

!["Binary tree"](/DSA/Educative.io/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Trees/Images/Binary%20Tree.png "Binary Tree")

## Types of Binary Trees

### Complete Binary Trees

A `complete binary tree` is a binary tree in which **all the levels of the tree are fully filled**, except for perhaps the nodes at last level.

!["Complete Binary tree"](/DSA/Educative.io/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Trees/Images/Complete%20Binary%20Tree.png "Complete Binary Tree")

!["Incomplete Binary tree"](/DSA/Educative.io/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Trees/Images/Incomplete%20Binary%20Tree.png "Incomplete Binary Tree")

### Full Binary Trees

In a `full` or `proper` binary tree, every node has `0 or 2` children. **No node can have 1 child.**
The **total number of nodes** in a full binary tree of height `‘h’` can be expressed as `2h + 1 <= total number of nodes <= 2^(h+1) - 1`

!["Full and non-Full Binary tree"](/DSA/Educative.io/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Trees/Images/Full%20and%20Incomplete%20Binary%20Tree.png "Full and non-Full Binary Tree")

### Perfect Binary Trees

A Binary tree is said to be `Perfect` if all its internal `nodes have two children` and `all leaves are at the same level`. Also note that,

> The **total number of nodes** in a perfect binary tree of height `h` are given as: `2^(h+1) - 1` while the **total number of leaf nodes** are given as `2^h or (n+1)/2`

The following image shows what a perfect binary looks like:

!["Perfect Binary tree"](/DSA/Educative.io/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Trees/Images/Perfect%20Binary%20Tree.png "Perfect Binary Tree")

<br/>

## Some proprties of Complete Binary Trees with Insertion in Complete Binary Trees

- All the levels are **completely filled** except possibly the last one
- Nodes at the last level are as far left as possible
- The **total number of nodes**, `n` in a complete binary tree of height `h` is expressed as `2^h <= n <= 2^{h+1} - 1`
- The **total number of non-leaf nodes**, `n_i` in a complete binary tree of height `h` is expressed as `2^{h-1} <= n_i <= 2^{h} - 1`
- The **total number of leaf-nodes**, `n_e` in a complete binary tree of height `h` is expressed as `2^{h-1} <= n_e <= 2^{h}`

The following rules apply when inserting a value in a Complete Binary Tree:

- **Nodes are inserted level by level**
- **Fill in the left-subtree before moving to the right one**

<br/>

## Skewed Binary Trees

`Skewed Binary Trees` are Binary trees such that **all the nodes except one have one and only one child**. All of the children nodes are either `left or right child nodes` so the entire tree is positioned to the `left or the right side`. This type of Binary Tree structure should be avoided at all costs because the time complexity of most operations will be high.

### Left-Skewed Binary Trees

**The left-skewed binary tree** has all `left child nodes`.

### Right-Skewed Binary Trees

**Right skewed binary trees** have all `right child nodes`.

!["Left and Right Skewed Binary trees"](/DSA/Educative.io/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Trees/Images/Right%20and%20Left%20skewed%20Tree.png "Left and Right Skewed Binary trees")
