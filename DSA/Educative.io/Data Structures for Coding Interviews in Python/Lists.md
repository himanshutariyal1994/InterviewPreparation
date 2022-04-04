# List in Python

In Python, a list is an ordered sequence of heterogeneous elements. In other words, a list can hold elements with different data types. For example,

```python
list = ['a', 'apple', 23, 3.14]
example_list = [3.14159, 'apple', 23] # Create a list of elements
empty_list = [] # Create an empty list
sequence_list = list(range(10)) # Create a list of first 10 whole numbers
print(example_list)
print(empty_list)
print(sequence_list)
```

So lists can hold integers, strings, characters, functions, and pretty much any other data type including other lists simultaneously!

```python
a_list = [2, 'Educative', 'A']


def foo():
    print('Hello from foo()!')


another_list = [a_list, 'Python', foo, ['yet another list']]

print(another_list[0])  # Elements of 'aList'
print(another_list[0][1])  # Second element of 'aList'
print(another_list[1])  # 'Python'
print(another_list[3])  # 'yet another list'

# You can also invoke the functions inside a list!
another_list[2]()  # 'Hello from foo()!'
```

## List comprehension

A Python technique called list comprehension is used to iterate over the initial array. With list comprehension, checking a condition and appending to the new list can all be done in one line. The code for it starts and ends with a ‘[’ and ends with a ‘]’. The basic syntax is:

```python
newList = [expression(i) for i in oldList if filter(i)]

lst = [1,2,3,4,5]
new_lst = [num**num for num in lst]
print(new_lst)
```

## Important list functions

### append() method

Use this function to add a single element to the end of a list. This function works in **O(1)**, constant time.

```python
list = [1, 3, 5, 'seven']
print(list)
list.append(9)
print(list)
```

### insert() method

Insert element to the list at the specified index. Format is **insert(index,element)** and it works in **O(n)** time

```python
list = [1, 3, 5, 'seven']
list.insert(0, 2)
print(list)
```

### remove() method

Removes the specified element from the list, and throws an **ValueError** if the element is not present. Check the existence of the element using the **in** keyword before using this method. Format is **remove(element)** and works in **O(n)** time

```python
list = [1, 3, 5, 'seven']
print(list)
list.remove('seven')
print(list)
print(0 in list)
list.remove(0)
print(list)
```

### pop() method

Removes the element at a specified index. If no index is provided, it removes the last element by default. If no index is provided, it works in **O(1)** time and otherwise it works in **O(N)** time.

```python
list = [1, 3, 5, 'seven']
print(list)
list.pop(2)
print(list)
list.pop()
print(list)
```

### reverse() method

This method reverses the entire list. Works in **O(N)** time and in-place meaning that it does not return a new list

```python
list = [1, 3, 5, 'seven']
print(list)
list.reverse()
print(list)
```

### sort() method

This method sorts the list in ascending order and works in **O(N LOG N)** time

```python
list = [43,4,8,1,22]
list.sort()
print(list)
```

## Slicing lists

Accessing and modifying several elements from objects such as lists/tuples/strings requires using a for loop in most languages. However, in Python, you can use **square brackets and a colon** to define a range of elements within a list that you want to access or **‘slice’**.

> list[start:end]

Here **start** and **end** indicate the starting and ending index of a list that is desired to be accessed.

### Indexing elements of a list

Also, note that it is not necessary to specify the last or the first index explicitly, you can simply leave the end or start index blank respectively.

> list[start:] means all numbers greater than start uptil the range
> list[:end] means all numbers less than end uptil the range
> list[:] means all numbers within the range

