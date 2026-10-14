# Problem: #3727 - Maximum Alternating Sum of Squares
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/maximum-alternating-sum-of-squares/
# Submitted: 2026-10-14
# Tags: Array, Greedy, Sorting
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        l = sorted(x ** 2 for x in nums)
        half = len(nums) // 2

        return sum(l[half:]) - sum(l[:half])
