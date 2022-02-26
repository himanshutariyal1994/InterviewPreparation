class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_arr = []
        i = 0

        while i < n:
            new_arr.append(nums[i])
            new_arr.append(nums[n+i])
            i += 1
        return new_arr
