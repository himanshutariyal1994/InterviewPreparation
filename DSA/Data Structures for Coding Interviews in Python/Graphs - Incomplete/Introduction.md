# Graph Structure

A graph is a data structure containing a set of nodes that are connected to each other in the form of a network. First of all, we’ll define the `two` basic components of a graph.

## Vertex

A `vertex` is the most essential part of a graph. A collection of vertices forms a graph. In that sense, vertices are similar to `linked list nodes`.

## Edge

An `edge` is the `link` between two vertices. It can be `uni-directional or bi-directional` depending on your graph. An edge can also have a cost associated with it.

<br/>

# Graph Terminologies

There are several terms used to describe the properties of graphs.

> `Degree of a Vertex`: The total number of edges incident on a vertex. There are two types of degrees:

- `In-Degree`: The total number of incoming edges of a vertex.

- `Out-Degree`: The total number of outgoing edges of a vertex.

> `Parallel Edges`: Two undirected edges are parallel if they have the same end vertices. Two directed edges are parallel if they have the same starting and ending vertices.

> `Self Loop`: This occurs when an edge starts and ends on the same vertex.

> `Adjacency`: Two vertices are said to be adjacent if there is an edge connecting them directly.

<br/>

# Types of Graphs

There are two common types of graphs:

- **Undirected**
- **Directed**

## Undirected Graph

In an `undirected` graph, the edges are `bi-directional`. For e.g., an `ordered pair (2, 3)` shows that there exists an edge between vertex `2` and `3` without any specific direction. You can go from vertex `2 to 3` or from `3 to 2`.

Let’s calculate the **maximum number of edges** for an undirected graph. We are denoting an edge between vertex a and b as (a, b). So, the **maximum possible edges of a graph with n vertices will be all possible pairs of vertices of that graph**, assuming that there are no self-loops.

If a graph has n vertices, then there are `C (n,2)` possible pairs of vertices, so by solving C (n,2) by binomial coefficients gives us `(n*(n-1))/2` maximum possible edges in an undirected graph.

## Directed Graph

In a `directed` graph, the edges are `unidirectional`. For a pair (2, 3), there exists an edge from vertex 2 towards vertex 3 and the only way to traverse is to go from 2 to 3, not the other way around.

This changes the maximum number of edges that can exist in the graph. **For a directed graph with n vertices, the minimum number of edges that can connect a vertex with every other vertex is n-1. This excludes self-loops. If you have n vertices, then all the possible edges become n\*(n-1).**

<br/>

# Representation of Graphs

The two most common ways to represent a graph are:

- `Adjacency Matrix`
- `Adjacency List`

## Adjacency Matrix

The `adjacency matrix` is a `two-dimensional matrix where each cell can contain a 0 or 1`. If a cell contains 1, there exists an edge between the corresponding vertices e.g., **Matrix[0][1]=1 shows that an edge exists between vertex 0 and 1.** The row and column headings represent the vertices.

> There is a directed graph that has an edge going from vertex 0 to vertex 1, so there is a 1 at Matrix[0][1] in the adjacency matrix. In the case of the undirected graph, we would have Matrix[1][0] = 1 as well since the edge is bidirectional.
>
> For a `directed` graph, the usual convention is to think of the `rows as sources and columns as destinations`.

## Adjacency List#

An `array` of `linked lists` is used to store all the edges in the graph. The size of the array is `equal` to the **number of vertices** in the graph. Each index of the array contains a vertex. This vertex points to a linked list that contains all the vertices connected to this one.

Example:

