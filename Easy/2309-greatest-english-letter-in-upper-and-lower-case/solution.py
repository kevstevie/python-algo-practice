# Problem: #2309 - Greatest English Letter in Upper and Lower Case
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
# Submitted: 2026-08-10
# Tags: Hash Table, String, Enumeration
class Solution:
    def greatestLetter(self, s: str) -> str:
        upper = [False] * 26
        lower = [False] * 26

        for c in s:
            if 'z' >= c >= 'a':
                lower[ord(c) - ord('a')] = True
            else:
                upper[ord(c) - ord('A')]= True
        
        for i in range(25, -1, -1):
            if upper[i] and lower[i]:
                return chr(ord('A') + i)
        
        return ""
