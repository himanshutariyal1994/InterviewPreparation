function findSum(arr, value) {
  let set = new Set();

  for (const i of arr) {
    if (set.has(value - i)) {
      return [i, value - i]
    }
    set.add(i)
  }
  return false;
}