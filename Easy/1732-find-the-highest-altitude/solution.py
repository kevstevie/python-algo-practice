# Problem: #1732 - Find the Highest Altitude
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/find-the-highest-altitude/
# Submitted: 2026-06-19
# Tags: Array, Prefix Sum
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        cur = 0

        for i in gain:
            cur += i
            ans = max(cur, ans)

        return ans
