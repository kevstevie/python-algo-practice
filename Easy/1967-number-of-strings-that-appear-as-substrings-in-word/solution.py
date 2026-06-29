# Problem: #1967 - Number of Strings That Appear as Substrings in Word
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
# Submitted: 2026-06-29
# Tags: Array, String
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 for i in patterns if i in word)
