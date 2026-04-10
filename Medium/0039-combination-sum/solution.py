# Problem: #39 - Combination Sum
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/combination-sum/
# Submitted: 2026-04-06
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(result, arr, start):
            if result == target:
                ans.append(arr[:])
                return

            if result > target:
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                arr.append(num)
                backtrack(result + num, arr, i)
                arr.pop()

        backtrack(0, [], 0)
        return ans
