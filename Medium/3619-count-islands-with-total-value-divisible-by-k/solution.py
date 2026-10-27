# Problem: #3619 - Count Islands With Total Value Divisible by K
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/
# Submitted: 2026-10-27
# Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        n = len(grid[0])
        m = len(grid)
        v = [[False] * n for _ in range(m)]

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[j][i] == 0 or v[j][i]:
                    continue
                temp = 0
                st = [(i, j)]
                v[j][i] = True
                while st:
                    pop = st.pop()
                    print(pop)
                    x = pop[0]
                    y = pop[1]
                    temp += grid[y][x]
                    for l in range(4):
                        d_x = dx[l]
                        d_y = dy[l]
                        dxx = x + d_x
                        dyy = y + d_y
                        if dxx < 0 or dxx >= n or dyy < 0 or dyy >= m or v[dyy][dxx]:
                            continue
                        if grid[dyy][dxx] == 0:
                            v[dyy][dxx] = True
                            continue
                        st.append((dxx, dyy))
                        v[dyy][dxx] = True

                if temp % k == 0:
                    ans += 1

        return ans
