# Problem: #3740 - Minimum Distance Between Three Equal Elements I
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/
# Submitted: 2026-04-10
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = float('inf')
        m = {}

        for i,v in enumerate(nums):
            m[v] = m.get(v, [])
            m[v].append(i)
            if len(m[v]) >= 3:
                arr = m[v]
                cand = (arr[-1] - arr[-3]) * 2
                ans = min(cand, ans)

        return -1 if ans == float('inf') else ans
