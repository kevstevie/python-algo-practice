# Problem: #1833 - Maximum Ice Cream Bars
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/maximum-ice-cream-bars/
# Submitted: 2026-06-21
# Tags: Array, Greedy, Sorting, Counting Sort
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mv = 10 ** 5 + 1
        count = [0] * mv

        for i in costs:
            count[i] += 1

        ans = 0

        for i in range(mv):
            if count[i] == 0:
                continue
            if i > coins:
                break
            minv = min(count[i],coins // i)
            ans += minv
            coins -= minv * i

        return ans
