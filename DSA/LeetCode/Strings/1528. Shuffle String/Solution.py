class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # brute force
        result = [""] * len(indices)

        for index, num in enumerate(indices):
            result[num] = s[index]

        return "".join(result)
