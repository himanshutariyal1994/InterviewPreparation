/*
 * Time Complexity: O(N^2)
 * Space Complexity: O(1)
 */
function selectionSort(lst) {
  n = lst.length
  for (let i = 0; i < n; i++) {
    // Finding the smallest element in the sub-array
    let min = i
    for (let j = i + 1; j < n; j++) {
      if (lst[j] < lst[min]) min = j
    }

    if (min !== i) {
      // Swap the element
      const temp = lst[min]
      lst[min] = lst[i]
      lst[i] = temp
    }
  }
  return lst
}

//Driver code
/*
selectionSort([])
selectionSort([731, 22, 53, 14, 255])
selectionSort([352,6252,122,3272,3262,22,353])
*/