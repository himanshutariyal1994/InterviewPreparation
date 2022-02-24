class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = float("-inf")

        for i in accounts:
            cust_sum = sum(i)

            if cust_sum > max_wealth:
                max_wealth = cust_sum

        return max_wealth
