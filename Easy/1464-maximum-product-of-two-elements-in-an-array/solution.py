# Problem: #1464 - Maximum Product of Two Elements in an Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Submitted: 2026-07-27
# Tags: Array, Sorting, Heap (Priority Queue)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()

        return (nums[-1] - 1) * (nums[-2] - 1)
