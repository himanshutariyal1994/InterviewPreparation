# Using O(n) space complexity


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans


# Using O(1) space complexity
# Note: use Euclid's Division theorem which states that any 2 integers can be written in the form of
# a = qb + r where r is the modulus and b is the divisor

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        q = len(nums)

        for i in range(q):
            r = nums[i]
            b = nums[nums[i]] % q

            nums[i] = q * b + r

        for i in range(q):
            nums[i] = nums[i] // q
