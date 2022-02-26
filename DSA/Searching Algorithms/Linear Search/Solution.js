/*
 * Time Complexity: O(N) since it iterates over the length of the list
 * Space Complexity: O(1)
 */
var linearSearch = function (lst, n) {
  let index = -1
  if (!lst || lst.length === 0) {
    return index
  }

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] === n) {
      return i
    }
  }
  return index
}

//Driver code
/*
linearSearch([], 1)
linearSearch([1, 2, 3, 4, 5], 3)
linearSearch([4, 55, 25, 63, 68, 36, 44], 68)
*/