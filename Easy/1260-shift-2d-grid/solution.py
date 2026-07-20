# Problem: #1260 - Shift 2D Grid
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/shift-2d-grid/
# Submitted: 2026-07-20
# Tags: Array, Matrix, Simulation
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        ans = [[0] * m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                p = i * m + j
                af = p + k
                af = af % (n * m)
                x = af // m
                y = af % m
                ans[x][y] = grid[i][j]

        return ans
