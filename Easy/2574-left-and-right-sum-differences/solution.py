# Problem: #2574 - Left and Right Sum Differences
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/left-and-right-sum-differences/
# Submitted: 2026-06-10
# Tags: Array, Prefix Sum
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        for i in range(n - 1):
            left[i + 1] = left[i] + nums[i]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] + nums[i + 1]

        return [abs(left[i] - right[i]) for i in range(n)]
