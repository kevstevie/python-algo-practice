# Problem: #3644 - Maximum K to Sort a Permutation
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/maximum-k-to-sort-a-permutation/
# Submitted: 2026-10-23
# Tags: Array, Bit Manipulation
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        for i, v in enumerate(nums):
            if i != v:
                ans &= i
        if ans == -1:
            return 0
        return ans
