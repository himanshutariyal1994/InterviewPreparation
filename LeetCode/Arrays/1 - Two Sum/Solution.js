/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  if (!nums || nums.length === 0) {
    return [];
  }

  const hashMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (hashMap.has(nums[i])) {
      return [i, hashMap.get(nums[i])];
    }
    hashMap.set(target - nums[i], i);
  }
  return [];
}