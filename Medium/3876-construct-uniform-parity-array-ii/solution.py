# Problem: #3876 - Construct Uniform Parity Array II
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/construct-uniform-parity-array-ii/
# Submitted: 2026-09-08
# Tags: Array, Math
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return all(x % 2 == 0 for x in nums1) or min(nums1) % 2 == 1
