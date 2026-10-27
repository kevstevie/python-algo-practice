# Problem: #3963 - Create Grid With Exactly One Path
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/create-grid-with-exactly-one-path/
# Submitted: 2026-10-27
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = ['.' * n]

        for i in range(1, m):
            ans.append('#' * (n - 1) + '.')

        return ans
