# Problem: #2923 - Find Champion I
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/find-champion-i/
# Submitted: 2026-07-08
# Tags: Array, Matrix
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            cnt = 0
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
            if cnt == n - 1:
                return i