```python
list = list(range(10))
print(list[3:])  # 3, 4, 5, 6, 7, 8, 9
print(list[:3])  # 0 1 2
print(list[:])  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

### Stepped indexing

You can do the same in Python very concisely with the notation:

> list[start:stop:step]
> where **step** indicates the increment in the indices while traversing through the list

### Initializing list elements

You can add/modify the contents of a list by specifying a range of elements that you want to update and setting it to the new value:

> arr[start:end] = [list, of, New, values]

```python
x = list(range(5))
print(x)  # 0, 1, 2, 3, 4
x[1:3] = [45, 21, 83,77]
print(x)  # 0, 45, 21, 83, 4
```

### Deleting elements from a list

The **del** keyword is used to delete elements from a list. In the following example, all the elements at even-numbered indices are deleted.

```python
list = list(range(10))
print(list)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
del list[::2]
del list[1]
print(list)  # 1, 3, 5, 7, 9
```

## Negative Indexing

We can use negative numbers to begin indexing the list elements from the end. For example, to access the **fifth-last** element of a list, we use:

> list[-5]

---

# Arrays in Python

In Python, an array is just an ordered sequence of **homogeneous** elements. In other words, an array can only hold elements of one datatype. The type of array is constrained and specified at the time of creation.

Python arrays are initialized using the array library:

```python
import array
new_array = array.array('type', [list])
```

> Here `type` defines the data type of array and `list` is a python list containing homogenous elements. It would be an empty list if we need to create a new empty array

## Types of array

There are several types of arrays in Python; refer to the table below for a complete list.

| Type code | C Type          | Python Type | Minimum Size in Bytes |
| --------- | --------------- | ----------- | --------------------- |
| 'c'       | 'character      | char        | 1                     |
| 'i'       | 'signed int'    | int         | 2                     |
| 'I'       | 'unsigned int'  | long        | 4                     |
| 'l'       | 'signed long'   | int         | 4                     |
| 'L'       | 'unsigned long' | long        | 4                     |
| 'f'       | 'float'         | float       | 4                     |
| 'd'       | 'double'        | double      | 8                     |

## Array slicing

Array slicing is done the same way as list slicing

```python
import array

initializer_list = [2, 5, 43, 5, 10, 52, 29, 5]
number_array = array.array('i', initializer_list)

print(number_array[1:5])  # 5,43,5,10
print(number_array[:-5])  # 2,5,43
print(number_array[5:])  # 52,29,5
print(number_array[:])   # all elements
```

## Changing or adding array elements

Elements can be changed the same way as list elements. You can also concatenate 2 arrays using the `+` operator or add several items using the **extend()** method

```python
import array

odd = array.array('i', [1, 3, 5])
even = array.array('i', [2, 4, 6])

integers = array.array('i')   # creating empty array of integer
integers = odd + even
print(integers)

numbers = array.array('i', [1, 2, 3])
numbers.append(4)
print(numbers)  # array('i', [1, 2, 3, 4])

# extend() appends iterable to the end of the array
numbers.extend([5, 6, 7])
print(numbers)     # array('i', [1, 2, 3, 4, 5, 6, 7])
```

## Removing or deleting array elements

To delete one or more elements from the array, use the **del()** method. Alternatively, the **remove(val)** or the **pop(index)** methods can also be used to remove specific elements or elements at a specific index.

> `Note`: An error is thrown if the index exceeds the size of the array or element is not found in the array.

```python
import array
integer_array = array.array('i', [1, 2, 3, 3, 4])

del integer_array[2]  # removing third element
print(integer_array)  # Output: array('i', [1, 2, 3, 4])

del integer_array  # deleting entire array
print(integer_array)  # Error: array is not defined

integer_array = array.array('i', [10, 11, 12, 12, 13])

integer_array.remove(12)
print(integer_array)   # array('i', [10, 11, 12, 13])

print(integer_array.pop(2))   # Output: 12
print(integer_array)   # array('i', [10, 11, 13])
```

# Arrays vs Lists

> Python lists are very flexible and can hold completely heterogeneous arbitrary data, but they use a lot more space than Python arrays. Each list contains pointers to a block of pointers, each of which in turn points to a full Python object. Again, the advantage of the list is flexibility: because each list element is a full structure containing both data and type information, the list can be filled with data of any desired type. Arrays lack this flexibility but are much more efficient for storing and manipulating data.

> The differences between the two largely exist because of the aforementioned backend implementation. Arrays in Python are implemented just like C arrays, with a pointer pointing to the first element of the array with the rest existing contiguously in the memory.

> Because of the way that lists are implemented, elements can be appended to them very efficiently. If you want your collection to grow and shrink in a time-efficient manner, then lists should be used. It’s also better to use lists if you need to manage lots of different data types, however, arrays are better when you need to store a lot of data and perform a large number of computationally intensive mathematical operations.
