# Problem: #2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
# Submitted: 2026-08-11
# Tags: Array, Hash Table, Sorting
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = set(nums)
        cur = nums[0]
        tot = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == cur + 1:
                cur = nums[i]
                tot += cur
            else:
                break
                
        while tot in s:
            tot += 1

        return tot
