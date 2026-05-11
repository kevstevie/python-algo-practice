# Problem: #2553 - Separate the Digits in an Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/separate-the-digits-in-an-array/
# Submitted: 2026-05-11
# Tags: Array, Simulation
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(j) for i in nums for j in str(i)]
