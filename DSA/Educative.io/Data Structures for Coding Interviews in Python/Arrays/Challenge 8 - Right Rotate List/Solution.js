function rightRotate(arr, n) {
  let arr_len = arr.length;

  if (arr_len === 0) {
    return arr
  } else {
    n = n % arr_len
  }

  const pivot = arr_len - n
  return [...arr.slice(pivot, arr_len), ...arr.slice(0, pivot)]
}