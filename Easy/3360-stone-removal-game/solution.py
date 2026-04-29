# Problem: #3360 - Stone Removal Game
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/stone-removal-game/
# Submitted: 2026-04-29
# Tags: Math, Simulation
class Solution:
    def canAliceWin(self, n: int) -> bool:
        ans = False

        for i in range(10, 0, -1):
            n -= i
            if n < 0:
                return ans
            ans = not ans

        return ans
