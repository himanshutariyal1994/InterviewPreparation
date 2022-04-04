/* 
 * Time Complexity: O(n)
 * Space Complexity: O(1) 
 */
function findMinimum(arr1) {
  let min = arr1[0]

  for (let num of arr1) {
    if (min > num) {
      min = num
    }
  }
  return min
}