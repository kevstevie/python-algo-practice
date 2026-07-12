# Problem: #1331 - Rank Transform of an Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/rank-transform-of-an-array/
# Submitted: 2026-07-12
# Tags: Array, Hash Table, Sorting
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        m = {}
        n = len(arr)
        rank = sorted(arr)
        ans = [0] * n
        cur = 0
        
        for i in range(n):
            num = rank[i]
            if num not in m:
                cur += 1
                m[num] = cur

        for i in range(n):
            ans[i] = m[arr[i]]

        return ans
