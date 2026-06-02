# Problem: #2144 - Minimum Cost of Buying Candies With Discount
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
# Submitted: 2026-06-02
# Tags: Array, Greedy, Sorting
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans = 0
        cost.sort()
        for i in range(len(cost)):
            v = cost.pop()
            if i % 3 != 2:
                ans += v

        return ans
