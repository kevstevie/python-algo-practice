# Problem: #162 - Find Peak Element
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/find-peak-element/
# Submitted: 2026-04-12
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l
