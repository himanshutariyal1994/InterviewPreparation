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

  let start = 0;
  let end = lst.length - 1

  while (start <= end) {
    const mid = Math.floor((start + end) / 2)
    if (lst[mid] > n) {
      end = mid - 1
    } else if (lst[mid] < n) {
      start = mid + 1
    } else {
      return mid;
    }
  }
  return index
}

//Driver code
/*
binarySearch([], 1)
binarySearch([1, 2, 3, 4, 5], 3)
*/