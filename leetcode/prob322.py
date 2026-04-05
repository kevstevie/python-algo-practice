from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for i in range(amount + 1):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i - j] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