!["Graphs as Adjacency List](/DSA/Educative.io/Data%20Structures%20for%20Coding%20Interviews%20in%20Python/Graphs/Graphs%20as%20Adjacency%20Lists.png "Graphs as Adjacency List")

**As you can see in the diagram above, all the vertices that connect directly to a vertex are appended in the corresponding linked list. If a new vertex is added to the graph, it is simply added to the array as well.**

Note: In an `undirected` graph an edge is represented with both adjacent nodes having their linked list populated with the corresponding nodes.

<br/>

# Graph Implementation using Adjacency List

The implementation will be based on the `adjacency list` model. The linked list class we created earlier will be used to represent adjacent vertices.

## The Graph Class

`Graph` class consists of two data members:

- The `total number of vertices` in the graph
- A `list of linked lists` to store adjacent vertices

The `variable` vertices contains an integer specifying the total number of vertices. The second component is `array`, which will act as our `adjacency list`. We simply have to run a loop and create a linked list for each vertex.

## Additional Functionality

Now, we’ll add `two methods` to make this class functional:

- `print_graph()` - **Prints the content of the graph**
- `add_edge()` - **Connects a source with a destination**

```python
# Entire implementation of a Graph using adjacency list
class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        if(self.is_empty()):
            self.head_node = temp_node
            return self.head_node
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    # Inserts a value at the end of the list
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)
        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return
        # if list not empty, traverse the list to the last node
        temp = self.get_head()
        while temp.next_element is not None:
            temp = temp.next_element
        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    def length(self):
        # start from the first element
        curr = self.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length

    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if (first_element is not None):
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    def delete(self, value):
        deleted = False
        if self.is_empty():  # Check if list is empty -> Return False
            print("List is Empty")
            return deleted
        current_node = self.get_head()  # Get current node
        previous_node = None  # Get previous node
        if current_node.data is value:
            self.delete_at_head()  # Use the previous function
            deleted = True
            return deleted

        # Traversing/Searching for Node to Delete
        while current_node is not None:
            # Node to delete is found
            if value is current_node.data:
                # previous node now points to next node
                previous_node.next_element = current_node.next_element
                current_node.next_element = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next_element

        return deleted

    def search(self, dt):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head_node
        while(temp is not None):
            if(temp.data is dt):
                return temp
            temp = temp.next_element

        print(dt, " is not in List!")
        return None

    def remove_duplicates(self):
        if self.is_empty():
            return

        # If list only has one node, leave it unchanged
        if self.get_head().next_element is None:
            return

        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node  # Iterator for the inner loop
            while inner_node:
                if inner_node.next_element:
                    if outer_node.data == inner_node.next_element.data:
                        # Duplicate found, so now removing it
                        new_next_element = inner_node.next_element.next_element
                        inner_node.next_element = new_next_element
                    else:
                        # Otherwise simply iterate ahead
                        inner_node = inner_node.next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            outer_node = outer_node.next_element
        return


class Graph:
    def __init__(self,vertices):
        # Total number of vertices
        self.vertices = vertices

        # Defining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []

        # Creating a new LinkedList for each vertex/index of the list
        for i in range(vertices):
            # Appending a new LinkedList on each array index
            self.array.append(LinkedList())

    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_head(destination)

            # Uncomment the following line for undirected graph
            # self.array[destination].insert_at_head(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")

g = Graph(4)
g.add_edge(0, 2)
g.add_edge(0, 1)
g.add_edge(1, 3)
g.add_edge(2, 3)

g.print_graph()

print(g.array[1].get_head().data)
print(g.array[0].get_head().data)
```

## add_edge (self, source, destination)

> Thanks to the `Graph` constructor, `source` and `destination` are already stored as indices of our list. This function simply inserts a `destination` vertex into the adjacency linked list of the source vertex by running the following line of code:

> array[source].insert_at_head(destination)

One important thing to note is that we are implementing a directed graph, so `add_edge(0, 1) is not equal to add_edge(1, 0)`. **In the case of an undirected graph, we will have to create an edge from the source to the destination and from the destination to the source, making it a bidirectional edge**:

> array[source].insert_at_head(destination)
> array[destination].insert_at_head(source)

`add_edge()` will not work if `source is less than zero and greater than or equal to the number of vertices`. Likewise, `destination also has to be greater than or equal to 0 and less than the number of vertices`.

## print_graph(self)

This function uses a simple nested loop to iterate through the adjacency list. **Each linked list is being traversed here**.

<br/>

# Complexities of Graph Operations

Let's discuss the performance of the two graph representations.
Below, you can find the time complexities for the `4 basic graph functions`.

Note that, in this table, `V means the total number of vertices and E means the total number of edges in the Graph`.

| Operation                 | Adjacency List | Adjacency Matrix |
| ------------------------- | -------------- | ---------------- |
| Add Vertex                | O(1)           | O(V^2)           |
| Remove Vertex             | O(V+E)         | O(V^2)           |
| Add Edge                  | O(1)           | O(1)             |
| Remove Edge               | O(E)           | O(1)             |
| Search                    | O(V)           | O(1)             |
| Breadth First Search(BFS) | O(V+E)         | O(V^2)           |
| Depth First Search(DFS)   | O(V+E)         | O(V^2)           |

## Adjacency List

- **Adding an edge in adjacency lists takes constant time as we only need to insert at the head node of the corresponding vertex.**

- **Removing an edge takes O(E) time because, in the worst case, all the edges could be at a single vertex and hence, we would have to traverse all E edges to reach the last one.**

- **Removing a vertex takes O(V + E) time because we have to delete all its edges and then reindex the rest of the list one step back in order to fill the deleted spot.**

- **Searching an edge between a pair of vertices can take up to O(V) if all V nodes are present at a certain index and we have to traverse them.**

## Adjacency Matrix

- **Edge operations are performed in constant time as we only need to manipulate the value in the particular cell.**

- **Vertex operations are performed in O(V^2) since we need to add rows and columns. We will also need to fill all the new cells.**

- **Searching an edge is O(1) because we can access each edge by indexing.**

## Comparison

Both representations are suitable for different situations. **If your application frequently manipulates vertices, the adjacency list is a better choice. If you are dealing primarily with edges, the adjacency matrix is the more efficient approach.**
