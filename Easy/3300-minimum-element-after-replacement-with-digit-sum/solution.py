# Problem: #3300 - Minimum Element After Replacement With Digit Sum
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
# Submitted: 2026-05-30
# Tags: Array, Math
class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sums(a):
            res = 0
            while a > 0:
                res += a % 10
                a //= 10
            return res

        return min(sums(i) for i in nums)
