# Problem: #3718 - Smallest Missing Multiple of K
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/smallest-missing-multiple-of-k/
# Submitted: 2026-06-22
# Tags: Array, Hash Table
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = {i for i in nums}
        cur = k

        while cur in s:
            cur += k
        return cur
