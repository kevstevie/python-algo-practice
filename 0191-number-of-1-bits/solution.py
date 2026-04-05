# Problem: #191 - Number of 1 Bits
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/number-of-1-bits/
# Submitted: 2026-04-05
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n > 0:
            if n % 2 == 1:
                ans += 1
            n //= 2

        return ans