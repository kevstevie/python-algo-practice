# Problem: #3498 - Reverse Degree of a String
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/reverse-degree-of-a-string/
# Submitted: 2026-09-20
# Tags: String, Simulation
class Solution:
    def reverseDegree(self, s: str) -> int:
        def code(c):
            return 26 - (ord(c) - ord('a'))
        
        return sum(code(s[i]) * (i + 1) for i in range(len(s)))
