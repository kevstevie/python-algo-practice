# Problem: #3871 - Count Commas in Range II
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/count-commas-in-range-ii/
# Submitted: 2026-09-09
# Tags: Math
class Solution:
    def countCommas(self, n: int) -> int:
        t = n - 999
        m = 1
        ans = 0

        while t >= 0:
            ans += t
            m += 1
            t -= 1000 ** m - 1000 ** (m - 1)
        
        return ans
