# Problem: #2033 - Minimum Operations to Make a Uni-Value Grid
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
# Submitted: 2026-04-28
# Tags: Array, Math, Sorting, Matrix
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for i in grid:
            for j in i:
                arr.append(j)

        arr.sort()
        mid = arr[len(arr) // 2]

        ans = 0

        for i in arr:
            sub = abs(i - mid)
            if sub % x != 0:
                return -1
            ans += sub // x
        return ans
