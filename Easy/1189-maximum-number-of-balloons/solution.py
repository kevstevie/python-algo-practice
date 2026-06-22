# Problem: #1189 - Maximum Number of Balloons
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/maximum-number-of-balloons/
# Submitted: 2026-06-22
# Tags: Hash Table, String, Counting
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = {'b','a','l','o','n'}
        d = {}

        for c in s:
            d[c] = 0

        for c in text:
            if c in s:
                d[c] += 1
        
        d['l'] //= 2
        d['o'] //= 2

        return min(d.values())
            
