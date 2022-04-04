# Challenge 9: Rearrange Positive & Negative Values

Given a list, can you rearrange its elements in such a way that the negative elements appear at one end and positive elements appear at the other? Solve this problem in Python and see if your code runs correctly!

## Problem Statement

Implement a function `rearrange(lst)` which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. Note that it is not necessary to maintain the sorted order of the input list.

> Generally zero is NOT positive or negative, we will treat zero as a positive integer for this challenge! So, zero will be placed at the right.

## Output

A list with negative elements at the left and positive elements at the right

## Sample Input

```
[10,-1,20,4,5,-9,-6]
```

## Sample Output

```
[-1,-9,-6,10,20,4,5]
```
