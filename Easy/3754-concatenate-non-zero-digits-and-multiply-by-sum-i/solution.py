# Problem: #3754 - Concatenate Non-Zero Digits and Multiply by Sum I
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
# Submitted: 2026-07-07
# Tags: Math
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        cur = 0
        summ = 0
        mul = 1

        while n > 0:
            if n % 10 != 0:
                summ += n % 10
                cur += n % 10 * mul
                mul *= 10
            n //= 10

        return cur * summ
