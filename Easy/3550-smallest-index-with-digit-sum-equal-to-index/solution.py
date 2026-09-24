# Problem: #3550 - Smallest Index With Digit Sum Equal to Index
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
# Submitted: 2026-09-24
# Tags: Array, Math
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(num):
            tot = 0
            while num > 0:
                tot += num % 10
                num //= 10
            return tot
        for i in range(len(nums)):
            if digit_sum(nums[i]) == i:
                return i
        return -1
