# Problem: #2078 - Two Furthest Houses With Different Colors
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/two-furthest-houses-with-different-colors/
# Submitted: 2026-04-20
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        rev = colors[::-1]
        for i in range(n):
            if colors[0] != rev[i] or colors[-1] != colors[i]:
                return n - i - 1
