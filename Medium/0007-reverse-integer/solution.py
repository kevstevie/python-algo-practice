# Problem: #7 - Reverse Integer
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/reverse-integer/
# Submitted: 2026-05-03
# Tags: Math
class Solution:
    def reverse(self, x: int) -> int:
        v = str(x)
        ans = 0
        
        if v[0] == "-":
            ans = int("-" + v[-1:0:-1])
        else:
            ans = int(v[::-1])

        return 0 if ans > 2**31 - 1 or ans < -2**31 else ans
