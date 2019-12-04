class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        days = len(prices)
        dp = [[0, -float('inf')] for _ in range(days + 1)]
        for i in range(1, days + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(-prices[i - 1], dp[i - 1][1])

        return dp[days][0]