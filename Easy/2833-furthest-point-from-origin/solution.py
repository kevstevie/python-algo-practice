# Problem: #2833 - Furthest Point From Origin
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/furthest-point-from-origin/
# Submitted: 2026-04-24
# Tags: String, Counting
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n = 0
        m = 0
        for i in moves:
            if i == "L":
                n += 1
            if i == "R":
                n -= 1
            if i == "_":
                m += 1
        
        return abs(n) + m
