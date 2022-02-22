class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        for i, num in enumerate(nums):
            n ^= i ^ num
        return n


# Another solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int(0.5 * n * (n+1)) - sum(nums)
