/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const hashMap = {}

  for (let num of nums) {
    if (num in hashMap) {
      return true
    }
    hashMap[num] = 1
  }
  return false
};