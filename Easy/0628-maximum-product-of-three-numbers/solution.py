# Problem: #628 - Maximum Product of Three Numbers
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/maximum-product-of-three-numbers/
# Submitted: 2026-07-26
# Tags: Array, Math, Sorting
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        ans = max(nums[0] * nums[1] * nums[2], nums[0] * nums[1] * nums[-1], \
        nums[0] * nums[-2] * nums[-1], nums[-3] * nums[-2] * nums[-1])

        return ans
