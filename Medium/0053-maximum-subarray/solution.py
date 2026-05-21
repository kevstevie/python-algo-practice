# Problem: #53 - Maximum Subarray
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/maximum-subarray/
# Submitted: 2026-05-21
# Tags: Array, Divide and Conquer, Dynamic Programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)
