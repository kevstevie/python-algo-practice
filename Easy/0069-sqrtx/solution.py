# Problem: #69 - Sqrt(x)
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/sqrtx/
# Submitted: 2026-09-22
# Tags: Math, Binary Search, Newton's Method
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0 
        r = x // 2 + 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans
