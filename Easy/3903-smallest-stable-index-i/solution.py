# Problem: #3903 - Smallest Stable Index I
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/smallest-stable-index-i/
# Submitted: 2026-09-06
# Tags: Array, Prefix Sum
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        INF = float('inf')
        ans = INF
        n = len(nums)
        max_left = nums[0]
        min_right = [0] * n
        min_right[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])

        for i in range(n):
            v = max_left - min_right[i]
            if v <= k:
                ans = min(ans, i)
            if i == n:
                break
            max_left = max(max_left, nums[i])
        
        
        ans = -1 if ans == INF else ans
        return ans
