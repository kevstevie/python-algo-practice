# Problem: #416 - Partition Equal Subset Sum
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/partition-equal-subset-sum/
# Submitted: 2026-04-06
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        acc = sum(nums)

        if acc % 2 == 1:
            return False

        target = acc // 2
        dp = [True] + [False] * target

        for i in nums:
            for j in range(target, 0, -1):
                if j - i >= 0 and dp[j - i]:
                    dp[j] = True

        return dp[acc // 2]
