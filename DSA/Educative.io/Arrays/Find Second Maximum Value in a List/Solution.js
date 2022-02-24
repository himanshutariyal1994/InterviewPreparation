// Brute force approach
/*
function findSecondMinimum(lst) {
  if (!lst || lst.length < 2) {
    return -1
  }

  lst.sort()
  return lst[lst.length - 2]
}
*/

// Optimal approach
function findSecondMaximum(lst) {
  if (!lst || lst.length < 2) {
    return -1
  }

  let first_max = Number.NEGATIVE_INFINITY
  let second_max = Number.NEGATIVE_INFINITY

  for (let num of lst) {
    if (first_max < num) {
      second_max = first_min
      first_max = num
    } else if (second_max < num && num != first_max) {
      second_max = num
    }
  }

  return second_max
}