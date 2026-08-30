# Problem: #2091 - Removing Minimum and Maximum From Array
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
# Submitted: 2026-08-30
# Tags: Array, Greedy
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_v = float('inf')
        max_v = float('-inf')
        min_idx = -1
        max_idx = -1
        n = len(nums)

        for i in range(n):
            num = nums[i]
            if min_v > num:
                min_v = num
                min_idx = i
            if max_v < num:
                max_v = num
                max_idx = i

        r = max(max_idx, min_idx)
        l = min(max_idx, min_idx)

        return min(r + 1, l + 1 + n - r, n - l)
