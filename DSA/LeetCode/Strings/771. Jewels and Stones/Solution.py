class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_set = set(jewels)
        return sum(s in stone_set for s in stones)
