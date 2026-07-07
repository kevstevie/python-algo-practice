# Problem: #1288 - Remove Covered Intervals
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/remove-covered-intervals/
# Submitted: 2026-07-07
# Tags: Array, Sorting
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sort = sorted(intervals, key=lambda x: (x[0], -x[1]))

        cur = sort[0]
        n = len(intervals)
        ans = n
        for i in range(1, n):
            pres = cur[0]
            pree = cur[1]
            j = sort[i]
            nexs = j[0]
            nexe = j[1]
            if pres <= nexs and pree >= nexe:
                ans -= 1
            if pree < nexe:
                cur = j

        return ans
