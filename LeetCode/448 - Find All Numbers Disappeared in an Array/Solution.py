class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = list(range(1, len(nums)+1))

        for index, num in enumerate(nums):
            arr[num-1] = -1
        return filter(lambda x: x != -1, arr)

# Alternate solution


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1

        return [i+1 for i, n in enumerate(nums) if n > 0]
