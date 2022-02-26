class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Brute force solution
        '''
        result = []
        length_nums = len(nums)

        for i in range(length_nums):
          numbers = 0

          for j in range(length_nums):
            if i != j and nums[i] > nums[j]:
              numbers += 1

          result.append(numbers)

        return result
        '''

        # Optimal solution
        len_nums = len(nums)
        sorted_nums = nums[:]
        sorted_nums.sort()

        hashMap = {}
        for i in range(len_nums):
            if sorted_nums[i] not in hashMap:
                hashMap[sorted_nums[i]] = i

        for i in range(len_nums):
            nums[i] = hashMap[nums[i]]

        return nums
