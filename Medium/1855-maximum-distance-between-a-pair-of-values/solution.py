# Problem: #1855 - Maximum Distance Between a Pair of Values
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
# Submitted: 2026-04-19
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n = len(nums1)
        m = len(nums2)
        p1 = 0
        p2 = 0

        while p1 < n and p2 < m:
            num1 = nums1[p1]
            num2 = nums2[p2]
            if num1 <= num2:
                ans = max(ans, p2 - p1)
                p2 += 1
            else:
                p1 += 1
                p2 += 1
        return ans
