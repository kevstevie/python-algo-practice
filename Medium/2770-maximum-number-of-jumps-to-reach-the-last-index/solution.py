# Problem: #2770 - Maximum Number of Jumps to Reach the Last Index
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/
# Submitted: 2026-05-10
# Tags: Array, Dynamic Programming
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] + [-1] * (n - 1)

        for i in range(n):
            for j in range(i):
                if abs(nums[i] - nums[j]) <= target and dp[j] != -1:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1] if dp[-1] != 0 else -1
