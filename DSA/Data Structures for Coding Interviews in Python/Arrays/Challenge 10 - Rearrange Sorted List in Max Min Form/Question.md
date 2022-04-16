# Challenge 10: Rearrange Sorted List in Max/Min Form

Arrange elements in such a way that the maximum element appears at first position, then minimum at second, then second maximum at third and second minimum at fourth and so on.

## Problem Statement

Implement a function called `max_min(lst)` which will re-arrange the elements of a sorted list such that the 0th index will have the largest number, the 1st index will have the smallest, and the 2nd index will have second-largest, and so on. In other words, all the even-numbered indices will have the largest numbers in the list in descending order and the odd-numbered indices will have the smallest numbers in ascending order.

## Input:

A sorted list

## Output:

A list with elements stored in max/min form

## Sample Input

```
lst = [1,2,3,4,5]
```

## Sample Output

```
lst = [5,1,4,2,3]
```
