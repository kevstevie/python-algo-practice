# Problem: #2540 - Minimum Common Value
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-common-value/
# Submitted: 2026-08-13
# Tags: Array, Hash Table, Two Pointers, Binary Search
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l = 0
        n = len(nums1)
        r = 0
        m = len(nums2)

        while l < n and r < m:
            num1 = nums1[l]
            num2 = nums2[r]

            if num1 == num2:
                return num1
            if num1 < num2:
                l += 1
            else:
                r += 1
        return -1
