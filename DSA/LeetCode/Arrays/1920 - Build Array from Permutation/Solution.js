/**
 * @param {number[]} nums
 * @return {number[]} ans
 * 
 */
// Uses O(N) space complexity
var buildArray = function (nums) {
  const ans = []

  for (const i in nums) {
    ans.push(nums[nums[i]])
  }
  return ans
};

// Uses O(1) space complexity
var buildArray = function (nums) {
  const q = nums.length

  // Create each number in the form of a = qb+r
  for (const i in nums) {
    const r = nums[i]
    const b = nums[nums[i]] % q
    nums[i] = q * b + r
  }

  for (const i in nums) {
    nums[i] = Math.floor(nums[i] / q)
  }

  return nums
}