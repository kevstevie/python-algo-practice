# Problem: #3674 - Minimum Operations to Equalize Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-operations-to-equalize-array/
# Submitted: 2026-04-18
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return 0 if len(set(nums)) == 1 else 1
