/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  const n = nums.length;
  const sum = nums.reduce((acc, curr) => acc + curr)
  return 0.5 * n * (n + 1) - sum;
};

// Another solution using sum logic
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  let sum = 0;
  for (let index in nums) {
    sum += (index + 1 - nums[i])
  }
  return sum;
};

// Another solution using XOR logic
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  let number = nums.length
  for (let index in nums) {
    number = number ^ index ^ nums[index]
  }
  return number;
};