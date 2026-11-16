# Problem: #2243 - Calculate Digit Sum of a String
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/calculate-digit-sum-of-a-string/
# Submitted: 2026-11-16
# Tags: String, Simulation
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        while n > k:
            temp = ''
            for i in range(0, n, k):
                start = i
                last = min(i + k, n)
                cur = 0
                for j in range(start, last):
                    cur += int(s[j])
                temp += str(cur)
            s = temp
            n = len(s)
        
        return s
