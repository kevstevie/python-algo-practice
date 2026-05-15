# Problem: #153 - Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Submitted: 2026-05-15
# Tags: Array, Binary Search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minv = float('inf')

        while l <= r:
            mid = (l + r) // 2
            minv = min(nums[mid], minv)
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return minv
