# Problem: #3867 - Sum of GCD of Formed Pairs
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/
# Submitted: 2026-07-16
# Tags: Array, Math, Two Pointers, Sorting, Simulation, Number Theory
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        gcd = []
        mx = 0
        for i in nums:
            mx = max(i, mx)
            gcd.append(math.gcd(i, mx))

        gcd.sort()
        l = 0
        r = len(gcd) - 1
        ans = 0
        while l < r:
            ans += math.gcd(gcd[l], gcd[r])
            r -= 1
            l += 1
        return ans
