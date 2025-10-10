class Solution:
    def maxProfit(self, prices):
        min_pric = prices[0]
        mx_prof = 0

        for price in prices[1:]:
            mx_prof = max(mx_prof, price - min_pric)
            min_pric = min(min_pric, price)

        return mx_prof


prices = [7, 6, 4, 3, 1]
p2 = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(sol.maxProfit(prices))
print(sol.maxProfit(p2))
