# Problem: #2220 - Minimum Bit Flips to Convert Number
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
# Submitted: 2026-11-18
# Tags: Bit Manipulation
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s_b = []
        g_b = []

        while start > 0:
            s_b.append(start % 2)
            start //= 2
        while goal > 0:
            g_b.append(goal % 2)
            goal //= 2

        while len(g_b) != len(s_b):
            if len(g_b) > len(s_b):
                s_b.append(0)
            else:
                g_b.append(0)
        
        return sum(1 for i in range(len(s_b)) if s_b[i] != g_b[i])
