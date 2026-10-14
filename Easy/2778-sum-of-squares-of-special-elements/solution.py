# Problem: #2778 - Sum of Squares of Special Elements 
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/sum-of-squares-of-special-elements/
# Submitted: 2026-10-14
# Tags: Array, Enumeration
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(nums[i] ** 2 for i in range(len(nums)) if len(nums) % (i + 1) == 0 )
