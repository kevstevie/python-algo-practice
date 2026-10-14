# Problem: #3723 - Maximize Sum of Squares of Digits
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
# Submitted: 2026-10-14
# Tags: Math, Greedy
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = ""

        while num > 0:
            tem = min(sum, 9)
            sum -= tem
            num -= 1
            ans += str(tem)
        
        if sum > 0:
            return ""
        return ans
