# Problem: #3550 - Smallest Index With Digit Sum Equal to Index
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
# Submitted: 2026-07-02
# Tags: Array, Math
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(a):
            res = 0
            while a > 0:
                res += a % 10
                a //= 10
            return res
        for i in range(len(nums)):
            if i == digit_sum(nums[i]):
                return i
        return -1
