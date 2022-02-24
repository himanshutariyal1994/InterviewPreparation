from typing import Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_set = set()

        for i in range(0, len(nums)):
            if nums[i] in number_set:
                return True
            number_set.add(nums[i])
        return False
