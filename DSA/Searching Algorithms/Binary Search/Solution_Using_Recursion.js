/*
 * Time Complexity: O(log N) since it divides the array in half for each pass
 * Space Complexity: O(1)
 * The array should be sorted to perform binary search --> O(N log N) for sorting array
 */
var binarySearch = function (lst, n) {
  // Assuming list is sorted in ascending order
  let index = -1
  if (!lst || lst.length === 0) {
    return index
  }

  return binarySearchUsingRecursion(lst, n, 0, lst.length - 1)
}

var binarySearchUsingRecursion = function (lst, n, start, end) {
  if (start > end) {
    return -1
  }

  let mid = Math.floor((start + end) / 2);

  if (lst[mid] > n) {
    return binarySearchUsingRecursion(lst, n, start, mid - 1)
  } else if (lst[mid] === n) {
    return mid
  } else {
    return binarySearchUsingRecursion(lst, n, mid + 1, end)
  }
}

//Driver code
/*
binarySearch([], 1)
binarySearch([1, 2, 3, 4, 5], 3)

or 

binarySearchUsingRecursion([], 1,0,-1)
binarySearchUsingRecursion([1, 2, 3, 4, 5], 3,0,4)

*/