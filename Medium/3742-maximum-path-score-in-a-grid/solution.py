# Problem: #3742 - Maximum Path Score in a Grid
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/maximum-path-score-in-a-grid/
# Submitted: 2026-04-30
# Tags: Array, Dynamic Programming, Matrix
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        inf = -float('inf')
        dp = [[[inf] * (k + 1) for j in range(m)] for i in range(n)]
        dp[0][0][0] = 0

        for i in range(1, m):
            for j in range(k + 1):
                v = grid[0][i]
                c = 0 if v == 0 else 1
                if j - c >= 0 and dp[0][i - 1][j - c] != inf:
                    dp[0][i][j] = dp[0][i - 1][j - c] + v

        for i in range(1, n):
            for j in range(k + 1):
                v = grid[i][0]
                c = 0 if v == 0 else 1
                if j - c >= 0 and dp[i - 1][0][j - c] != inf:
                    dp[i][0][j] = dp[i - 1][0][j - c] + v

        for i in range(1, n):
            for j in range(1, m):
                for l in range(k + 1):
                    v = grid[i][j]
                    c = 0 if v == 0 else 1
                    if l - c < 0:
                        continue
                    dp[i][j][l] = max(dp[i - 1][j][l - c], dp[i][j - 1][l - c]) + v

        ans = max(dp[n - 1][m - 1])
        return ans if ans != inf else -1
