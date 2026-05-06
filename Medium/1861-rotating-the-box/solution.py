# Problem: #1861 - Rotating the Box
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/rotating-the-box/
# Submitted: 2026-05-06
# Tags: Array, Two Pointers, Matrix
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n = len(boxGrid)
        m = len(boxGrid[0])

        moved = [["."] * m for i in range(n)]

        for i in range(n):
            st = []
            idx = m - 1
            for j in range(m):
                st.append((j, boxGrid[i][j]))
            while st:
                pop = st.pop()
                if pop[1] == "*":
                    moved[i][pop[0]] = "*"
                    idx = pop[0] - 1
                    continue
                if pop[1] == "#":
                    moved[i][idx] = "#"
                    idx -= 1

                
        ans = [["."] * n for i in range(m)]

        for i in range(n):
            for j in range(m):
                ans[j][n - i - 1] = moved[i][j]

        return ans
