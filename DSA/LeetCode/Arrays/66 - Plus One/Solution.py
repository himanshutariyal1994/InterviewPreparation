class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_len = len(digits) - 1

        if digits[digits_len] < 9:
            digits[digits_len] += 1
            return digits

        for i in range(digits_len, -1, -1):
            digits[i] += 1
            if digits[i] > 9:
                digits[i] = 0
            else:
                return digits

        digits.insert(0, 1)
        return digits
