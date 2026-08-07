# Problem: #3345 - Smallest Divisible Digit Product I
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/smallest-divisible-digit-product-i/
# Submitted: 2026-08-07
# Tags: Math, Enumeration
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 101):
            num = i
            prod = 1
            while num > 0:
                prod *= (num % 10)
                num //= 10
            if prod % t == 0:
                return i
        
