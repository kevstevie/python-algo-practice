# Problem: #3364 - Minimum Positive Sum Subarray 
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-positive-sum-subarray/
# Submitted: 2026-11-16
# Tags: Array, Sliding Window, Prefix Sum
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        n = len(nums)

        for i in range(n):
            if i + l > n:
                break
            v = sum(nums[i:i + l])
            if v > 0:
                ans = min(ans, v)
            for j in range(i + l, n):
                if j >= i + r:
                    break
                v += nums[j]
                if v > 0:
                    ans = min(ans, v)

        if ans == float('inf'):
            return -1
        else:
            return ans
