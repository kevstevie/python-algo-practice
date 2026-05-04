# Problem: #48 - Rotate Image
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/rotate-image/
# Submitted: 2026-05-04
# Tags: Array, Math, Matrix
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = n - 1

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                matrix[j][m - i], matrix[m - i][m - j], matrix[m - j][i], matrix[i][j] \
                = matrix[i][j], matrix[j][m - i], matrix[m - i][m - j], matrix[m - j][i]
