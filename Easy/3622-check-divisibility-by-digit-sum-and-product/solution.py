# Problem: #3622 - Check Divisibility by Digit Sum and Product
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
# Submitted: 2026-08-24
# Tags: Math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        tot = 0
        prod = 1
        cur = n

        while cur > 0:
            num = cur % 10
            cur //= 10
            tot += num
            prod *= num
        
        return n % (tot + prod) == 0
