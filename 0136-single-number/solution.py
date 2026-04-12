# Problem: #136 - Single Number
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/single-number/
# Submitted: 2026-04-12
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)
