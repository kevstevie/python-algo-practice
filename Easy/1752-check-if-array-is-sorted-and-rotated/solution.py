# Problem: #1752 - Check if Array Is Sorted and Rotated
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# Submitted: 2026-05-24
# Tags: Array
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        for start in range(n):
            flag = True
            for i in range(1, n):
                idx_prev = (start + i - 1) % n
                idx_next = (start + i) % n
                if nums[idx_prev] > nums[idx_next]:
                    flag = False
                    break
            if flag:
                return True
        return False
