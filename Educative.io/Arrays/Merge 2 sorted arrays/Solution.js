/* Using a new array
Time Complexity: O(n + m)
Space Complexity: O(n + m) */
function mergeArrays(arr1, arr2) {
  let i = 0,
    j = 0,
    arr = [];

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      arr.push(arr1[i]);
      i++;
    } else {
      arr.push(arr2[j]);
      j++;
    }
  }

  if (i < arr1.length) {
    arr = [...arr, arr1.slice(i)]
  }
  if (j < arr2.length) {
    arr = [...arr, arr2.slice(j)]
  }
  return arr
}

/* Not using a new array
Time Complexity: O(n + m)
Space Complexity: O(n + m) */

function mergeArrays(arr1, arr2) {
  let i = 0,
    j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] > arr2[j]) {
      arr1.splice(i, 0, arr2[j]);
      i++;
      j++
    } else {
      i++;
    }
  }

  if (j < arr2.length) {
    arr1 = [...arr1, arr2.slice(j)]
  }
  return arr1;
}