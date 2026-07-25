# Problem: #3536 - Maximum Product of Two Digits
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/maximum-product-of-two-digits/
# Submitted: 2026-07-25
# Tags: Math, Sorting
class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []

        while n > 0:
            arr.append(n % 10)
            n //= 10
        
        arr.sort()

        return arr[-2] * arr[-1]
