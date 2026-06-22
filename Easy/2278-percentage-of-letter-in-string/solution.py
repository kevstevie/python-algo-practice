# Problem: #2278 - Percentage of Letter in String
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/percentage-of-letter-in-string/
# Submitted: 2026-06-22
# Tags: String
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return floor(s.count(letter) / len(s) * 100)
