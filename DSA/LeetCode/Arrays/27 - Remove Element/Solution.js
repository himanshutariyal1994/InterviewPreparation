/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
  let i = 0,
    j = nums.length - 1;
  let removedEle;

  while (i <= j) {
    if (nums[i] === val) {
      nums[i] = nums[j]
      j--
    } else {
      i++;
    }
  }
  return i
};