# Problem: #3286 - Find a Safe Walk Through a Grid
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
# Submitted: 2026-07-02
# Tags: Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        q = []
        n = len(grid)
        m = len(grid[0])
        v = [[False] * m for i in range(n)]

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        heapq.heappush(q, (grid[0][0] ,0, 0))

        while q:
            pop = heapq.heappop(q)
            if v[pop[1]][pop[2]]:
                continue
            v[pop[1]][pop[2]] = True
            if pop[0] >= health:
                break
            if pop[1] == n - 1 and pop[2] == m - 1:
                return True
            for i in range(4):
                x = pop[1] + dx[i]
                y = pop[2] + dy[i]
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if v[x][y]:
                    continue
                heapq.heappush(q, (pop[0] + grid[x][y], x, y))

        return False
