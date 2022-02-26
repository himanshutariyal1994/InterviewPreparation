/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
  // Brute force solution
  /* result = []
  for(let i=0;i<nums.length;i++) {
    let lessElements = 0
    
    for(let j = 0;j<nums.length;j++) {
      if(nums[i] != nums[j] && nums[i] > nums[j]) {
        lessElements++;
      }
    }
    result.push(lessElements)
  }
  return result*/

  // Optimal approach
  // Sort the array in descending order
  result = [...nums].sort((a, b) => b - a)
  hashMap = {}

  // Create a map of elements with the number of elements less than it
  const countMap = new Map(result.map((ele, index) => [ele, result.length - index - 1]));

  return nums.map((ele) => countMap.get(ele))
};