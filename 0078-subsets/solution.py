# Problem: #78 - Subsets
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/subsets/
# Submitted: 2026-04-08
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(s, arr):
            res.append(arr[:])
            for i in range(s, len(nums)):
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()
        backtrack(0, [])

        return res
