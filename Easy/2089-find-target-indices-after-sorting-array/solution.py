# Problem: #2089 - Find Target Indices After Sorting Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Submitted: 2026-10-19
# Tags: Array, Binary Search, Sorting
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        return ans
