# Problem: #3612 - Process String with Special Operations I
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/process-string-with-special-operations-i/
# Submitted: 2026-06-17
# Tags: String, Simulation
class Solution:
    def processStr(self, s: str) -> str:
        ans = ''

        for c in s:
            n = len(ans)
            if c == '#':
                for i in range(n):
                    ans += ans[i]
                continue
            if c == '*':
                ans = ans[0:n - 1]
                continue
            if c == '%':
                ans = ans[::-1]
                continue
            ans += c
        return ans
            
