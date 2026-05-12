# Problem: #1665 - Minimum Initial Energy to Finish Tasks
# Difficulty: Hard
# Language: Python3
# URL: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
# Submitted: 2026-05-12
# Tags: Array, Greedy, Sorting
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        ans = 0
        cur = 0

        tasks.sort(key=lambda x: -x[1] + x[0])
        
        for (n, m) in tasks:
            if cur < m:
                dif = m - cur
                ans += dif
                cur = m
            cur -= n

        return ans
