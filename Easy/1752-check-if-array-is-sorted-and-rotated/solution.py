# Problem: #1752 - Check if Array Is Sorted and Rotated
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# Submitted: 2026-05-24
# Tags: Array
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                cnt += 1

        return cnt <= 1
