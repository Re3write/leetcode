class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10000 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i>= coin:
                   dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[amount] == 10000:
            return -1
        else:
            return dp[amount]