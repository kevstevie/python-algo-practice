# Problem: #905 - Sort Array By Parity
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/sort-array-by-parity/
# Submitted: 2026-05-06
# Tags: Array, Two Pointers, Sorting
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] % 2 == 0:
                l += 1
                continue
            if nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                continue
            if nums[r] % 2 == 1:
                r -= 1
        return nums
        
