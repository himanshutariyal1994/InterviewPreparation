class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}

        for i, char in enumerate(s):
            if char in dict:
                dict[char] = -1
            else:
                dict[char] = i

        for i in dict.keys():
            if dict[i] > -1:
                return dict[i]

        return -1
