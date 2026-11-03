# Problem: #3736 - Minimum Moves to Equal Array Elements III
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
# Submitted: 2026-11-03
# Tags: Array, Math
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_v = 0
        for i in nums:
            max_v = max(max_v, i)
        return sum(max_v - i for i in nums)
