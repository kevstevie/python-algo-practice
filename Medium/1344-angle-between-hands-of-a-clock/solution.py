# Problem: #1344 - Angle Between Hands of a Clock
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/angle-between-hands-of-a-clock/
# Submitted: 2026-06-18
# Tags: Math
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = 30 * hour % 360
        m = 30 * minutes / 5

        h += 30 * minutes / 5 / 12

        return min(abs(h - m), 360 - abs(h - m))
