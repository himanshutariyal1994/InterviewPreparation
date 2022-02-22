/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function (nums) {
  const arr = Array(nums.length).fill().map((v, i) => ++i);

  for (let num of nums) {
    arr[num - 1] = -1
  }

  return arr.filter((num) => num !== -1);
};

// Alternate solution
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function (nums) {
  for (let i in nums) {
    const index = Math.abs(nums[i]) - 1;
    if (nums[index] > 0) {
      nums[index] *= -1
    }
  }

  const result = []
  for (let j in nums) {
    if (nums[j] > 0) {
      result.push(++j);
    }
  }
  return result;
}