class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        palin, num = 0, x
        while x > 0:
            palin = (palin*10) + x % 10
            x //= 10

        return num == palin
