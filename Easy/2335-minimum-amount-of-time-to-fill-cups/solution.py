# Problem: #2335 - Minimum Amount of Time to Fill Cups
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
# Submitted: 2026-10-29
# Tags: Array, Greedy, Sorting, Heap (Priority Queue)
class Solution:
    def fillCups(self, amount: list[int]) -> int:
        ans = 0
        amount.sort()
        while amount[2] != 0:
            amount[2] -= 1
            amount[1] -= 1
            ans += 1
            amount.sort()
        return ans
