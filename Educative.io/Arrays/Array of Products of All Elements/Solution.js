function findProduct(arr) {
  let result = []
  let left_side = 1
  let right_side = 1

  for (let i in arr) {
    result[i] = right_side
    right_side *= arr[i]
  }

  for (let i = arr.length - 1; i >= 0; i--) {
    result[i] *= left_side
    left_side *= arr[i]
  }

  return result
}