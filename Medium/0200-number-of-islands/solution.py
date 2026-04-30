# Problem: #200 - Number of Islands
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/number-of-islands/
# Submitted: 2026-04-13
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        v = [[False] * len(grid[0]) for _ in range(len(grid))]

        ans = 0
        st = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if v[i][j] or grid[i][j] == "0":
                    continue
                st.append((i, j))
                ans += 1
                while st:
                    pop = st.pop()
                    for k in range(4):
                        x = pop[0] + dx[k]
                        y = pop[1] + dy[k]
                        if x < 0 or y < 0 \
                        or x >= len(grid) or y >= len(grid[0]) or v[x][y]:
                            continue
                        v[x][y] = True
                        if grid[x][y] == "1":
                            st.append((x,y))

        return ans
