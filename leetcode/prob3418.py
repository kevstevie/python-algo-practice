from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        row = len(coins)
        col = len(coins[0])
        dp = [[[-float('inf')] * 3 for _ in range(col)] for _ in range(row)]

        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = 0

        for j in range(1, col):
            dp[0][j][0] = dp[0][j-1][0] + coins[0][j]
            dp[0][j][1] = max(dp[0][j-1][1] + coins[0][j], dp[0][j-1][0])
            dp[0][j][2] = max(dp[0][j-1][2] + coins[0][j], dp[0][j-1][1])

        for i in range(1, row):
            dp[i][0][0] = dp[i-1][0][0] + coins[i][0]
            dp[i][0][1] = max(dp[i-1][0][1] + coins[i][0], dp[i-1][0][0])
            dp[i][0][2] = max(dp[i-1][0][2] + coins[i][0], dp[i-1][0][1])

        for i in range(1, row):
            for j in range(1, col):
                best_from = lambda k: max(dp[i-1][j][k], dp[i][j-1][k])

                dp[i][j][0] = best_from(0) + coins[i][j]
                dp[i][j][1] = max(best_from(1) + coins[i][j], best_from(0))
                dp[i][j][2] = max(best_from(2) + coins[i][j], best_from(1))

        return max(dp[row-1][col-1])
