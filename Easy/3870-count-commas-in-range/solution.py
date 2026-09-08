# Problem: #3870 - Count Commas in Range
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/count-commas-in-range/
# Submitted: 2026-09-08
# Tags: Math
class Solution:
    def countCommas(self, n: int) -> int:
        t = n - 1000
        m = 1
        ans = 0

        while t >= 0:
            ans += t * m + 1
            m += 1
            t -= 1000 ** m
        
        return ans
