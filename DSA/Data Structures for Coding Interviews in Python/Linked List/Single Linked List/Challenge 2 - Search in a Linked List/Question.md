# Challenge 2: Search in a Singly Linked List

To search for a specific value in a linked list, there is no other approach but to traverse the whole list until we find the desired value.
In that sense, the search operation in linked lists is similar to the linear search in normal lists or arrays - all of them take `O(n)` amount of time.

The search algorithm in a linked list can be generalized to the following steps:

- Start from the head node.
- Traverse the list till you either find a node with the given value or you reach the end node which will indicate that the given node doesn’t exist in the list.

## Input

A linked list and an integer to be searched.

## Output

True if the integer is found. False otherwise.

## Sample Input

```
Linked List = 5->90->10->4
Integer = 4
```

## Sample Output

> True
