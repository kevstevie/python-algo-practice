# Problem: #2913 - Subarrays Distinct Element Sum of Squares I
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
# Submitted: 2026-10-15
# Tags: Array, Hash Table, Binary Indexed Tree, Segment Tree
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                k = len(set(nums[i:j + 1]))
                ans += k ** 2
        return ans
