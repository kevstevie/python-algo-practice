# Problem: #120 - Triangle
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/triangle/
# Submitted: 2026-04-10
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        inf = float('inf')
        l = len(triangle[-1])
        dp = [[inf] * l for _ in range(l)]
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(i + 1):
                dp[i][j] = triangle[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])

        return min(dp[-1])
