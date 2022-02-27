class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        temp = 0

        for i in s:
            temp += 1 if i == 'R' else -1
            if temp == 0:
                counter += 1

        return counter
