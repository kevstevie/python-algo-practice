# Problem: #3653 - XOR After Range Multiplication Queries I
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/xor-after-range-multiplication-queries-i/
# Submitted: 2026-04-08
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 1000000007
        for query in queries:
            (l, r, k, v) = query
            for i in range(l, r + 1, k):
                nums[i] = nums[i] * v % mod

        return reduce(lambda acc, cur: acc ^ cur, nums)
