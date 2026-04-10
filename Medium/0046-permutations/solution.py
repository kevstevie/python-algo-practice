# Problem: #46 - Permutations
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/permutations/
# Submitted: 2026-04-09
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr, v):
            if len(arr) == len(nums):
                res.append(arr[:])
                return
            for i in range(len(nums)):
                if v[i]:
                    continue
                arr.append(nums[i])
                v[i] = True
                backtrack(arr, v)
                arr.pop()
                v[i] = False

        backtrack([], [False] * len(nums))
        return res
