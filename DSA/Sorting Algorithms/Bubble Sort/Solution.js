/*
 * Time Complexity: O(N^2)
 * Space Complexity: O(1)
 */
function bubbleSort(lst) {
  n = lst.length
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (lst[j] > lst[j + 1]) {
        const temp = lst[j + 1]
        lst[j + 1] = lst[j]
        lst[j] = temp
      }
    }
  }
  return lst
}

//Driver code
/*
bubbleSort([])
bubbleSort([731, 22, 53, 14, 255])
bubbleSort([352, 6252, 122, 3272, 3262, 22, 353])
*/