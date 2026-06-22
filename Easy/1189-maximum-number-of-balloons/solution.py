# Problem: #1189 - Maximum Number of Balloons
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/maximum-number-of-balloons/
# Submitted: 2026-06-22
# Tags: Hash Table, String, Counting
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        words = 'balloon'
        s = {c for c in words}
        d = {i:0 for i in s}

        for c in text:
            if c in s:
                d[c] += 1
        
        d['l'] //= 2
        d['o'] //= 2

        return min(d.values())
            
