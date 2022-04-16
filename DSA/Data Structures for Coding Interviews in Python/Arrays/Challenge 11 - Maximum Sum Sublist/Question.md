# Challenge 11: Maximum Sum Sublist

Given an array, find the contiguous sublist with the largest sum.

## Maximum sublist sum: An overview

Given an unsorted list A, the maximum sum sub list is the sub list (contiguous elements) from A for which the sum of the elements is maximum. In this challenge, we want to find the sum of the maximum sum sub list.

This problem is a tricky one because the list might have negative integers in any position, so we have to cater to those negative integers while choosing the continuous sublist with the largest positive values.

## Problem statement

Given an integer list, return the maximum sublist sum. The list may contain both positive and negative integers and is unsorted using the method `find_max_sum_sublist(lst)`

## Input

A list

## Output

a number (maximum subarray sum)

## Sample input

```
[-4,2,-5,1,2,3,6,-5,1]
```

## Sample output

> largest_sum = 12 (1+2+3+6)
