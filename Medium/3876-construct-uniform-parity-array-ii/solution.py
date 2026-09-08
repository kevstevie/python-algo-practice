# Problem: #3876 - Construct Uniform Parity Array II
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/construct-uniform-parity-array-ii/
# Submitted: 2026-09-08
# Tags: Array, Math
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        cnt = 0
        n = len(nums1)

        for i in nums1:
            if i % 2 == 1:
                min_odd = min(min_odd, i)
            else:
                cnt += 1
        if n == cnt:
            return True

        for i in nums1:
            if i % 2 == 0 and i < min_odd:
                return False

        return True
