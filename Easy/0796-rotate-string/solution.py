# Problem: #796 - Rotate String
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/rotate-string/
# Submitted: 2026-05-03
# Tags: String, String Matching
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            rotate = s[i:] + s[:i]
            if rotate == goal:
                return True
        return False
