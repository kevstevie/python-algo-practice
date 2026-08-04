# Problem: #3731 - Find Missing Elements
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/find-missing-elements/
# Submitted: 2026-08-04
# Tags: Array, Hash Table, Sorting
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set()
        minv = float('inf')
        maxv = float('-inf')

        for i in nums:
            s.add(i)
            minv = min(minv, i)
            maxv = max(maxv, i)
        
        ans = []

        for i in range(minv, maxv + 1):
            if i not in s:
                ans.append(i)
        
        return ans
