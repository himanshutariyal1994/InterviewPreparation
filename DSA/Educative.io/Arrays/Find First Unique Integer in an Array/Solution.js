function findFirstUnique(arr) {
  const map = new Map()

  for (let i = 0; i < arr.length; i++) {
    if (map.has(arr[i])) {
      map.set(arr[i], -1)
    } else {
      map.set(arr[i], i)
    }
  }

  for (const [key, value] of map.entries()) {
    if (value > -1) {
      return key
    }
  }
  return -1
}